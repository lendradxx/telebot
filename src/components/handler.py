from telebot import TeleBot, types


def textHandler(bot: TeleBot, msg: types.Message):
    command = msg.text[1:len(msg.text)].strip().split(" ").pop(0).lower()

    if command == "hello":
        bot.reply_to(msg, "Hello!")
    elif command == "yo":
        bot.reply_to(msg, "Yo!")
    else:
        pass