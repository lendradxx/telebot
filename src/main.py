import os
from telebot import TeleBot, types
from utils import core
from components import handler

if __name__ == "__main__":
    bot = TeleBot(core.getConfig("BOT", "TOKEN"))
    # Print Info Bot
    core.printHeader("[BOT-INFO]")
    print(f"BOT NAME: @{bot.get_me().username}")
    print("PREFIX: ", core.getConfig("BOT", "PREFIX"))

    # Handling message
    @bot.message_handler(content_types="text")
    def textHandler(message: types.Message):
        if core.lateMsg(message.date): return
        handler.textHandler(bot=bot, msg=message)

    print("Listening")
    bot.infinity_polling(skip_pending=True)