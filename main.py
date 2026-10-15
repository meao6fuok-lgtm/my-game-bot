import telebot
from telebot import types

TOKEN = '8864719805:AAEODhrkA5Y-wyUxrHfAHR7I5dm7Ow4qj58'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('لعبة Cuphead')
    btn2 = types.KeyboardButton('GTA San Andreas')
    btn3 = types.KeyboardButton('Hollow Knight')
    btn4 = types.KeyboardButton('لعبة God of War 1')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "🎮 أهلاً بك! اختر اللعبة التي تريد تحميلها من القائمة:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_game_selection(message):
    text = message.text
    if text == 'لعبة Cuphead':
        bot.send_message(message.chat.id, "🎮 رابط تحميل لعبة Cuphead المباشر:\nhttps://apkvision.org/app/games/cuphead-mobile-91548/")
    elif text == 'GTA San Andreas':
        bot.send_message(message.chat.id, "🎮 رابط تحميل لعبة GTA San Andreas:\nhttps://www.mediafire.com/file_example")
    elif text == 'Hollow Knight':
        bot.send_message(message.chat.id, "🎮 رابط تحميل لعبة Hollow Knight:\nhttps://apkpure.com/ar/hollow-knight/com.davy.hollowknight")
    elif text == 'لعبة God of War 1':
        bot.send_message(message.chat.id, "🎮 رابط تحميل لعبة God of War 1:\nhttps://play.google.com/store/apps/details?id=com.gowcos.ppspp")
    else:
        bot.send_message(message.chat.id, "اختر لعبة من الأزرار بالأسفل 👇")

print("البوت يعمل الآن بنجاح تام...")
bot.infinity_polling(timeout=60, long_polling_timeout=5)
