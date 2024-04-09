import telebot
from config import TOKEN, TIME_UPDATE_DB, TIME_UPDATE_USER
from loguru import logger
from parser import update_info
from time import sleep
from database import Database
from threading import Thread
from datetime import datetime


logger.add("./data/debug.log")

bot = telebot.TeleBot(TOKEN)
logger.info("Staring bot")


@bot.message_handler(commands=["start"])
def start(message):
    while True:
        logger.info(f"Getting data from {message.from_user.first_name}{message.from_user.last_name} (@{message.from_user.username})")
        data = update_info()
        logger.info(f"Data is loaded from {message.from_user.first_name}{message.from_user.last_name} (@{message.from_user.username})")

        # bot.delete_message(message.chat.id, message.message_id)  # TODO: Починить
        bot.send_message(message.from_user.id, data)

        sleep(TIME_UPDATE_USER)


def saving_data():
    while True:
        Database(update_info(), str(datetime.now())).save_data()
        sleep(TIME_UPDATE_DB)


Thread(target=saving_data).start()

bot.polling()
