import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from aiogram.client.default import DefaultBotProperties
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram import F
import math

API_TOKEN = "7497399233:AAGf-D1HcQwNA9uWsXJ5RI66S4mik9m0mzk"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
dp = Dispatcher()

next_test = ""


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
        reply_markup=keyboard
    )


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
        f"На каком расстоянии от A они встретятся?", reply_markup=keyboard
    )


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
        f"Чему равна конечная температура газа?", reply_markup=keyboard
    )


async def physics_energy_task(call: CallbackQuery):
    m = random.randint(1, 10) * 10  # Масса в кг
    h = random.randint(2, 10) * 5  # Высота в метрах
    g = 9.81  # Ускорение свободного падения в м/с²
    E_potential = m * g * h  # Потенциальная энергия
    # Кинетическая энергия, случайное значение
    E_kinetic = random.randint(1, 5) * 10
    final_energy = E_potential + E_kinetic  # Общая энергия
    options = [final_energy, E_potential,
               E_kinetic, random.randint(1, 100) * 10]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(final_energy)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(final_energy)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(final_energy)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(final_energy)}")
        ]
    ])
    await call.message.answer(
        f"Тело массой {m} кг поднято на высоту {h} м. "
        f"Если кинетическая энергия тела равна {E_kinetic} Дж, "
        f"какова общая энергия системы (потенциальная + кинетическая)?", reply_markup=keyboard
    )


async def informatics_sorting_task(call: CallbackQuery):
    n = random.randint(5, 15)  # Количество элементов в массиве
    a = random.randint(1, 100)  # Первое значение
    b = random.randint(1, 100)  # Второе значение
    # Генерируем массив случайных чисел
    array = [random.randint(1, 100) for _ in range(n)]
    # Количество операций сортировки методом пузырька
    # В худшем случае это (n*(n-1))/2
    operations = (n * (n - 1)) // 2
    options = [operations, operations - random.randint(1, 10), operations + random.randint(1, 10),
               random.randint(1, 100)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(operations)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(operations)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(operations)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(operations)}")
        ]
    ])

    await call.message.answer(
        f"Дан массив из {n} случайных чисел. "
        f"Сколько операций потребуется для сортировки массива методом пузырька в худшем случае?",
        reply_markup=keyboard
    )


async def memory_storage_task(call: CallbackQuery):
    num_identifiers = 65536  # Количество идентификаторов
    num_digits = 10  # Количество десятичных цифр
    num_special_chars = 400  # Количество специальных символов
    total_symbols = num_digits + num_special_chars  # Общее количество символов
    # Вычисляем минимальное количество бит для кодирования одного символа
    # Количество бит для представления всех символов
    bits_per_symbol = (total_symbols).bit_length()
    # Объем памяти в байтах для одного идентификатора
    # Округляем вверх до байта
    bytes_per_identifier = (321 * bits_per_symbol + 7) // 8
    # Общий объем памяти для всех идентификаторов
    total_memory_bytes = num_identifiers * bytes_per_identifier
    # Переводим в Кбайты
    total_memory_kb = total_memory_bytes // 1024
    # Генерируем варианты ответов
    options = [total_memory_kb, total_memory_kb + random.randint(1, 10),
               total_memory_kb - random.randint(1, 10), random.randint(1, 100)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(total_memory_kb)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(total_memory_kb)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(total_memory_kb)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(total_memory_kb)}")
        ]
    ])
    await call.message.answer(
        f"При регистрации в компьютерной системе каждому объекту присваивается идентификатор, "
        f"состоящий из 321 символа и содержащий только десятичные цифры и символы из 400-символьного специального алфавита. "
        f"Определите объем памяти (в Кбайт), необходимый для хранения {num_identifiers} идентификаторов.",
        reply_markup=keyboard
    )


