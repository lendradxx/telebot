import datetime
from utils import core
from lib.db import User
from telebot import TeleBot, types


def textHandler(bot: TeleBot, msg: types.Message):
    userDB = User()
    command = msg.text[1 : len(msg.text)].strip().split(" ").pop(0).lower()
    args = msg.text[1 : len(msg.text)].strip().split(" ")[1 : len(msg.text)]
    # Log new message
    print(f"Sender: @{msg.chat.username}")
    print(f"Command: {command}")
    print(f"Args: [{len(args)}]")
    print(f"Date: {datetime.datetime.now().strftime('%Y/%m/%d')}")
    core.printHeaderLine("=")

    if command == "hello":
        bot.reply_to(msg, "Hello!")
    elif command == "say":
        bot.send_message(msg.chat.id, " ".join(args))
    elif command == "start":
        if userDB.checkUser(msg.chat.username):
            print("[DBMS]: Skipped, because user already registered")
            core.printHeaderLine("=")
            return

        print("[DBMS]: Inserting new users...")
        userDB.addUser(msg.chat.first_name, msg.chat.username)
        core.printHeaderLine("=")
    else:
        pass
