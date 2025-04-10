import telebot
import random
from pyexpat.errors import messages

bot = telebot.TeleBot("7741259913:AAHdSZGIPtNb3wKA6gbBBr3k_wRbDFtalwc")


@bot.message_handler(commands=["start"])
def main(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("Математика", callback_data="math")
    btn2 = telebot.types.InlineKeyboardButton("Физика", callback_data="physics")
    btn3 = telebot.types.InlineKeyboardButton(
        "Информатика", callback_data="informatics"
    )
    markup.row(btn1, btn2, btn3)
    bot.reply_to(message, "Какой предмет вы хотите потренировать?", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    pass

    # print('new handler')


@bot.callback_query_handler(func=lambda call: True)
def handle_subject_selection(call):
    if call.data == "math":
        show_options(call, "Математика")
    elif call.data == "physics":
        show_options(call, "Физика")
    elif call.data == "informatics":
        show_options(call, "Информатика")
    elif call.data.startswith(("random_", "topic_", "test_")):
        option, subject = call.data.split("_", 1)
        # print(option, subject)
        global next_test
        if option == "random":
            next_test = "random_"
            bot.send_message(
                call.message.chat.id, f"Вы выбрали случайные вопросы по {subject}."
            )
            if subject == "Математика":
                next_test += "math"
                random_math(call)
            elif subject == "Физика":
                next_test += "physics"
                random_physics(call)
            elif subject == "informatics":
                next_test += "informatics"
                random_informatics(call)
        elif option == "topic":
            bot.send_message(
                call.message.chat.id,
                f"Вы выбрали вопросы по определённой теме по {subject}.",
            )
        elif option == "test":
            bot.send_message(call.message.chat.id, f"Вы выбрали тест по {subject}.")
        # print(1235146, call)
    elif call.data.startswith(("answer_")):
        a, b, x = call.data.split("_")
        if b == x:
            bot.send_message(call.message.chat.id, f"Верно!")
            f_next_test(call)
        else:
            bot.send_message(call.message.chat.id, f"Неверно, {x}")


def f_next_test(call):
    # print(1)
    option, subject = next_test.split("_", 1)
    # print(option, subject)
    if option == "random":
        if subject == "math":
            random_math(call)


def show_options(call, subject):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(
        "Случайные вопросы", callback_data=f"random_{subject}"
    )
    btn2 = telebot.types.InlineKeyboardButton(
        "По определённой теме", callback_data=f"topic_{subject}"
    )
    btn3 = telebot.types.InlineKeyboardButton("Тест", callback_data=f"test_{subject}")
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(
        call.message.chat.id,
        f"Вы выбрали {subject}. Выберите вариант:",
        reply_markup=markup,
    )
    # bot.register_next_step_handler(call, handle_option_selection)


def random_math(call):
    math_task = ["math_AB_task", "math_probability_1_test"]
    globals()[random.choice(math_task)](call)


def random_physics(call):
    physics_task = ["physics_mkT_1_task"]
    globals()[random.choice(physics_task)](call)


def random_informatics(call):
    pass


def math_AB_task(call):
    a = random.randint(1, 20) * 5
    b = random.randint(1, 20) * 5
    s = random.randint(45, 80) * 5
    t = random.choice([0.5, 1, 1.5, 2])
    # a, b, s, t = 50, 55, 415, 2
    x = ((s - a * t) / (a + b) + t) * a
    # print(a, b, s, t, x)
    while int(x) != x:
        a = random.randint(1, 20) * 5
        b = random.randint(1, 20) * 5
        s = random.randint(45, 80) * 5
        t = random.choice([0.5, 1, 1.5, 2])
        # a, b, s, t = 50, 55, 415, 2
        x = ((s - a * t) / (a + b) + t) * a
        # print(a, b, s, t, x)
    x1 = random.randint(45, 80) * 5
    x2 = random.randint(45, 80) * 5
    x3 = int(s - x)
    x = int(x)
    an = [x, x1, x2, x3]
    random.shuffle(an)
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(
        str(an[0]), callback_data=f"answer_{an[0]}_{x}"
    )
    btn2 = telebot.types.InlineKeyboardButton(
        str(an[1]), callback_data=f"answer_{an[1]}_{x}"
    )
    btn3 = telebot.types.InlineKeyboardButton(
        str(an[2]), callback_data=f"answer_{an[2]}_{x}"
    )
    btn4 = telebot.types.InlineKeyboardButton(
        str(an[3]), callback_data=f"answer_{an[3]}_{x}"
    )
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(
        call.message.chat.id,
        f"Расстояние между городами A и B равно {s}км. Из города A в город B со скоростью {a}км/ч выехал первый автомобиль,"
        f" а через {t} часа после этого навстречу ему из города B выехал второй автомобиль со скоростью {b}км/ч."
        f" На каком расстоянии от города A автомобили встретятся? Ответ дайте в километрах. Выберите вариант ответа:",
        reply_markup=markup,
    )


def math_probability_1_test(call):
    x = random.randint(1, 40)
    y = random.randint(10, 30)
    z = random.randint(4, 9)
    a, b = y + 1, 0
    for i in range(x, x + y + 1):
        if i % z == 0:
            b += 1
    ans = round(b / a, 2)
    q = round(random.choice([ans - 0.02, ans + 0.02, ans - 0.01, ans + 0.01]), 2)
    w = round(random.randint(10, 30) / 100, 2)
    an = [ans, round(1 - ans, 2), q, w]
    # print(x, y, z, a, b, ans)
    random.shuffle(an)
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(
        str(an[0]), callback_data=f"answer_{an[0]}_{ans}"
    )
    btn2 = telebot.types.InlineKeyboardButton(
        str(an[1]), callback_data=f"answer_{an[1]}_{ans}"
    )
    btn3 = telebot.types.InlineKeyboardButton(
        str(an[2]), callback_data=f"answer_{an[2]}_{ans}"
    )
    btn4 = telebot.types.InlineKeyboardButton(
        str(an[3]), callback_data=f"answer_{an[3]}_{ans}"
    )
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(
        call.message.chat.id,
        f"Из множества натуральных чисел от {x} до {x+y} наудачу выбирают число. Какова вероятность того,"
        f" что это число делится на {z}? Результат округлите до сотых.",
        reply_markup=markup,
    )


def physics_mkT_1_task(call):
    a = random.randint(1, 10) * 50
    b = random.randint(2, 5)
    while (a / (b - 1)) != int(a / (b - 1)):
        a = random.randint(1, 10) * 50
        b = random.randint(2, 5)
    c = int(a / (b - 1))
    x = c + a
    x1 = random.randint(1, 4) * 100 + 50
    x2 = random.randint(1, 4) * 100
    an = [x, c, x1, x2]
    random.shuffle(an)
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(
        str(an[0]), callback_data=f"answer_{an[0]}_{x}"
    )
    btn2 = telebot.types.InlineKeyboardButton(
        str(an[1]), callback_data=f"answer_{an[1]}_{x}"
    )
    btn3 = telebot.types.InlineKeyboardButton(
        str(an[2]), callback_data=f"answer_{an[2]}_{x}"
    )
    btn4 = telebot.types.InlineKeyboardButton(
        str(an[3]), callback_data=f"answer_{an[3]}_{x}"
    )
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(
        call.message.chat.id,
        f"При увеличении абсолютной температуры на {a}K средняя кинетическая энергия теплового движения молекул аргона увеличилось "
        f"аргона увеличилось в {b} раза. Какова конечная температура газа?",
        reply_markup=markup,
    )


def physics_mkT_2_task(call):
    pass


bot.polling(non_stop=True)
