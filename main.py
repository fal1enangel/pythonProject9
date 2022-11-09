import random
import requests
import telebot #библиотека бота
from bs4 import BeautifulSoup as b

bot = telebot.TeleBot('5608475022:AAHwmLXcZriEm1YpJWrmVATB-sR9z0IQ0Gk') #авторизация (токен) бота
from telebot import types

first = ['Думаем и пересчитываем деньги чаще – это приманит к нам финансовую энергию.',
         'Сегодня стремления и возможности будут находиться в гороскопе на разных полюсах.',
         'Сдвинуться с места заставляет лишь острая необходимость или «волшебный пинок», если же их нет, можно весь день провести за перекладыванием с места на место бумажек, увлекательными беседами ни о чем или томным созерцанием действительности за окном.'
    , 'Гороскоп советует дать себе отдых: если есть возможность – отложите дела.',
         'Сегодня Луна в Тельце, энергетика довольно тяжелая.',
         'Если вы своевременно найдете недостатки в своей работе, то еще есть время исправить их без материальных потерь для себя.']
second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
c = ['Лучше синица в руках, чем в каком-нибудь другом месте.', 'Индюк тоже думал, что купается, пока вода не закипела.',
     'Каждому овощу свой фрукт.', 'Каждому овощу свой фрукт.', 'Дело небогато, да сделано рогато.',
     'Алкоголизм не пропьешь!', 'Если б не «еслиб», купил бы деревеньку и жил бы помаленьку.',
     'Лучше c Петровым на Майорке, чем с майором на Петровке',
     'Каждому овощу свой фрукт.', 'Что посеешь, потом хрен найдешь.']
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
    bot.send_message(message.from_user.id,
                     "Привет, сейчас я расскажу тебе гороскоп на сегодня. Если не хочешь гороскоп, то напиши пословица.")
keyboard = types.InlineKeyboardMarkup()
key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
keyboard.add(key_oven)
key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
keyboard.add(key_telec)
key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
keyboard.add(key_bliznecy)
key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
keyboard.add(key_rak)
key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
keyboard.add(key_lev)
key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
keyboard.add(key_deva)
key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
keyboard.add(key_vesy)
key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
keyboard.add(key_scorpion)
key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
keyboard.add(key_strelec)
key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
keyboard.add(key_kozerog)
key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
keyboard.add(key_vodoley)
key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
keyboard.add(key_ryby)
bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
elif message.text == "/help":
bot.send_message(message.from_user.id, "Напиши Привет")
elif message.text == 'пословица' or message.text == 'Пословица':
bot.send_message(message.from_user.id, random.choice(c))
else:
bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help. И держи анекдот")
r2 = requests.get("https://www.anekdot.ru/last/good/").text
soup = b(r2, 'html.parser')
anekdots = soup.find_all('div', class_='text')
clear_anek = [c.text for c in anekdots]
bot.send_message(message.from_user.id, random.choice(clear_anek))

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
    msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add)
bot.send_message(call.message.chat.id, msg)

bot.infinity_polling()