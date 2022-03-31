import configparser, time, os


def getConfig(header: str, variable: str):
    config = configparser.ConfigParser()
    config.read_file(open("settings.conf"))
    return config.get(header, variable)


def lateMsg(date: int):
    totalDate = int(time.time()) - date
    if totalDate >= 5:
        return True
    else:
        return False


def printHeaderLine(line: str):
    terminalSize = os.get_terminal_size()
    resultLine = ""
    for i in range(terminalSize.columns):
        resultLine += line

    print(resultLine)