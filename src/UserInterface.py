import Deck, Cards, KingdomCards, Menu


class UserInterface:

    def __init__(self):
        self.__Deck = Deck.Deck()
        self.__playDeck = Deck.Deck(10)
        self.__trimDeck = Deck.Deck()
        self.__editionList = [
            "Edition List",
            "Dominion",
            "\t1.1 - 1st Edition",
            "\t1.2 - 2nd Edition",
            "Intrigue",
            "\t2.1 - 1st Edition",
            "\t2.2 - 2nd Edition",
            "3 - Seaside",
            "4 - Alchemy",
            "5 - Prosperity",
            "6 - Cornucopia",
            "7 - Hinterlands",
            "8 - Dark Ages",
            "9 - Guilds",
            "10 - Adventures",
            "11 - Empires",
            "12 - Nocturne",
            "13 - Renaissance",
            "14 - Menagerie"
        ]


    def run(self):

        print("What editions are you playing with?")
        msg = ""
        for i in self.__editionList:
            msg += i + "\n"
        msg += "D - Done with selection\n"
        msg += "R - Restart selection\n"
        msg += "P - Print current selection\n"
        msg += "X - Exit\n"
        print(msg)
        keepGoing = True
        editionList = []
        while keepGoing:
            userInput = input("Command: ")
            if userInput == "X":
                keepGoing = False
            elif userInput == "1.1" or userInput == "1.2":
                if "Dominion" not in editionList and not (
                        "Dominion 1st Edition" in editionList or "Dominion 2nd Edition" in editionList):
                    editionList.append("Dominion")
                if userInput == "1.2" and not "Dominion 2nd Edition" in editionList:
                    editionList.append("Dominion 2nd Edition")
                elif userInput == "1.1" and not "Dominion 1st Edition" in editionList:
                    editionList.append("Dominion 1st Edition")
            elif userInput == "2.1" or userInput == "2.2":
                if "Intrigue" not in editionList and not (
                        "Intrigue 1st Edition" in editionList or "Intrigue 2nd Edition" in editionList):
                    editionList.append("Intrigue")
                if userInput == "2.2" and not "Intrigue 2nd Edition" in editionList:
                    editionList.append("Intrigue 2nd Edition")
                elif userInput == "2.1" and not "Intrigue 1st Edition" in editionList:
                    editionList.append("Intrigue 1st Edition")
            elif userInput.isdigit() and 2 < int(userInput) < 15:
                if not KingdomCards.GAMEEDITIONS[int(userInput) + 3] in editionList:
                    editionList.append(KingdomCards.GAMEEDITIONS[int(userInput) + 3])
            elif userInput == "D":
                self.__BuildDeck(editionList)
                self.__EditDeck()
            elif userInput == "R":
                editionList = []
            elif userInput == "P":
                print("Your current selection:")
                for i in editionList:
                    print("\t" + i)
            else:
                print(msg)

    def __BuildDeck(self, editionList):
        for i in range(len(editionList)):
            for j in range(len(KingdomCards.KINGDOMCARDDECK)):
                if Cards.Card(j).getEditionName() == editionList[i]:
                    self.__Deck.addCard(j)

    def __EditDeck(self):
        print("Welcome to the Edit Menu")
        menu = Menu.Menu("Edit")
        menu.addOption("D", "Shuffle and draw cards")
        menu.addOption("S", "Save a specific card to play with")
        menu.addOption("R", "Remove card from draw deck")
        menu.addOption("E", "Draw cards from an Edition")
        menu.addOption("C", "Draw cards of a certain cost")
        menu.addOption("T", "Draw cards of a certain type")
        menu.addOption("M", "Build a selection to draw from")
        menu.addOption("P", "Print current selection")
        menu.addOption("X", "Return to Edition Selection")

        keepGoing = True

        while keepGoing:
            userInput = menu.show()
            if userInput == "D":
                self.__DrawDeck()
            elif userInput == "S":
                self.__SaveCard()
            elif userInput == "R":
                self.__RemoveCard()
            elif userInput == "E":
                self.__TrimEdition()
                self.__ClearTrim()
            elif userInput == "C":
                self.__TrimCost()
                self.__ClearTrim()
            elif userInput == "T":
                self.__TrimType()
                self.__ClearTrim()
            elif userInput == "M":
                self.__TrimMenu()
                self.__ClearTrim()
            elif userInput == "P":
                print("Your current selection: ")
                self.__playDeck.printDeck()
            elif userInput == "X":
                keepGoing = False

    def __ClearTrim(self):
        for i in range(self.__trimDeck.getSize()):
            self.__playDeck.addCard(self.__trimDeck.draw())
            i -= 1

    def __DrawDeck(self):
        # TODO
        pass

    def __TrimMenu(self):
        # TODO
        pass

    def __TrimEdition(self):
        # TODO
        pass

    def __TrimCost(self):
        # TODO
        pass

    def __TrimType(self):
        # TODO
        pass

    def __SaveCard(self):
        # TODO
        pass

    def __RemoveCard(self):
        # TODO
        pass