async def impulse_calculation_task(call: CallbackQuery):
    # Данные задачи
    force = 10  # Сила в Н
    initial_impulse = 10  # Начальный импульс в кг·м/с
    time = 4  # Время в секундах
    # Вычисляем изменение импульса
    # Изменение импульса = сила * время
    change_in_impulse = force * time
    # Импульс тела через заданное время
    final_impulse = initial_impulse + change_in_impulse
    # Генерируем варианты ответов
    options = [final_impulse, final_impulse + random.randint(1, 5),
               final_impulse - random.randint(1, 5), random.randint(5, 50)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(final_impulse)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(final_impulse)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(final_impulse)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(final_impulse)}")
        ]
    ])
    await call.message.answer(
        f"Тело движется по прямой в инерциальной системе отсчёта под действием постоянной силы величиной {force} Н, "
        f"направленной в сторону движения тела. Начальный импульс тела равен {initial_impulse} кг·м/с. "
        f"Определите импульс тела через {time} с.",
        reply_markup=keyboard
    )


async def harmonic_oscillator_task(call: CallbackQuery):
    # Данные задачи
    initial_period = 2  # Начальный период в секундах
    mass_increase_factor = 4  # Увеличение массы в 4 раза
    # Вычисляем новый период
    new_period = initial_period * math.sqrt(mass_increase_factor)
    # Генерируем варианты ответов
    options = [new_period, new_period + random.uniform(0.1, 1.0),
               new_period - random.uniform(0.1, 1.0), random.uniform(3, 5)]
    # Округляем до двух знаков после запятой
    options = [round(option, 2) for option in options]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(new_period)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(new_period)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(new_period)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(new_period)}")
        ]
    ])
    await call.message.answer(
        f"Период свободных гармонических колебаний пружинного маятника равен {initial_period} с. "
        f"Какой будет период свободных колебаний этого маятника, если массу груза увеличить в {mass_increase_factor} раза?",
        reply_markup=keyboard
    )


async def audio_file_size_task(call: CallbackQuery):
    # Данные задачи
    original_size_mb = 48  # Размер оригинального файла в Мбайт
    original_channels = 1  # Моно (1 канал)
    new_channels = 2  # Стерео (2 канала)
    resolution_factor = 1 / 3  # Разрешение в 3 раза ниже
    sample_rate_factor = 2  # Частота дискретизации в 2 раза выше
    # Вычисляем новый размер файла
    # Новый размер = оригинальный размер * (новое количество каналов / старое количество каналов) * (старое разрешение / новое разрешение) * (новая частота / старая частота)
    new_size_mb = original_size_mb * (new_channels / original_channels) * (
        1 / resolution_factor) * sample_rate_factor
    # Генерируем варианты ответов
    options = [int(new_size_mb), int(new_size_mb + random.uniform(1, 10)),
               int(new_size_mb - random.uniform(1, 10)), random.randint(40, 100)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(int(new_size_mb))}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(int(new_size_mb))}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(int(new_size_mb))}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(int(new_size_mb))}")
        ]
    ])
    await call.message.answer(
        f"Музыкальный фрагмент был записан в формате моно и имеет размер {original_size_mb} Мбайт. "
        f"Затем его записали в формате стерео с разрешением в 3 раза ниже и частотой дискретизации в 2 раза выше. "
        f"Какой размер полученного файла в Мбайт? В ответе укажите только целое число.",
        reply_markup=keyboard
    )


async def network_address_task(call: CallbackQuery):
    # Данные задачи
    subnet_mask = "255.255.255.224"  # Маска сети
    # Преобразуем маску в двоичный формат
    binary_mask = '11111111.11111111.11111111.11111100'  # 255.255.255.224
    # Считаем количество единиц в маске
    num_ones = binary_mask.count('1')
    # Количество адресов в подсети = 2^(32 - количество единиц) - 2 (адрес сети и широковещательный)
    num_addresses = (2 ** (32 - num_ones)) - 2
    # Генерируем варианты ответов
    options = [num_addresses, num_addresses + random.randint(1, 10),
               num_addresses - random.randint(1, 10), random.randint(10, 50)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{str(options[0])}_{str(num_addresses)}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{str(options[1])}_{str(num_addresses)}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{str(options[2])}_{str(num_addresses)}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{str(options[3])}_{str(num_addresses)}")
        ]
    ])
    await call.message.answer(
        f"Для подсети с маской сети {subnet_mask} сколько различных адресов компьютеров теоретически допускает эта маска, "
        f"если два адреса (адрес сети и широковещательный) не используются?",
        reply_markup=keyboard
    )


