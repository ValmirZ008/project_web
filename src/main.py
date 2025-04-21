import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = "7497399233:AAGf-D1HcQwNA9uWsXJ5RI66S4mik9m0mzk"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
dp = Dispatcher()

next_test = ""


@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Математика", callback_data="математика")],
        [InlineKeyboardButton(text="Физика", callback_data="физика")],
        [InlineKeyboardButton(text="Информатика", callback_data="информатика")]
    ])
    await message.answer("Какой предмет вы хотите потренировать?", reply_markup=keyboard)


@dp.callback_query(F.data.in_({"математика", "физика", "информатика"}))
async def handle_subject_selection(call: CallbackQuery):
    subject = call.data
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Случайные вопросы",
                              callback_data=f"random_{subject}")],
        [InlineKeyboardButton(
            text="По теме", callback_data=f"topic_{subject}")],
        [InlineKeyboardButton(text="Тест", callback_data=f"test_{subject}")]
    ])
    await call.message.answer(f"Вы выбрали {subject.title()}. Выберите вариант:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("random_"))
async def handle_random(call: CallbackQuery):
    global next_test
    subject = call.data.split("_", 1)[1]
    next_test = call.data
    await call.message.answer(f"Вы выбрали случайные вопросы по {subject}.")

    if subject == "математика":
        await random_math(call)
    elif subject == "физика":
        await random_physics(call)
    elif subject == "информатика":
        await call.message.answer("Пока нет задач по информатике.")


@dp.callback_query(F.data.startswith("answer_"))
async def check_answer(call: CallbackQuery):
    _, chosen, correct = call.data.split("_")
    if chosen == correct:
        await call.message.answer("✅ Верно!")
        await f_next_test(call)
    else:
        await call.message.answer(f"❌ Неверно. Правильный ответ: {correct}")


async def f_next_test(call: CallbackQuery):
    option, subject = next_test.split("_", 1)
    if option == "random":
        if subject == "математика":
            await random_math(call)
        elif subject == "физика":
            await random_physics(call)


async def random_math(call: CallbackQuery):
    tasks = [math_AB_task, math_probability_1_test]
    await random.choice(tasks)(call)


async def random_physics(call: CallbackQuery):
    tasks = [physics_mkT_1_task]
    await random.choice(tasks)(call)


async def math_AB_task(call: CallbackQuery):
    while True:
        a = random.randint(1, 20) * 5
        b = random.randint(1, 20) * 5
        s = random.randint(45, 80) * 5
        t = random.choice([0.5, 1, 1.5, 2])
        x = ((s - a * t) / (a + b) + t) * a
        if x.is_integer():
            break
    x = int(x)
    options = [x, random.randint(
        45, 80) * 5, int(s - x), random.randint(45, 80) * 5]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(x)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(x)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(x)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(x)}")
        ]
    ])
    await call.message.answer(
        f"Расстояние между городами A и B — {s} км. Из A в B со скоростью {a} км/ч выехал автомобиль. "
        f"{t} часа спустя навстречу из B со скоростью {b} км/ч — второй. "
        f"На каком расстоянии от A они встретятся?", reply_markup=keyboard)


async def math_probability_1_test(call: CallbackQuery):
    x = random.randint(1, 40)
    y = random.randint(10, 30)
    z = random.randint(4, 9)
    total = y + 1
    count = sum(1 for i in range(x, x + y + 1) if i % z == 0)
    ans = round(count / total, 2)
    distractors = [
        round(ans + 0.01, 2),
        round(ans - 0.01, 2),
        round(random.uniform(0.1, 0.5), 2),
        round(1 - ans, 2)
    ]
    options = list(set([ans] + distractors))[:4]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(ans)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(ans)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(ans)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(ans)}")
        ]
    ])
    await call.message.answer(
        f"Из натуральных чисел от {x} до {x + y} случайно выбирается число. "
        f"Какова вероятность, что оно делится на {z}? Округлите до сотых.",
        reply_markup=keyboard)


async def physics_mkT_1_task(call: CallbackQuery):
    while True:
        a = random.randint(1, 10) * 50
        b = random.randint(2, 5)
        if (a / (b - 1)).is_integer():
            break
    c = int(a / (b - 1))
    x = c + a
    options = [x, c, random.randint(
        1, 4) * 100 + 50, random.randint(1, 4) * 100]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(x)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(x)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(x)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(x)}")
        ]
    ])
    await call.message.answer(
        f"Температура увеличилась на {a} K, и средняя кинетическая энергия молекул аргона увеличилась в {b} раза. "
        f"Чему равна конечная температура газа?", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
