import telebot
import random
from pyexpat.errors import messages

bot = telebot.TeleBot('7741259913:AAHdSZGIPtNb3wKA6gbBBr3k_wRbDFtalwc')

@bot.message_handler(commands=['start'])
def main(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Математика', callback_data='math')
    btn2 = telebot.types.InlineKeyboardButton('Физика', callback_data='physics')
    btn3 = telebot.types.InlineKeyboardButton('Информатика', callback_data='informatics')
    markup.row(btn1, btn2, btn3)
    bot.reply_to(message, 'Какой предмет вы хотите потренировать?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_subject_selection(call):
    if call.data == 'math':
        show_options(call, 'Математика')
    elif call.data == 'physics':
        show_options(call, 'Физика')
    elif call.data == 'informatics':
        show_options(call, 'Информатика')
    elif call.data.startswith(('random_', 'topic_', 'test_')):
        option, subject = call.data.split('_', 1)
        if option == 'random':
            bot.send_message(call.message.chat.id, f'Вы выбрали случайные вопросы по {subject}.')
            random_math(call)
        elif option == 'topic':
            bot.send_message(call.message.chat.id, f'Вы выбрали вопросы по определённой теме по {subject}.')
        elif option == 'test':
            bot.send_message(call.message.chat.id, f'Вы выбрали тест по {subject}.')
        #print(1235146, call)
    elif call.data.startswith(('answer_')):
        a, b, x = call.data.split('_')
        if b == x:
            bot.send_message(call.message.chat.id, f'Верно!')
        else:
            bot.send_message(call.message.chat.id, f'Неверно, {x}')

def show_options(call, subject):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Случайные вопросы', callback_data=f'random_{subject}')
    btn2 = telebot.types.InlineKeyboardButton('По определённой теме', callback_data=f'topic_{subject}')
    btn3 = telebot.types.InlineKeyboardButton('Тест', callback_data=f'test_{subject}')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(call.message.chat.id, f'Вы выбрали {subject}. Выберите вариант:', reply_markup=markup)
    #bot.register_next_step_handler(call, handle_option_selection)


def random_math(call):
    a = random.randint(1, 20) * 5
    b = random.randint(1, 20) * 5
    s = random.randint(45, 80) * 5
    t = random.choice([0.5, 1, 1.5, 2])
    #a, b, s, t = 50, 55, 415, 2
    x = ((s-a*t)/(a+b)+t)*a
    #print(a, b, s, t, x)
    while int(x) != x:
        a = random.randint(1, 20) * 5
        b = random.randint(1, 20) * 5
        s = random.randint(45, 80) * 5
        t = random.choice([0.5, 1, 1.5, 2])
        #a, b, s, t = 50, 55, 415, 2
        x = ((s-a*t)/(a+b)+t)*a
        print(a, b, s, t, x)
    x1 = random.randint(45, 80) * 5
    x2 = random.randint(45, 80) * 5
    x3 = int(s - x)
    x = int(x)
    an = [x, x1, x2, x3]
    random.shuffle(an)
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(str(an[0]), callback_data=f'answer_{an[0]}_{x}')
    btn2 = telebot.types.InlineKeyboardButton(str(an[1]), callback_data=f'answer_{an[1]}_{x}')
    btn3 = telebot.types.InlineKeyboardButton(str(an[2]), callback_data=f'answer_{an[2]}_{x}')
    btn4 = telebot.types.InlineKeyboardButton(str(an[3]), callback_data=f'answer_{an[3]}_{x}')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(call.message.chat.id, f'Расстояние между городами A и B равно {s}км. Из города A в город B со скоростью {a}км/ч выехал первый автомобиль,'
                                           f' а через {t} часа после этого навстречу ему из города B выехал второй автомобиль со скоростью {b}км/ч.'
                                           f' На каком расстоянии от города A автомобили встретятся? Ответ дайте в километрах.Выберите вариант ответа:', reply_markup=markup)


bot.polling(non_stop=True)