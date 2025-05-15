import sqlite3

DB_NAME = "database.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            user_id INTEGER,
            subject TEXT,
            correct INTEGER DEFAULT 0,
            incorrect INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, subject),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id: int, username: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()


def update_stats(user_id: int, subject: str, is_correct: bool):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT correct, incorrect FROM stats WHERE user_id = ? AND subject = ?",
        (user_id, subject)
    )
    row = cursor.fetchone()

    if row:
        if is_correct:
            cursor.execute(
                "UPDATE stats SET correct = correct + 1 WHERE user_id = ? AND subject = ?",
                (user_id, subject)
            )
        else:
            cursor.execute(
                "UPDATE stats SET incorrect = incorrect + 1 WHERE user_id = ? AND subject = ?",
                (user_id, subject)
            )
    else:
        cursor.execute(
            "INSERT INTO stats (user_id, subject, correct, incorrect) VALUES (?, ?, ?, ?)",
            (user_id, subject, int(is_correct), int(not is_correct))
        )

    conn.commit()
    conn.close()


def get_stats(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT correct, incorrect FROM stats WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        correct, incorrect = row
        total = correct + incorrect
        return correct, incorrect, total
    else:
        return 0, 0, 0
