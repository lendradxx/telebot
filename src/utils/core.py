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


def createLine(line: str, length: int):
    resultLine = ""
    for i in range(0, length):
        resultLine += line

    return resultLine


def printHeader(headerTitle: str):
    terminalSize = os.get_terminal_size()
    lengthLine = int((terminalSize.columns / 2) - len(headerTitle))
    beginLine = createLine("=", length=lengthLine)
    endLine = createLine("=", length=lengthLine)
    print(f"{beginLine}{headerTitle}{endLine}")
