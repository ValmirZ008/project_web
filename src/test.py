from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from aiogram.client.default import DefaultBotProperties
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram import F
from utils import get_main_menu_keyboard, get_difficulty_keyboard
from db import init_db, update_stats, get_stats, add_user
from deepseek_tester import deepseek_tester_main
from zadachi import *


API_TOKEN = "7287039940:AAEQj66VgJUwDxxkxJtDwhyhwOeIABOutwY"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
dp = Dispatcher()

next_test = ""
user_stats = {}


@dp.message(Command('question'))
async def ask_and_handle_question(msg: types.Message):
    question = "Сколько будет 2 + 2?"
    await msg.answer(question)

    @dp.message(lambda message: True)
    async def handle_answer(answer_msg: types.Message):
        correct_answer = "4"
        user_answer = answer_msg.text.strip()

        if user_answer == correct_answer:
            await answer_msg.answer("Правильно! Молодец!")
        else:
            await answer_msg.answer("Неправильно, попробуй еще раз.")

        # Удаляем обработчик, чтобы не дублировать ответы
        dp.message.unregister(handle_answer)


async def neiro_question_math(
    call: CallbackQuery): await neiro_question(call, 'math')


async def neiro_question_inf(
    call: CallbackQuery): await neiro_question(call, 'inf')


async def neiro_question_physics(
    call: CallbackQuery): await neiro_question(call, 'physics')


async def neiro_question(call: CallbackQuery, lesson):
    global answer
    answer, question = deepseek_tester_main('math')
    # question = "Сколько будет 2 + 2?"
    await call.message.answer(question)

    @dp.message(lambda message: True)
    async def handle_answer(answer_msg: types.Message):
        correct_answer = answer
        user_answer = answer_msg.text.strip()
        if user_answer == correct_answer:
            await answer_msg.answer("Правильно! Молодец!")
        else:
            await answer_msg.answer("Неправильно, попробуй еще раз.")
        if lesson == 'math':
            await random_math(call)
        elif lesson == 'inf':
            await random_informatics(call)
        else:
            await random_physics(call)
        # await call.message.answer(reply_markup=get_main_menu_keyboard())
        # dp.message.unregister(handle_answer)


async def random_math(call: CallbackQuery):
    tasks = [math_AB_task, math_probability_1_test,
             football_probability_task, math_percentage_task, math_speed_task, generate_cone_pyramid_task, math_probability_task, neiro_question_math]
    await random.choice(tasks)(call)


async def random_physics(call: CallbackQuery):
    tasks = [physics_energy_task, physics_mkT_1_task,
             impulse_calculation_task, physics_energy_task, physics_force_task, harmonic_oscillator_task, physics_ohms_task, neiro_question_inf]
    await random.choice(tasks)(call)


async def random_informatics(call: CallbackQuery):
    tasks = [informatics_sorting_task, memory_storage_task,
             audio_file_size_task, network_address_task, informatics_encoding_task, informatics_conversion_task, informatics_bits_task, neiro_question_physics]
    await random.choice(tasks)(call)


@dp.message(Command('start'))
async def start_handler(message: Message):
    username = message.from_user.full_name or message.from_user.username
    add_user(message.from_user.id, username)
    welcome_text = (
        f"👋 Привет, <b>{username}</b>!\n\n"
        "Я — бот для тренировки знаний.\n\n"
        "🎯 Выберите уровень сложности для начала тренировки.\n\n"
        "💡 Вы можете выбрать между лёгким, средним и сложным уровнем.\n"
        "Если хотите тренироваться по предметам, используйте соответствующие кнопки ниже.\n\n"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu_keyboard())


@dp.message(F.text == "🎯 Выбрать сложность")
async def choose_difficulty_handler(message: Message):
    await message.answer("🎯 Выберите уровень сложности:", reply_markup=get_difficulty_keyboard())


