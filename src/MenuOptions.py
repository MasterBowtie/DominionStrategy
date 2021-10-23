
class MenuOption:

    def __init__(self, command, description):

        self.__command = command
        self.__description = description

    def getCommand(self):
        return self.__command

    def getDescription(self):
        return self.__description
