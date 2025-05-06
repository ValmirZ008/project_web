from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 Профиль"), KeyboardButton(
                text="🎯 Выбрать сложность")],
            [KeyboardButton(text="🏋️ Тренировка"),
             KeyboardButton(text="📚 Учебники")],
            [KeyboardButton(text="📈 Статистика"),
             KeyboardButton(text="⚙️ Настройки")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )


def get_difficulty_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🟢 Лёгкая"), KeyboardButton(
                text="🟡 Средняя"), KeyboardButton(text="🔴 Сложная")],
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True
    )


def get_task_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔁 Новая задача")],
            [KeyboardButton(text="⬅️ В главное меню")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
