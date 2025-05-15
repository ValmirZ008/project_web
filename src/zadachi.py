import random
from aiogram.types import CallbackQuery
from aiogram import F
import math
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_options_keyboard(options, correct_answer, subject):
    random.shuffle(options)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    row = []
    for i, option in enumerate(options):
        cb_data = f"answer_{option}_{correct_answer}_{subject}"
        button = InlineKeyboardButton(text=str(option), callback_data=cb_data)
        row.append(button)
        if len(row) == 2:
            keyboard.inline_keyboard.append(row)
            row = []
    if row:
        keyboard.inline_keyboard.append(row)
    return keyboard


async def math_probability_1_test(call: CallbackQuery):
    x = random.randint(1, 40)
    y = random.randint(10, 30)
    z = random.randint(4, 9)
    total = y + 1
    count = sum(1 for i in range(x, x + y + 1) if i % z == 0)
    ans = round(count / total, 2)
    distractors = [
        ans,
        round(ans - 0.02, 2),
        round(random.uniform(0.1, 0.5), 2),
        round(1 - ans, 2)
    ]
    options = list(set([ans] + distractors))[:4]
    random.shuffle(options)
    correct_answer = ans
    keyboard = create_options_keyboard(options, correct_answer, "math")
    await call.message.answer(
        f"Из натуральных чисел от {x} до {x + y} случайно выбирается число. "
        f"Какова вероятность, что оно делится на {z}? Округлите до сотых.",
        reply_markup=keyboard
    )


