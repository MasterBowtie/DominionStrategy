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
            if userInput == "D":
                self.__DrawDeck()
            elif userInput == "S":
                self.__SaveCard()
            elif userInput == "P":
                print("Your current selection: ")
                self.__playDeck.printDeck()
            elif userInput == "X":
                keepGoing = False
            elif userInput == "R":
                self.__RemoveCard()
            elif userInput == "E":
                self.__TrimEdition()
                self.__DrawTrim()
                self.__ClearTrim()
            elif userInput == "C":
                self.__TrimCost()
                self.__DrawTrim()
                self.__ClearTrim()
            elif userInput == "T":
                self.__TrimType()
                self.__DrawTrim()
                self.__ClearTrim()
            elif userInput == "M":
                self.__TrimMenu()
                self.__DrawTrim()
                self.__ClearTrim()


    def __ClearTrim(self):
        for i in range(self.__trimDeck.getSize()):
            self.__playDeck.addCard(self.__trimDeck.draw())
            i -= 1

    def __DrawDeck(self):
        # TODO
        self.__Deck.shuffle()
        print(self.__playDeck.getLimit())
        while self.__playDeck.getSize() < 10:
            self.__playDeck.addCard(self.__Deck.draw())
        print("\nThe cards you are playing with\n")
        self.__playDeck.sortEdition()
        self.__playDeck.printDeck()
        exit()

    def __TrimMenu(self):
        print("Welcome to the Trim Menu")
        menu = Menu.Menu("Trim")
        menu.addOption("C", "Cost")
        menu.addOption("T", "Type")
        menu.addOption("E", "Edition")
        menu.addOption("D", "Draw from selection")
        menu.addOption("P", "Print current selection")
        menu.addOption("R", "Clear current Selection")
        menu.addOption("X", "Return to previous menu")

        keepGoing = True

        while keepGoing:
            userInput = menu.show()
            if userInput == "C":
                self.__TrimCost()
            elif userInput == "T":
                self.__TrimType()
            elif userInput == "E":
                self.__TrimEdition()
            elif userInput == "D":
                self.__drawTrim()
            elif userInput == "P":
                self.__trimDeck.printDeck()
            elif userInput == "R":
                self.__ClearTrim()
            elif userInput == "X":
                keepGoing = False

    def __DrawTrim(self):
        # TODO
        keepGoing = True
        self.__trimDeck.shuffle()
        while keepGoing:
            userInput = input("How many do you want to draw: ")
            if userInput.isdigit():
                keepGoing = False
                for i in range(int(userInput)):
                    self.__playDeck.addCard(self.__trimDeck.draw())


    def __TrimEdition(self):
        print()
        menu = Menu.Menu("Edition")
        for i in range(len(self.__editionList)):
            menu.addOption(str(i + 1), self.__editionList[i])
        menu.addOption("X", "Return to previous menu")

        keepGoing = True

        while keepGoing:
            userInput = menu.show()
            if userInput == "X":
                keepGoing = False
            for i in range(len(self.__editionList)):
                if userInput == menu.getOption(i).getCommand():
                    keepGoing = False
                    for card in self.__Deck:
                        if card.getEditionName() == menu.getOption(i).getDescription():
                            self.__trimDeck.addCard(card.getID())

    def __TrimCost(self):
        # TODO
        pass

    def __TrimType(self):
        # TODO
        pass

    def __SaveCard(self):
        isValid = False
        while not isValid:
            print("Do you know the name of the Card (Y/N)?")
            userInput = input("Command: ")
            if userInput.upper() == "Y":
                found = False
                while not found:
                    userInput = input("What is the name of the card: ")
                    found, index = self.__Deck.searchDeckTitles(userInput)
                    if not found:
                        print("Your card was not found")
                        break
                    isValid = True
                    self.__playDeck.addCard(index)
                    print("\tYour card has been added")
            elif userInput.upper() == "N":
                self.__TrimMenu()
            elif userInput.upper() == "X":
                isValid = True

    def __RemoveCard(self):
        isValid = False
        while not isValid:
            print("Do you know the name of the Card (Y/N)?")
            userInput = input("Command: ")
            if userInput.upper() == "Y":
                found = False
                while not found:
                    userInput = input("What is the name of the card: ")
                    found, index = self.__Deck.searchDeckTitles(userInput)
                    if not found:
                        print("Your card was not found")
                        break
                    isValid = True
                    self.__Deck.pull(index)
                    print("\tThat card has been removed")
            elif userInput.upper() == "N":
                self.__TrimMenu()
            elif userInput.upper == "X":
                isValid = True

