import os
import telebot
from telebot import types

TOKEN = '8864719805:AAEODhrkA5Y-wyUxrHfAHR7I5dm7Ow4qj58'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_cuphead = types.KeyboardButton('لعبة Cuphead')
    btn_gta_sa = types.KeyboardButton('GTA San Andreas')
    btn_hollow = types.KeyboardButton('Hollow Knight')
    btn_godofwar = types.KeyboardButton('لعبة God of War 1')
    markup.add(btn_cuphead, btn_gta_sa, btn_hollow, btn_godofwar)
    bot.send_message(message.chat.id, "🎮 أهلاً بك! اختر اللعبة التي تريد تحميلها من القائمة:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_game_selection(message):
    text = message.text
    if text == 'لعبة Cuphead':
        link = "https://apkvision.org/app/games/cuphead-mobile-91548/"
        bot.send_message(message.chat.id, f"🎮 رابط تحميل لعبة Cuphead المباشر:\n\n{link}")
    elif text == 'GTA San Andreas':
        link = "https://www.mediafire.com/file_example"
        bot.send_message(message.chat.id, f"🎮 رابط تحميل لعبة GTA San Andreas (نسخة معدلة 60fps):\n\n{link}")
    elif text == 'Hollow Knight':
        link = "https://apkpure.com/ar/hollow-knight/com.davy.hollowknight"
        bot.send_message(message.chat.id, f"🎮 رابط تحميل لعبة Hollow Knight (التحديث الجديد):\n\n{link}")
    elif text == 'لعبة God of War 1':
        link = "https://play.google.com/store/apps/details?id=com.gowcos.ppspp"
        bot.send_message(message.chat.id, f"🎮 رابط تحميل لعبة God of War 1 من متجر بلاي:\n\n{link}")
    else:
        bot.send_message(message.chat.id, "يرجى اختيار إحدى الألعاب من القائمة الموجودة بالأسفل 👇")

if __name__ == '__main__':
    print("...البوت يعمل الآن على منصة ريلواي")
    bot.polling(non_stop=True, interval=0, timeout=20)
