# -*- coding: utf-8 -*-

import random
import telebot

bot = telebot.TeleBot('token')

from telebot import types

# Заготовка для первого предложения
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
cookie = ["Делайте то, чего просит душа и тело", "Делайте то, что Вы считаете правильным для Вас", "Будьте внимательны к подсказкам судьбы", "Сделай что-то важное прямо сейчас", "Если чувствуешь, что это твое — никого не слушай, рискни!", "Любовь украсит ваши дни, и станут яркими они", "Время – ваш союзник, лучше отложить принятие важного решения хотя бы на день"]

#Стартовое общение с пользователем

@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Связаться со звёздами")
    btn2 = types.KeyboardButton("Печенька с предсказанием")
    btn3 = types.KeyboardButton("Что ты умеешь?")
    markup.add(btn1, btn2, btn3)
    send_message = f'<b>Привет, {message.from_user.first_name}!</b>\nЯ твой лучший ассистент. Гадалки могут обманывать, звёзды же обмануть не могут. У меня самый достоверный гороскоп, который поможет тебе спланировать предстоящий день. Обрати внимание на кнопочки внизу\n<b>Связаться со звёздами</b> - получить лучший и самый точный гороскоп\n<b>Печенька с предсказанием</b> - да, это то, о чем вы подумали. Печенька. С предсказанием\n<b>Что ты умеешь?</b> - всем заблудшим душам порой нужна помощь, нажми сюда, если запутаешься'
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Печенька с предсказанием':
        bot.send_message(message.from_user.id, random.choice(cookie))
    elif message.text == 'Связаться со звёздами':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton(text='Овен', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Телец', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Рак', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Лев', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Девы', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Весы', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Козерог', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Водолец', callback_data='zodiac'),
            types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        ]
        keyboard.add(*buttons)
        #показываем все кнопки с сообщением
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup = keyboard)
    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.from_user.id, 'Что я умею? Наставить тебя на истинный путь, замотивировать, позволить прислушаться к вселенной на основе глубоко-осмысленной и сгенерированной мной информации. \nКнопки внизу помогут тебе получить полный гороскоп или же короткое предсказание. Удачи! Прислушиваться к моим советам или нет - решать, конечно же, только тебе')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю, я хорошо понимаю звёзды, но плохо понимаю людей. Ты всегда можешь набрать в чате /help, чтобы вспомнить чему я обучен')


#обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call:True)
def callback_worcker(call):
    #Если нажали на кнопку - выводим гороскоп
    if call.data == 'zodiac':
        #формируем текст гороскопа
        msg = random.choice(first) + ' ' +random.choice(second) + ' '+ random.choice(second_add) + ' ' + random.choice(third)
        bot.send_photo(call.message.chat.id, photo='https://img1.goodfon.ru/wallpaper/nbig/1/55/kosmos-zvezda-belyy-karlik.jpg')
        #отправляем текст юзеру
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop = True, interval = 0)