async def football_probability_task(call: CallbackQuery):
    # Данные задачи
    team_a = "A"
    team_b = "B"
    team_c = "C"
    # Вероятность того, что команда A будет первой владеть мячом
    probability_first = 0.5  # 50% вероятность, так как монета бросается
    # Вероятность того, что команда A будет первой владеть мячом в обоих матчах
    probability_both_matches = probability_first * probability_first
    # Генерируем варианты ответов
    options = [round(probability_both_matches, 2),
               round(probability_both_matches + random.uniform(0.1, 0.5), 2),
               round(probability_both_matches - random.uniform(0.1, 0.5), 2),
               round(random.uniform(0.0, 1.0), 2)]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]),
                callback_data=f"answer_{str(options[0])}_{str(round(probability_both_matches, 2))}"),
            InlineKeyboardButton(
                text=str(options[1]),
                callback_data=f"answer_{str(options[1])}_{str(round(probability_both_matches, 2))}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]),
                callback_data=f"answer_{str(options[2])}_{str(round(probability_both_matches, 2))}"),
            InlineKeyboardButton(
                text=str(options[3]),
                callback_data=f"answer_{str(options[3])}_{str(round(probability_both_matches, 2))}")
        ]
    ])
    await call.message.answer(
        f"Команда {team_a} должна сыграть с командой {team_b} и с командой {team_c} по одному разу. "
        f"Какова вероятность того, что команда {team_a} будет первой владеть мячом в обоих матчах?",
        reply_markup=keyboard
    )


async def generate_cone_pyramid_task(call: CallbackQuery):
    # Генерация случайного объема конуса
    # Объем конуса в диапазоне от 100 до 200 * π
    volume_cone = random.uniform(100, 200)
    # Высота конуса в диапазоне от 7 до 15
    height_cone = random.randint(7, 15)
    # Вычисление радиуса основания конуса
    radius_cone = (3 * volume_cone) / height_cone
    # Извлечение кубического корня для получения радиуса
    radius_cone = radius_cone ** (1/3)
    # Вычисление стороны квадрата основания пирамиды
    side_square = radius_cone * (2 ** 0.5)
    # Вычисление объема пирамиды
    area_base = side_square ** 2
    volume_pyramid = (1/3) * area_base * height_cone
    # Форматирование задачи
    correct_answer = round(volume_pyramid)
    options = [correct_answer, random.randint(
        1, 4) * 100, random.randint(1, 4) * 50 + 50, random.randint(1, 4) * 150]
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=str(options[0]), callback_data=f"answer_{options[0]}_{correct_answer}"),
            InlineKeyboardButton(
                text=str(options[1]), callback_data=f"answer_{options[1]}_{correct_answer}")
        ],
        [
            InlineKeyboardButton(
                text=str(options[2]), callback_data=f"answer_{options[2]}_{correct_answer}"),
            InlineKeyboardButton(
                text=str(options[3]), callback_data=f"answer_{options[3]}_{correct_answer}")
        ]
    ])
    await call.message.answer(
        f"В круговой конус вписана правильная четырехугольная пирамида.\n"
        f"Объем конуса равен {volume_cone:.2f}π, а высота равна {height_cone}.\n"
        f"Каков объем вписанной пирамиды?", reply_markup=keyboard
    )


async def informatics_task(call: CallbackQuery):
    await call.message.answer("Пока нет задач по информатике.")


async def random_math(call: CallbackQuery):
    tasks = [math_AB_task, math_probability_1_test,
             football_probability_task, generate_cone_pyramid_task]
    await random.choice(tasks)(call)


async def random_physics(call: CallbackQuery):
    tasks = [physics_energy_task, physics_mkT_1_task,
             impulse_calculation_task, harmonic_oscillator_task]
    await random.choice(tasks)(call)
    # await call.message.answer("Задачи по физике будут добавлены позже.")


