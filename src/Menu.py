import MenuOptions


class Menu:

    def __init__(self, header):
        self.__header = header
        self.__optionCount = 0
        self.__options = []

    def addOption(self, command, description):

        if command is not None and command != "":
            self.__options.append(MenuOptions.MenuOption(command, description))
            self.__optionCount += 1

    def __isValidCommand(self, command):
        isValid = False
        for i in range(self.getOptionCount()):
            if command == self.getOption(i).getCommand():
                isValid = True
                break
        return isValid

    def getOption(self, optionIndex):
        option = None
        if optionIndex >= 0 and optionIndex < self.getOptionCount():
            option = self.__options[optionIndex]
        return option

    def getHeader(self):
        return self.__header

    def getOptionCount(self):
        return self.__optionCount

    def show(self):
        command, keepGoing = '', True

        while keepGoing:
            optionList = ''

            print()
            print(self.getHeader(), "menu:")

            for i in range(self.getOptionCount()):
                option = self.getOption(i)
                if option is not None and i == self.getOptionCount() - 1:
                    print(f"{option.getCommand()} - {option.getDescription()}")
                    optionList += option.getCommand()
                elif option is not None:
                    print(f"{option.getCommand()} - {option.getDescription()}")
                    optionList += option.getCommand() + ", "


            print(f"\nEnter a {self.getHeader()} command ({optionList})")
            command = input()
            keepGoing = not self.isValidCommand(command)

        return command

