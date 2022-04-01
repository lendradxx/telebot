from telebot import TeleBot, types


def textHandler(bot: TeleBot, msg: types.Message):
    command = msg.text[1:len(msg.text)].strip().split(" ").pop(0).lower()
    args = msg.text[1:len(msg.text)].strip().split(" ")[1:len(msg.text)]

    if command == "hello":
        bot.reply_to(msg, "Hello!")
    elif command == "say":
        bot.send_message(msg.chat.id, " ".join(args))
    elif command == "start":
        pass
    else:
        pass