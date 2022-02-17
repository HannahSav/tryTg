from random import randint
import config
from array import *
from telebot import *

bot = telebot.TeleBot(config.TOKEN)
array_of_jokes = ["Негр загорает", "Колобок повесился", "Буратино утонул"]


# @bot.message_handler(content_types=["text"])
# def default_test(message):
#    keyboard = types.InlineKeyboardMarkup()
#    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
#    keyboard.add(url_button)
#    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, "Это бот с анекдотами.\n"
                                      "/add_joke - добавить новый анек \n"
                                      "/read_joke - прочитать анек")


@bot.message_handler(commands=["add_joke"])
def add_joke(message):
    bot.send_message(message.chat.id, "Введите ваш анекдот одним сообщением:")
    bot.register_next_step_handler(message, third)


def third(message):
    array_of_jokes.append(message.text)
    bot.send_message(message.chat.id, "Ваш анекдот успешно добавлен")


@bot.message_handler(commands=["read_joke"])
def read_joke(message):
    num = randint(0, len(array_of_jokes) - 1)
    bot.send_message(message.chat.id, array_of_jokes[num])


@bot.message_handler(commands=["have_coffee"])
def coffee(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="caputino", url="https://ya.ru")
    url_button1 = types.InlineKeyboardButton(text="latte", url="https://ya.ru")
    keyboard.add(url_button)
    keyboard.add(url_button1)
    bot.send_message(message.chat.id, "choo", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
