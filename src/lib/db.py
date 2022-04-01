import os
from tinydb import TinyDB, Query


class User:
    def __init__(self) -> None:
        dataPath = "data/users.json"
        # Check is data directory exist
        if not os.path.isdir("data"):
            try:
                os.mkdir("data")
            except:
                os.makedirs("data")

        # Check is data file exist
        if not os.path.isfile(dataPath):
            fp = open(dataPath, "w")
            fp.write("")
            fp.close()

        self.db = TinyDB("data/users.json")
        self.user = Query()

    def addUser(self, name: str, username: str):
        self.db.insert({"name": name, "username": username})

    def getUser(self, username: str):
        return self.db.search(self.user.username == username)

    def getAllUser(self):
        return self.db.all()

    def checkUser(self, username: str):
        userDB = self.getUser(username)
        if len(userDB) == 0:
            return False
        else:
            if userDB[0]["username"] == username:
                return True
            else:
                return False
