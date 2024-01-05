import pygame
from src.Deck import Deck
from src.Menu import Menu
from src.menu.main_menu import main_menu
from src.menu.select import selection_menu


class UserInterface:
    def __init__(self):
        self.__Deck = Deck()
        self.__playDeck = Deck(10)
        self.__trimDeck = Deck()
        self.__attributeList = ["Title", [], [], []]

    def run(self):
        pygame.init()
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        pygame.display.set_mode((width * .75, height * .75), pygame.RESIZABLE) #To be determined

        running = True
        next_menu = 0
        b_ratio = .35

        while (running):
            if next_menu == -1:
                running = False
            elif next_menu == 0:
                next_menu = main_menu(b_ratio)
            elif next_menu == 1:
                next_menu = selection_menu(b_ratio)


    # menu = Menu.EditionMenu()
        # menu.show()
        # keepGoing = True
        # editionList = []
        # while keepGoing:
        #     userInput = input("Command: ")
        #     if userInput.upper() == "X":
        #         keepGoing = False
        #     elif userInput == "1.1" or userInput == "1.2":
        #         if "Dominion" not in editionList and not (
        #                 "Dominion 1st Edition" in editionList or "Dominion 2nd Edition" in editionList):
        #             editionList.append("Dominion")
        #         if userInput == "1.2" and not "Dominion 2nd Edition" in editionList:
        #             editionList.append("Dominion 2nd Edition")
        #         elif userInput == "1.1" and not "Dominion 1st Edition" in editionList:
        #             editionList.append("Dominion 1st Edition")
        #     elif userInput == "2.1" or userInput == "2.2":
        #         if "Intrigue" not in editionList and not (
        #                 "Intrigue 1st Edition" in editionList or "Intrigue 2nd Edition" in editionList):
        #             editionList.append("Intrigue")
        #         if userInput == "2.2" and not "Intrigue 2nd Edition" in editionList:
        #             editionList.append("Intrigue 2nd Edition")
        #         elif userInput == "2.1" and not "Intrigue 1st Edition" in editionList:
        #             editionList.append("Intrigue 1st Edition")
        #     elif userInput.isdigit() and 2 < int(userInput) < 15:
        #         if not KingdomCards.GAMEEDITIONS[int(userInput) + 3] in editionList:
        #             editionList.append(KingdomCards.GAMEEDITIONS[int(userInput) + 3])
        #     elif userInput.upper() == "D":
        #         self.__BuildDeck(editionList)
        #         self.__EditDeck()
        #         menu.show()
        #     elif userInput.upper() == "R":
        #         editionList = []
        #     elif userInput.upper() == "P":
        #         print("Your current selection:")
        #         for i in editionList:
        #             print("\t" + i)
        #     else:
        #         print("Invalid input")


    def __BuildDeck(self, editionList):
        for i in range(len(editionList)):
            for j in range(len(KingdomCards.KINGDOMCARDDECK)):
                if Cards.Card(j).getEditionName() == editionList[i]:
                    self.__Deck.addCard(Cards.Card(j))
        for card in self.__Deck:
            for cost in KingdomCards.COST:
                if card.getCost() == cost and cost not in self.__attributeList[1]:
                    self.__attributeList[1].append(cost)
            for type in KingdomCards.CARDTYPE:
                if card.getType() == type and type not in self.__attributeList[2]:
                    self.__attributeList[2].append(type)
            for edition in KingdomCards.GAMEEDITIONS:
                if card.getEditionName() == edition and edition not in self.__attributeList[3]:
                    self.__attributeList[3].append(edition)

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
            if self.__playDeck.getSlots() == 0:
                self.__DrawDeck()
            userInput = menu.show()
            if userInput == "D":
                self.__DrawDeck()
            elif userInput == "S":
                self.__SaveCard()
            elif userInput == "P":
                print("Your current selection: ", end="")
                self.__playDeck.printDeck()
            elif userInput == "X":
                keepGoing = False
            elif userInput == "R":
                self.__RemoveCard()
            elif userInput == "E":
                self.__Trim(3)
                self.__drawTrim()
                self.__ClearTrim()
            elif userInput == "C":
                self.__Trim(1)
                self.__drawTrim()
                self.__ClearTrim()
            elif userInput == "T":
                self.__Trim(2)
                self.__drawTrim()
                self.__ClearTrim()
            elif userInput == "M":
                self.__TrimMenu()
                self.__ClearTrim()


    def __ClearTrim(self):
        self.__trimDeck.clearDeck()

    def __DrawDeck(self):
        self.__Deck.shuffle()
        while self.__playDeck.getSize() < 10:
            self.__playDeck.addCard(self.__Deck.draw())
        print("\nThe cards you are playing with")
        self.__playDeck.sortTitle()
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
                self.__Trim(1)
            elif userInput == "T":
                self.__Trim(2)
            elif userInput == "E":
                self.__Trim(3)
            elif userInput == "D":
                self.__drawTrim()
            elif userInput == "P":
                self.__trimDeck.printDeck()
            elif userInput == "R":
                self.__ClearTrim()
            elif userInput == "X":
                keepGoing = False

    def __drawTrim(self):
        keepGoing = True
        self.__trimDeck.shuffle()
        while keepGoing:
            userInput = input(f"How many do you want to draw ({self.__trimDeck.getSize()}): ")
            if userInput.isdigit() and int(userInput) <= self.__trimDeck.getSize() and int(userInput) <= self.__playDeck.getSlots():
                keepGoing = False
                for i in range(int(userInput)):
                    card = self.__trimDeck.draw().getTitle()
                    found, index = self.__Deck.searchDeck(card, 0)
                    self.__playDeck.addCard(self.__Deck.pull(index))
            else:
                print("That is not a valid input")


    def __Trim(self, index):
        menu = Menu.Menu("Edition")
        for i in range(len(self.__attributeList[index])):
            menu.addOption(str(i + 1), self.__attributeList[index][i])
        menu.addOption("X", "Return to previous menu")

        keepGoing = True

        while keepGoing:
            userInput = menu.show()
            if userInput == "X":
                keepGoing = False
            for i in range(len(self.__attributeList[index])):
                if userInput == menu.getOption(i).getCommand():
                    keepGoing = False
                    found, location = self.__trimDeck.searchDeck(menu.getOption(i).getDescription(), index)
                    if self.__trimDeck.getSize() == 0:
                        for card in self.__Deck:
                            if menu.getOption(i).getDescription() in card.get(index):
                                self.__trimDeck.addCard(card)
                    elif found:
                        trimDeck = []
                        for card in self.__trimDeck:
                            if (index == 3 or index == 0) and menu.getOption(i).getDescription() == card.get(index):
                                trimDeck.append(card)
                            elif (index == 2 or index == 1) and menu.getOption(i).getDescription() in card.get(index):
                                trimDeck.append(card)
                        self.__ClearTrim()
                        for card in trimDeck:
                            self.__trimDeck.addCard(card)
                    else:
                        for card in self.__Deck:
                            if menu.getOption(i).getDescription() in card.get(index):
                                self.__trimDeck.addCard(card)

    def __SaveCard(self):
        isValid = False
        while not isValid:
            print("Do you know the name of the Card (Y/N)?")
            userInput = input("Command: ")
            if userInput.upper() == "Y":
                found = False
                while not found:
                    userInput = input("What is the name of the card: ")
                    found, index = self.__Deck.searchDeck(userInput, 0)
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
                    found, index = self.__Deck.searchDeck(userInput, 0)
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