async def random_informatics(call: CallbackQuery):
    tasks = [informatics_sorting_task, memory_storage_task,
             audio_file_size_task, network_address_task]
    await random.choice(tasks)(call)
    # await call.message.answer("Задачи по информатике будут добавлены позже.")


@dp.message(Command('start'))
async def start_handler(message: Message):
    username = message.from_user.full_name or message.from_user.username
    welcome_text = (
        f"👋 Привет, <b>{username}</b>!\n\n"
        "Я — бот для тренировки знаний.\n\n"
        "🎯 Выберите уровень сложности для начала тренировки.\n\n"
        "💡 Вы можете выбрать между лёгким, средним и сложным уровнем.\n"
        "Если хотите тренироваться по предметам, используйте соответствующие кнопки ниже.\n\n"
    )
    keyboard = ReplyKeyboardMarkup(
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
    await message.answer(welcome_text, reply_markup=keyboard)


@dp.message(F.text == "🎯 Выбрать сложность")
async def choose_difficulty_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🟢 Лёгкая"), KeyboardButton(
                text="🟡 Средняя"), KeyboardButton(text="🔴 Сложная")],
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True
    )
    await message.answer("🎯 Выберите уровень сложности:", reply_markup=keyboard)


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
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 Профиль"), KeyboardButton(
                text="🎯 Выбрать сложность")],
            [KeyboardButton(text="🏋️ Тренировка"),
             KeyboardButton(text="📚 Учебники")],
            [KeyboardButton(text="📈 Статистика"),
             KeyboardButton(text="⚙️ Настройки")]
        ],
        resize_keyboard=True
    )
    await message.answer("🔙 Вернулись в главное меню:", reply_markup=keyboard)


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
    await message.answer(f"👤 Ваш профиль:\n\n<b>Имя:</b> {message.from_user.full_name}\n<b>ID:</b> {message.from_user.id}")


@dp.message(F.text == "📚 Учебники")
async def textbooks_handler(message: Message):
    await message.answer("📚 Список доступных учебников:\n\n1. Математика: Алгебра и Геометрия\n2. Физика: Механика, Термодинамика\n3. Информатика: Основы программирования")


@dp.message(F.text == "📈 Статистика")
async def statistics_handler(message: Message):
    await message.answer("📈 Ваша статистика:\n\n✅ Верных ответов: 0\n❌ Неверных ответов: 0\n📚 Пройдено тестов: 0")


@dp.message(F.text == "⚙️ Настройки")
async def settings_handler(message: Message):
    await message.answer("⚙️ В разработке...")


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

    # keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #     [
    #         InlineKeyboardButton(text=str(options[0]), callback_data=f"answer_{options[0]}_{correct_answer}"),
    #         InlineKeyboardButton(text=str(options[1]), callback_data=f"answer_{options[1]}_{correct_answer}")
    #     ],
    #     [
    #         InlineKeyboardButton(text=str(options[2]), callback_data=f"answer_{options[2]}_{correct_answer}"),
    #         InlineKeyboardButton(text=str(options[3]), callback_data=f"answer_{options[3]}_{correct_answer}")
    #     ]
    # ])
    # await call.message.answer(
    #     f"В круговой конус вписана правильная четырехугольная пирамида.\n"
    #     f"Объем конуса равен {volume_cone:.2f}π, а высота равна {height_cone}.\n"
    #     f"Каков объем вписанной пирамиды?", reply_markup=keyboard

# @dp.callback_query(F.data == "math_tasks")
# async def math_tasks_handler(call: CallbackQuery):
#     await random_math(call)
#
#
# @dp.callback_query(F.data == "physics_tasks")
# async def physics_tasks_handler(call: CallbackQuery):
#     await random_physics(call)
#
#
# @dp.callback_query(F.data == "informatics_tasks")
# async def informatics_tasks_handler(call: CallbackQuery):
#     await random_informatics(call)


@dp.callback_query(F.data.startswith('answer'))
async def check_answer(call: CallbackQuery):
    answer = call.data.split("_")[1]
    correct_answer = call.data.split("_")[2]
    if answer == correct_answer:
        await call.answer("✅ Правильно!")
    else:
        await call.answer("❌ Неправильно!")
    await call.message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
