from random import randint
import config
from db import *
from telebot import *

#TODO:
#add likes, dislikes, reit
#add bd (read)
#add command menu

bot = telebot.TeleBot(config.TOKEN)
connect()
array_of_jokes = ["Негр загорает", "Колобок повесился", "Буратино утонул"]


@bot.message_handler(commands=["start", "help"])
def start(message):
    truncate()
    bot.send_message(message.chat.id, "Это бот с анекдотами.\n"
                                      "/add_joke - добавить новый анек \n"
                                      "/read_joke - прочитать анек")


@bot.message_handler(commands=["add_joke"])
def add_joke(message):
    bot.send_message(message.chat.id, "Введите ваш анекдот одним сообщением:")
    bot.register_next_step_handler(message, third)


def third(message):
    insert(message)
    array_of_jokes.append(message.text)
    bot.send_message(message.chat.id, "Ваш анекдот успешно добавлен")


@bot.message_handler(commands=["read_joke"])
def read_joke(message):
    num = randint(0, len(array_of_jokes) - 1)
    bot.send_message(message.chat.id, array_of_jokes[num])
    print (message)



if __name__ == '__main__':
    bot.infinity_polling()
