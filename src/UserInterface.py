import Deck, Cards, KingdomCards, Menu


class UserInterface:
    def __init__(self):
        self.__Deck = Deck.Deck()
        self.__playDeck = Deck.Deck(10)
        self.__trimDeck = Deck.Deck()
        self.__typeList = []
        self.__costList = []
        self.__editionList = []

    def run(self):
        menu = Menu.EditionMenu()
        menu.show()
        keepGoing = True
        editionList = []
        while keepGoing:
            userInput = input("Command: ")
            if userInput.upper() == "X":
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
            elif userInput.upper() == "D":
                self.__BuildDeck(editionList)
                self.__EditDeck()
                menu.show()
            elif userInput.upper() == "R":
                editionList = []
            elif userInput.upper() == "P":
                print("Your current selection:")
                for i in editionList:
                    print("\t" + i)


    def __BuildDeck(self, editionList):
        for i in range(len(editionList)):
            for j in range(len(KingdomCards.KINGDOMCARDDECK)):
                if Cards.Card(j).getEditionName() == editionList[i]:
                    self.__Deck.addCard(j)
        for card in self.__Deck:
            for cost in KingdomCards.COST:
                if card.getCost() == cost and cost not in self.__costList:
                    self.__costList.append(cost)
            for type in KingdomCards.CARDTYPE:
                if card.getType() == type and type not in self.__typeList:
                    self.__typeList.append(type)
            for edition in KingdomCards.GAMEEDITIONS:
                if card.getEditionName() == edition and edition not in self.__editionList:
                    self.__editionList.append(edition)
        print(self.__costList)
        print(self.__typeList)
        print(self.__editionList)

    def __EditDeck(self):
        print("\nWelcome to the Edit Menu")
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
            if userInput.upper() == "D":
                self.__DrawDeck()
            elif userInput.upper() == "S":
                self.__SaveCard()
            elif userInput.upper() == "R":
                self.__RemoveCard()
            elif userInput.upper() == "E":
                self.__TrimEdition()
                self.__ClearTrim()
            elif userInput.upper() == "C":
                self.__TrimCost()
                self.__ClearTrim()
            elif userInput.upper() == "T":
                self.__TrimType()
                self.__ClearTrim()
            elif userInput.upper() == "M":
                self.__TrimMenu()
                self.__ClearTrim()
            elif userInput.upper() == "P":
                print("Your current selection: ")
                self.__playDeck.printDeck()
            elif userInput.upper() == "X":
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
        print("Do you know the name of the Card (Y/N)?")
        userInput = input("Command: ")
        isValid = False
        while not isValid:
            if userInput.lower() == "y":
                isValid = True
                found = False
                while not found:
                    userInput = input("What is the name of the card: ")
                    found, index = self.__Deck.searchDeckTitles(userInput)
                    if not found:
                        print("Your card was not found")
                        self.__SaveCard()
                    self.__playDeck.addCard(index)
            elif userInput.lower() == "n":
                isValid = True
                self.__TrimMenu()
            elif userInput.lower() == "x":
                isValid = True

    def __RemoveCard(self):
        # TODO
        pass