async def math_probability_task(call: CallbackQuery):
    start = random.randint(1, 20)
    end = start + random.randint(10, 30)
    total = end - start + 1
    even_count = sum(1 for i in range(start, end + 1) if i % 2 == 0)
    probability = round(even_count / total, 2)

    options = list(set([
        probability,
        round(probability + 0.1, 2),
        round(probability - 0.1, 2),
        round(random.uniform(0.1, 0.9), 2)
    ]))
    random.shuffle(options)

    correct_answer = probability
    keyboard = create_options_keyboard(options, correct_answer, "math")

    await call.message.answer(
        f"Из натуральных чисел от {start} до {end} случайно выбирается одно число.\n"
        f"Какова вероятность, что оно чётное? Округлите до сотых.",
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
    correct_answer = x
    keyboard = create_options_keyboard(options, correct_answer, "math")
    await call.message.answer(
        f"Расстояние между городами A и B — {s} км. Из A в B со скоростью {a} км/ч выехал автомобиль. "
        f"{t} часа спустя навстречу из B со скоростью {b} км/ч — второй. "
        f"На каком расстоянии от A они встретятся?", reply_markup=keyboard
    )


async def math_percentage_task(call: CallbackQuery):
    final_price = random.randint(800, 1200)
    discount = 0.2
    original_price = round(final_price / (1 - discount))
    options = [original_price, original_price + 100,
               original_price - 100, random.randint(1000, 2000)]
    random.shuffle(options)
    keyboard = create_options_keyboard(options, original_price, "math")
    await call.message.answer(
        f"После скидки в 20% цена товара составляет {final_price} рублей. \n"
        f"Какова была первоначальная цена товара?",
        reply_markup=keyboard
    )


async def math_speed_task(call: CallbackQuery):
    v1 = 60
    t1 = 2
    v2 = 90
    t2 = 1
    s1 = v1 * t1
    s2 = v2 * t2
    v_avg = round((s1 + s2) / (t1 + t2))
    options = [v_avg, v_avg + 10, v_avg - 10, random.randint(40, 100)]
    random.shuffle(options)
    keyboard = create_options_keyboard(options, v_avg, "math")
    await call.message.answer(
        f"Автомобиль ехал {t1} часа со скоростью {v1} км/ч и {t2} час — со скоростью {v2} км/ч.\n"
        f"Найдите среднюю скорость движения.", reply_markup=keyboard
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
    correct_answer = x
    keyboard = create_options_keyboard(options, correct_answer, "physics")
    await call.message.answer(
        f"Температура увеличилась на {a} K, и средняя кинетическая энергия молекул аргона увеличилась в {b} раза. "
        f"Чему равна конечная температура газа?", reply_markup=keyboard
    )


async def physics_energy_task(call: CallbackQuery):
    m = random.randint(1, 10) * 10  # Масса в кг
    h = random.randint(2, 10) * 5  # Высота в метрах
    g = 9.81  # Ускорение свободного падения в м/с²
    E_potential = m * g * h  # Потенциальная энергия
    E_kinetic = random.randint(1, 5) * 10
    final_energy = E_potential + E_kinetic  # Общая энергия
    options = [final_energy, E_potential,
               E_kinetic, random.randint(1, 100) * 10]
    random.shuffle(options)
    correct_answer = final_energy
    keyboard = create_options_keyboard(options, correct_answer, "physics")
    await call.message.answer(
        f"Тело массой {m} кг поднято на высоту {h} м. "
        f"Если кинетическая энергия тела равна {E_kinetic} Дж, "
        f"какова общая энергия системы (потенциальная + кинетическая)?", reply_markup=keyboard
    )


async def physics_ohms_task(call: CallbackQuery):
    voltage = random.randint(5, 20)
    resistance = random.randint(1, 10)
    current = round(voltage / resistance, 2)

    options = list(set([
        current,
        round(current + 0.5, 2),
        round(current - 0.5, 2),
        round(random.uniform(0.5, 3.0), 2)
    ]))
    random.shuffle(options)

    correct_answer = current
    keyboard = create_options_keyboard(options, correct_answer, "physics")

    await call.message.answer(
        f"На резистор сопротивлением {resistance} Ом подано напряжение {voltage} В.\n"
        f"Какова сила тока в цепи? Ответ в амперах, округлите до сотых.",
        reply_markup=keyboard
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
    correct_answer = operations
    keyboard = create_options_keyboard(options, correct_answer, "info")

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
    bits_per_symbol = (total_symbols).bit_length()
    bytes_per_identifier = (321 * bits_per_symbol + 7) // 8
    total_memory_bytes = num_identifiers * bytes_per_identifier
    total_memory_kb = total_memory_bytes // 1024
    options = [total_memory_kb, total_memory_kb + random.randint(1, 10),
               total_memory_kb - random.randint(1, 10), random.randint(1, 100)]
    random.shuffle(options)
    correct_answer = total_memory_kb
    keyboard = create_options_keyboard(options, correct_answer, "info")
    await call.message.answer(
        f"При регистрации в компьютерной системе каждому объекту присваивается идентификатор, "
        f"состоящий из 321 символа и содержащий только десятичные цифры и символы из 400-символьного специального алфавита. "
        f"Определите объем памяти (в Кбайт), необходимый для хранения {num_identifiers} идентификаторов.",
        reply_markup=keyboard
    )


async def impulse_calculation_task(call: CallbackQuery):
    force = 10  # Сила в Н
    initial_impulse = 10  # Начальный импульс в кг·м/с
    time = 4  # Время в секундах
    change_in_impulse = force * time
    final_impulse = initial_impulse + change_in_impulse
    options = [final_impulse, final_impulse + random.randint(1, 5),
               final_impulse - random.randint(1, 5), random.randint(5, 50)]
    random.shuffle(options)
    correct_answer = final_impulse
    keyboard = create_options_keyboard(options, correct_answer, "physics")
    await call.message.answer(
        f"Тело движется по прямой в инерциальной системе отсчёта под действием постоянной силы величиной {force} Н, "
        f"направленной в сторону движения тела. Начальный импульс тела равен {initial_impulse} кг·м/с. "
        f"Определите импульс тела через {time} с.",
        reply_markup=keyboard
    )


async def harmonic_oscillator_task(call: CallbackQuery):
    initial_period = 2  # Начальный период в секундах
    mass_increase_factor = 4  # Увеличение массы в 4 раза
    new_period = initial_period * math.sqrt(mass_increase_factor)
    options = [new_period, new_period + random.uniform(0.1, 1.0),
               new_period - random.uniform(0.1, 1.0), random.uniform(3, 5)]
    options = [round(option, 2) for option in options]
    random.shuffle(options)
    correct_answer = new_period
    keyboard = create_options_keyboard(options, correct_answer, "physics")
    await call.message.answer(
        f"Период свободных гармонических колебаний пружинного маятника равен {initial_period} с. "
        f"Какой будет период свободных колебаний этого маятника, если массу груза увеличить в {mass_increase_factor} раза?",
        reply_markup=keyboard
    )


async def physics_force_task(call: CallbackQuery):
    mass = random.randint(1, 5)
    acceleration = random.randint(2, 6)
    force = mass * acceleration
    options = [force, force + 2, force - 2, random.randint(1, 30)]
    random.shuffle(options)
    keyboard = create_options_keyboard(options, force, "physics")
    await call.message.answer(
        f"Тело массой {mass} кг движется с ускорением {acceleration} м/с².\n"
        f"Найдите силу, действующую на тело.", reply_markup=keyboard
    )


async def physics_energy_task(call: CallbackQuery):
    mass = random.randint(2, 6)
    velocity = random.randint(2, 6)
    energy = int((mass * velocity ** 2) / 2)
    options = [energy, energy + 5, energy - 5, random.randint(10, 100)]
    random.shuffle(options)
    keyboard = create_options_keyboard(options, energy, "physics")
    await call.message.answer(
        f"Масса тела — {mass} кг, скорость — {velocity} м/с.\n"
        f"Найдите его кинетическую энергию.", reply_markup=keyboard
    )


async def audio_file_size_task(call: CallbackQuery):
    while True:
        original_size_mb = random.randint(30, 80)
        original_channels = 1  # Моно (1 канал)
        new_channels = 2  # Стерео (2 канала)
        # Разрешение в 3 раза ниже
        resolution_factor = 1 / random.randint(2, 6)
        # Частота дискретизации в 2 раза выше
        sample_rate_factor = random.randint(2, 6)
        # Новый размер = оригинальный размер * (новое количество каналов / старое количество каналов) * (старое разрешение / новое разрешение) * (новая частота / старая частота)
        new_size_mb = original_size_mb * (new_channels / original_channels) * (
            1 / resolution_factor) * sample_rate_factor
        if new_size_mb == int(new_size_mb):
            break
    # Генерируем варианты ответов
    options = [int(new_size_mb), int(new_size_mb + random.uniform(1, 10)),
               int(new_size_mb - random.uniform(1, 10)), random.randint(40, 100)]
    random.shuffle(options)
    correct_answer = int(new_size_mb)
    keyboard = create_options_keyboard(options, correct_answer, "info")
    await call.message.answer(
        f"Музыкальный фрагмент был записан в формате моно и имеет размер {original_size_mb} Мбайт. "
        f"Затем его записали в формате стерео с разрешением в 3 раза ниже и частотой дискретизации в 2 раза выше. "
        f"Какой размер полученного файла в Мбайт? В ответе укажите только целое число.",
        reply_markup=keyboard
    )


async def network_address_task(call: CallbackQuery):
    subnet_mask = "255.255.255.224"
    binary_mask = '11111111.11111111.11111111.11111100'
    num_ones = binary_mask.count('1')
    num_addresses = (2 ** (32 - num_ones)) - 2
    correct_answer = str(num_addresses)

    distractors = set()
    while len(distractors) < 3:
        delta = random.randint(1, 10)
        candidate = num_addresses + random.choice([-1, 1]) * delta
        if candidate > 0 and candidate != num_addresses:
            distractors.add(candidate)
    options = list(distractors) + [num_addresses]
    keyboard = create_options_keyboard(options, correct_answer, "info")
    await call.message.answer(
        f"Для подсети с маской сети {subnet_mask} сколько различных адресов компьютеров теоретически допускает эта маска, "
        f"если два адреса (адрес сети и широковещательный) не используются?",
        reply_markup=keyboard
    )


async def informatics_bits_task(call: CallbackQuery):
    alphabet_size = random.choice([32, 64, 128, 256])
    bits_required = alphabet_size.bit_length()

    options = list(set([
        bits_required,
        bits_required + 1,
        bits_required - 1 if bits_required > 1 else 1,
        random.randint(2, 10)
    ]))
    random.shuffle(options)

    correct_answer = bits_required
    keyboard = create_options_keyboard(options, correct_answer, "info")

    await call.message.answer(
        f"Какое минимальное количество бит необходимо для кодирования каждого символа, "
        f"если алфавит содержит {alphabet_size} символов?",
        reply_markup=keyboard
    )


async def football_probability_task(call: CallbackQuery):
    team_a = "A"
    team_b = "B"
    team_c = "C"

    probability_first = round(random.uniform(0.3, 0.7), 1)
    probability_both_matches = round(probability_first ** 2, 2)
    correct_answer = str(probability_both_matches)

    options = [
        probability_both_matches,
        round(probability_both_matches + random.uniform(0.1, 0.5), 2),
        round(probability_both_matches - random.uniform(0.1, 0.5), 2),
        round(random.uniform(0.0, 1.0), 2)
    ]
    keyboard = create_options_keyboard(options, correct_answer, "math")
    await call.message.answer(
        f"Команда {team_a} должна сыграть с командами {team_b} и {team_c} по одному разу. "
        f"Какова вероятность того, что команда {team_a} будет первой владеть мячом в обоих матчах?",
        reply_markup=keyboard
    )


async def informatics_conversion_task(call: CallbackQuery):
    number = random.randint(10, 100)
    binary = bin(number)[2:]
    options = [binary, bin(number + 1)[2:], bin(number - 1)[2:],
               bin(random.randint(1, 100))[2:]]
    random.shuffle(options)
    keyboard = create_options_keyboard(options, binary, "info")
    await call.message.answer(
        f"Переведите число {number} из десятичной системы счисления в двоичную:",
        reply_markup=keyboard
    )


async def generate_cone_pyramid_task(call: CallbackQuery):
    volume_cone = random.uniform(100, 200)
    height_cone = random.randint(7, 15)
    radius_cone = ((3 * volume_cone) / height_cone) ** (1 / 3)
    side_square = radius_cone * (2 ** 0.5)
    area_base = side_square ** 2
    volume_pyramid = (1 / 3) * area_base * height_cone
    correct_answer = str(round(volume_pyramid))
    options = [
        round(volume_pyramid),
        random.randint(1, 4) * 100,
        random.randint(1, 4) * 50 + 50,
        random.randint(1, 4) * 150
    ]
    keyboard = create_options_keyboard(options, correct_answer, "math")
    await call.message.answer(
        f"В круговой конус вписана правильная четырехугольная пирамида.\n"
        f"Объем конуса равен {volume_cone:.2f}, а высота равна {height_cone}\n"
        f"Каков объем вписанной пирамиды?",
        reply_markup=keyboard
    )


async def informatics_encoding_task(call: CallbackQuery):
    num_symbols = 7
    message_length = 120

    bits_per_symbol = math.ceil(math.log2(num_symbols))
    total_bits = bits_per_symbol * message_length
    total_bytes = math.ceil(total_bits / 8)

    correct_answer = total_bytes
    options = list(set([
        correct_answer,
        correct_answer + random.randint(1, 5),
        correct_answer - random.randint(1, 3),
        random.randint(10, 50)
    ]))
    random.shuffle(options)

    keyboard = create_options_keyboard(options, correct_answer, "info")
    await call.message.answer(
        f"В некотором алфавите используется {num_symbols} символов. "
        f"Для передачи сообщений каждый символ кодируется одинаковым минимально возможным числом бит. "
        f"Сообщение содержит {message_length} символов.\n\n"
        f"Какой объем памяти (в байтах) необходим для хранения этого сообщения?",
        reply_markup=keyboard
    )


# МАТЕМАТИКА
easy_math_tasks = [
    math_percentage_task,
    math_speed_task,
    math_probability_task,
]

medium_math_tasks = [
    math_probability_1_test,
    math_AB_task,
]

hard_math_tasks = [
    football_probability_task,
    generate_cone_pyramid_task,
]

# ФИЗИКА
easy_physics_tasks = [
    physics_force_task,
    physics_energy_task,
    physics_ohms_task,
]

medium_physics_tasks = [
    impulse_calculation_task,
    physics_energy_task,
    physics_mkT_1_task,
]

hard_physics_tasks = [
    harmonic_oscillator_task,
]

# ИНФОРМАТИКА
easy_informatics_tasks = [
    informatics_bits_task,
    informatics_conversion_task,
]

medium_informatics_tasks = [
    informatics_sorting_task,
    informatics_encoding_task,
    network_address_task,
]

hard_informatics_tasks = [
    memory_storage_task,
    audio_file_size_task,
]


async def run_random_task(event, subject: str, difficulty: str):
    task_map = {
        "math": {
            "easy": easy_math_tasks,
            "medium": medium_math_tasks,
            "hard": hard_math_tasks,
        },
        "physics": {
            "easy": easy_physics_tasks,
            "medium": medium_physics_tasks,
            "hard": hard_physics_tasks,
        },
        "informatics": {
            "easy": easy_informatics_tasks,
            "medium": medium_informatics_tasks,
            "hard": hard_informatics_tasks,
        }
    }

    task_list = task_map[subject][difficulty]
    await random.choice(task_list)(event)
