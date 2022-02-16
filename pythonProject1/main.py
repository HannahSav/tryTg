import config
import telebot
from telebot import *

bot = telebot.TeleBot(config.TOKEN)


#@bot.message_handler(content_types=["text"])
#def default_test(message):
#    keyboard = types.InlineKeyboardMarkup()
#    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
#    keyboard.add(url_button)
#    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "nu ti i kek")

@bot.message_handler(commands=["have_coffee"])
def coffee(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="caputino", url="https://ya.ru")
    url_button1 = types.InlineKeyboardButton(text="latte", url="https://ya.ru")
    keyboard.add(url_button)
    keyboard.add(url_button1)
    bot.send_message(message.chat.id, "choo", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    print(message)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.infinity_polling()