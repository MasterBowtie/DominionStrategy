import src.MenuOptions

class EditionMenu:
    def __init__(self):
        self.__header = "Edition"
        options = []
        options.append(MenuOptions.MenuOption("1.1", "1st Edition"))
        options.append(MenuOptions.MenuOption("1.2", "2nd Edition"))
        options.append(MenuOptions.MenuOption("2.1", "1st Edition"))
        options.append(MenuOptions.MenuOption("2.2", "2nd Edition"))
        options.append(MenuOptions.MenuOption("3", "Seaside"))
        options.append(MenuOptions.MenuOption("4", "Alchemy"))
        options.append(MenuOptions.MenuOption("5", "Prosperity"))
        options.append(MenuOptions.MenuOption("6", "Cornicopia"))
        options.append(MenuOptions.MenuOption("7", "Hinterlands"))
        options.append(MenuOptions.MenuOption("8", "Dark Ages"))
        options.append(MenuOptions.MenuOption("9", "Guilds"))
        options.append(MenuOptions.MenuOption("10", "Adventures"))
        options.append(MenuOptions.MenuOption("11", "Empires"))
        options.append(MenuOptions.MenuOption("12", "Nocturne"))
        options.append(MenuOptions.MenuOption("13", "Renaissance"))
        options.append(MenuOptions.MenuOption("14", "Menagerie"))
        options.append(MenuOptions.MenuOption("D", "Done with selection"))
        options.append(MenuOptions.MenuOption("R", "Restart selection"))
        options.append(MenuOptions.MenuOption("P", "Print current selection"))
        options.append(MenuOptions.MenuOption("X", "Exit"))
        self.__options = options
        self.__optionCount = len(options)

    def __isValidCommand(self, command):
        isValid = False
        for i in range(len(self.__options)):
            if command == self.__options[i].getCommand():
                isValid = True
                break
        return isValid

    def show(self):
        print("\nWhat editions are you playing with?\n")
        print(self.__header, "Menu:")
        print("Dominion")
        print(f"\t{self.__options[0].getCommand()} - {self.__options[0].getDescription()}")
        print(f"\t{self.__options[1].getCommand()} - {self.__options[1].getDescription()}")
        print("Intrigue")
        print(f"\t{self.__options[2].getCommand()} - {self.__options[2].getDescription()}")
        print(f"\t{self.__options[3].getCommand()} - {self.__options[3].getDescription()}")
        for i in range(4, len(self.__options)):
            print(f"{self.__options[i].getCommand()} - {self.__options[i].getDescription()}")

        print(f"\nEnter {self.__header} command (", end=" ")
        for i in range(len(self.__options) - 4, len(self.__options)):
            print(f"{self.__options[i].getCommand()}", end=" ")
        print(")")

class Menu:

    def __init__(self, header):
        self.__header = header
        self.__options = []

    def addOption(self, command, description):

        if command is not None and command != "":
            self.__options.append(MenuOptions.MenuOption(command, description))

    def __isValidCommand(self, command):
        isValid = False
        for i in range(len(self.__options)):
            if command == self.__options[i].getCommand():
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
        return len(self.__options)

    def show(self):
        command, keepGoing = '', True

        while keepGoing:
            print("\n" + str(self.getHeader()) + " Menu:")

            for i in range(len(self.__options)):
                print(f"{self.__options[i].getCommand()} - {self.__options[i].getDescription()}")
            print(f"\nEnter a {self.__header} command (", end=" ")
            for i in range(len(self.__options)):
                print(f"{self.__options[i].getCommand()} ", end="")
            print(")")

            command = input("Command: ")
            keepGoing = not self.__isValidCommand(command.upper())

        return command.upper()