task_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔁 Новая задача")],
        [KeyboardButton(text="⬅️ В главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)


@dp.message(F.text == "🟢 Лёгкая")
async def easy_difficulty_handler(message: Message):
    await message.answer("🎯 Вы выбрали <b>Лёгкий</b> уровень сложности. Начнем с простых вопросов!")


@dp.message(F.text == "🟡 Средняя")
async def medium_difficulty_handler(message: Message):
    await message.answer("🎯 Вы выбрали <b>Средний</b> уровень сложности. Время для более сложных задач!")


@dp.message(F.text == "🔴 Сложная")
async def hard_difficulty_handler(message: Message):
    await message.answer("🎯 Вы выбрали <b>Сложный</b> уровень сложности. Готовьтесь к самым трудным вопросам!")


@dp.message(F.text == "⬅️ Назад")
async def back_to_main_menu(message: Message):
    await message.answer("🔙 Вернулись в главное меню:", reply_markup=get_main_menu_keyboard())


@dp.message(F.text == "⬅️ В главное меню")
async def handle_back_to_main_menu(message: Message):
    await back_to_main_menu(message)


@dp.message(F.text == "🔁 Новая задача")
async def handle_new_task(message: Message):
    await message.answer("🔄 Отправьте, по какому предмету вы хотите новую задачу.")


@dp.callback_query(F.data == "math_tasks")
async def math_tasks_handler(call: CallbackQuery):
    await random_math(call)


@dp.callback_query(F.data == "physics_tasks")
async def physics_tasks_handler(call: CallbackQuery):
    await random_physics(call)


@dp.callback_query(F.data == "informatics_tasks")
async def informatics_tasks_handler(call: CallbackQuery):
    await random_informatics(call)


@dp.message(F.text == "👤 Профиль")
async def profile_handler(message: Message):
    correct, incorrect, total = get_stats(message.from_user.id)

    await message.answer(
        f"👤 <b>Ваш профиль</b>\n\n"
        f"<b>Имя:</b> {message.from_user.full_name}\n"
        f"<b>ID:</b> <code>{message.from_user.id}</code>\n\n"
        f"📈 <b>Статистика:</b>\n"
        f"✅ Верных ответов: <b>{correct}</b>\n"
        f"❌ Неверных ответов: <b>{incorrect}</b>\n"
        f"📚 Пройдено тестов: <b>{total}</b>",
        parse_mode="HTML"
    )


@dp.message(F.text == "📚 Учебники")
async def textbooks_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по математике ЕГЭ",
                    url="https://drive.google.com/file/d/1wYreA8-fIBSDDhffaJcv5HXWnNclV-V8/view?usp=sharing"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по математике ОГЭ",
                    url="https://drive.google.com/file/d/15CTNzSau5Z698vccah3q8f_3iYOxMpHR/view?usp=sharing"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по физике ЕГЭ",
                    url="https://drive.google.com/file/d/1hdPqXI9k_ScP5lYyVS5lMaJSWgxyoi9C/view?usp=sharing"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по физике ОГЭ",
                    url="https://drive.google.com/file/d/1P72i6Lx3YBFLL3rHDznjL3PZS8obM9I9/view?usp=sharing"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по информатике ЕГЭ",
                    url="https://drive.google.com/file/d/1dZpJB7mXbHcMPdJmQ3AT9Q2TjyeZk7l3/view?usp=sharing"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 Скачать учебник по информатике ОГЭ",
                    url="https://drive.google.com/file/d/1PwWKOL8lf9un9Yio6ZuT2GsVwwlzrexI/view?usp=sharing"
                )
            ]
        ]
    )

    await message.answer(
        "Выберите учебник для скачивания:",
        reply_markup=keyboard
    )


@dp.message(F.text == "🏋️ Тренировка")
async def training_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Математика\n", callback_data="math_tasks"),
             InlineKeyboardButton(text="Физика\n", callback_data="physics_tasks")],
            [InlineKeyboardButton(text="Информатика\n",
                                  callback_data="informatics_tasks")]
        ]
    )
    await message.answer("🏋️ Выберите предмет для тренировки:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("choose_difficulty_"))
async def difficulty_chosen(call: CallbackQuery):
    _, subject, difficulty = call.data.split("_")
    await call.message.answer(f"🎯 Вы выбрали <b>{difficulty.capitalize()}</b> уровень по предмету <b>{subject.capitalize()}</b>.")
    await run_random_task(call, subject, difficulty)


@dp.callback_query(F.data.startswith('answer'))
async def check_answer(call: CallbackQuery):
    parts = call.data.split("_")
    answer = parts[1]
    correct_answer = parts[2]
    subject = parts[3] if len(parts) > 3 else None
    if answer == correct_answer:
        await call.answer("✅ Правильно!")
        update_stats(call.from_user.id, subject=subject, is_correct=True)
    else:
        await call.answer("❌ Неправильно!")
        update_stats(call.from_user.id, subject=subject, is_correct=False)
    await call.message.delete()
    next_msg = await call.message.answer("🧠 Следующая задача:")
    await asyncio.sleep(0.5)
    await next_msg.delete()

    # Пока закоментил, до этого не удалялось сообщение
    # await call.message.answer("Выберите действие:", reply_markup=get_task_reply_keyboard())
    if subject == "math":
        await random_math(call)
    elif subject == "physics":
        await random_physics(call)
    elif subject == "info":
        await random_informatics(call)


async def main():
    init_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
