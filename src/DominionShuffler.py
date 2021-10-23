from Deck import Deck
from Cards import Card
from DominionDecks import KINGDOMCARDDECK, CARDTYPE, GAMEEDITIONS, COST
import random


class DominionShuffler:
    def __init__(self):
        self.__editionList = []
        self.__costList = []
        self.__typeList = []
        self.__playDeck = Deck(10)
        self.__shuffleDeck = Deck()

    def main(self):
        print("__________Welcome to the Dominion Shuffler__________")
        self.editionSelection()
        self.buildShuffleDeck()
        userInput = input("Would you like to customize your deck (Y/N)? ")
        if userInput.lower() == "y":
            self.customizing()
        self.buildDeck()

    def customizing(self):
        userInput = "Y"
        while userInput.lower() == "y":
            print("1) Save specific cards."
                  "\n2) remove specific cards. "
                  "\n3) Save cards of a certain cost."
                  "\n4) Save cards of a certain type."
                  "\n5) Save cards from a certain edition.")
            userInput = input("What would you like to do (0 to abort): ")
            if userInput.isdigit:
                if int(userInput) == 1:
                    self.saveCards()
                elif int(userInput) == 2:
                    self.removeCards()
                elif int(userInput) == 3:
                    self.costSave()
                elif int(userInput) == 4:
                    self.typeSave()
                elif int(userInput) == 5:
                    self.editionSave()
                elif int(userInput) == 0:
                    break
                else:
                    print("That is not an option")
                if self.__playDeck.getSlots() != 0:
                    userInput = input("Would you like to keep customizing (Y/N)?: ")

    ''' 
    Choosing the editions the user wants to play with
    '''

    def editionSelection(self):
        print("What editions are you playing with? (0 to end)")
        msg = "Dominion\n\t1.1) 1st Edition\n\t1.2) 2nd Edition"
        msg += "\n Intrigue\n\t2.1) 1st Edition\n\t2.2) 2nd Edition"
        msg += "\n3) Seaside"
        msg += "\n4) Alchemy"
        msg += "\n5) Prosperity"
        msg += "\n6) Cornucopia"
        msg += "\n7) Hinterlands"
        msg += "\n8) Dark Ages"
        msg += "\n9) Guilds"
        msg += "\n10) Adventures"
        msg += "\n11) Empires"
        msg += "\n12) Nocturne"
        msg += "\n13) Renaissance"
        msg += "\n14) Menagerie"
        print(msg)
        userInput = "-1"
        while userInput != "0" or len(self.__editionList) == 0:
            userInput = input("Edition: ")
            if userInput == "0" or userInput == "":
                print(end="")
            elif "1.1" in userInput or "1.2" in userInput:
                if "Dominion" not in self.__editionList and not (
                        "Dominion 1st Edition" in self.__editionList or "Dominion 2nd Edition" in self.__editionList):
                    self.__editionList.append("Dominion")
                if "1.2" in userInput and not "Dominion 2nd Edition" in self.__editionList:
                    self.__editionList.append("Dominion 2nd Edition")
                elif "1.1" in userInput and not "Dominion 1st Edition" in self.__editionList:
                    self.__editionList.append("Dominion 1st Edition")
            elif "2.1" in userInput or "2.2" in userInput:
                if "Intrigue" not in self.__editionList and not (
                        "Intrigue 1st Edition" in self.__editionList or "Intrigue 2nd Edition" in self.__editionList):
                    self.__editionList.append("Intrigue")
                if "2.2" in userInput and not "Intrigue 2nd Edition" in self.__editionList:
                    self.__editionList.append("Intrigue 2nd Edition")
                elif "2.1" in userInput and not "Intrigue 1st Edition" in self.__editionList:
                    self.__editionList.append("Intrigue 1st Edition")
            elif userInput.isdigit() and 2 < int(userInput) < 15:
                if not GAMEEDITIONS[int(userInput) + 3] in self.__editionList:
                    self.__editionList.append(GAMEEDITIONS[int(userInput) + 3])
            else:
                print("That is not an option. Number inputs only. 0 to end selection")

    ''' 
    Fix!!!
    
    Try and make 1st and 2nd editions include the Base sets?
    
    Exceptions!!!
    '''

    def editionSave(self):
        print(self.__editionList)
        userInput = "y"
        while userInput.lower() == "y":
            reserveDeck = []
            for i in range(len(self.__editionList)):
                print(str(i + 1) + ") " + self.__editionList[i])
            valid = False
            while not valid:
                userInput = input("What edition would you like to reserve from? ")
                if not userInput.isdigit:
                    print("Oops! That is not a number")
                else:
                    valid = True
            self.__shuffleDeck.searchDeckEdition(reserveDeck, self.__editionList[0])
            random.shuffle(reserveDeck)
            while valid:
                userInput = input("How many would you like to reserve? ")
                if userInput.isdigit:
                    if int(userInput) > int(self.__playDeck.getLimit() - self.__playDeck.getSize()):
                        print("Oops!")
                        print("That exceeds your card limit")
                    else:
                        valid = False
                else:
                    print("Oops! That is not a number")
            for i in range(int(userInput)):
                key = reserveDeck.pop()
                found, index = self.__shuffleDeck.searchDeckTitles(key.getTitle())
                if found:
                    self.__playDeck.addCard(self.__shuffleDeck.pull(index))
            if self.__playDeck.getSlots() > 0:
                userInput = input("Do you want to reserve more (Y/N)? ")

    ''' 
    Exceptions!!!
    '''

    def typeSave(self):
        valid = True
        userInput = "y"
        while userInput.lower() == "y":
            reserveDeck = []
            for i in range(6):
                print(str(i + 1) + ") " + str(CARDTYPE[i]))
            for i in range(len(self.__editionList)):
                if self.__editionList[i] == "Dark Ages":
                    print("7) Looter")
                if self.__editionList[i] == "Adventures":
                    print("8) Reserve\n9) Traveller")
                if self.__editionList[i] == "Empires":
                    print("10) Gathering")
                if self.__editionList[i] == "Nocturne":
                    print("11) Night\n12) Fate\n13) Doom")
            while valid:
                userInput = input("What type do you want to reserve? ")
                if userInput.isdigit():
                    valid = False
                else:
                    print()
            self.__shuffleDeck.searchDeckType(reserveDeck, int(userInput) - 1)
            random.shuffle(reserveDeck)
            while not valid:
                while not valid:
                    userInput = input("How many do you want to reserve? ")
                    if userInput.isdigit():
                        valid = True
                    else:
                        print()
                if int(userInput) > int(self.__playDeck.getLimit() - self.__playDeck.getSize()) == True:
                    print("That exceeds your play limit")
                    valid = False
            for i in range(int(userInput)):
                key = reserveDeck.pop()
                found, index = self.__shuffleDeck.searchDeckTitles(key.getTitle())
                if found:
                    self.__playDeck.addCard(self.__shuffleDeck.pull(index))
            if self.__playDeck.getSlots() > 0:
                userInput = input("Do you want to reserve more (Y/N)? ")

    ''' 
    Exceptions!!!
    '''

    def costSave(self):
        valid = True
        userInput = "y"
        while userInput.lower() == "y":
            reserveDeck = []
            while valid:
                userInput = input("What cost do you want to reserve (Potions = 0)? ")
                if userInput.isdigit() == False:
                    print("That is not a number")
                else:
                    self.__shuffleDeck.searchDeckCost(reserveDeck, int(userInput))
                    random.shuffle(reserveDeck)
                    valid = False
            while not valid:
                userInput = input("How many do you want to reserve? ")
                if userInput.isdigit():
                    if int(userInput) > (int(self.__playDeck.getLimit() - self.__playDeck.getSize())) == True:
                        print("That exceeds your play limit")
                    else:
                        valid = True
                        for i in range(int(userInput)):
                            key = reserveDeck.pop()
                            found, index = self.__shuffleDeck.searchDeckTitles(key.getTitle())
                            if found:
                                self.__playDeck.addCard(self.__shuffleDeck.pull(index))
            if self.__playDeck.getSlots() > 0:
                userInput = input("Do you want to reserve more (Y/N)? ")

    '''
    When all the customizing is done, the cards are chosen randomly
    '''

    def buildDeck(self):
        self.__shuffleDeck.shuffle()
        while self.__playDeck.getSize() < 10:
            self.__playDeck.addCard(self.__shuffleDeck.draw())
        self.__playDeck.sortTitle()
        self.__playDeck.sortEdition()
        print("\nYour Kingdom Cards for this game\n")
        self.__playDeck.printDeck()

    '''
    Removing cards from the shuffle deck
    '''

    def removeCards(self):
        userInput = "y"
        while userInput.lower() == "y":
            searchKey = input("Please type in the name of the card: ")
            found, index = self.__shuffleDeck.searchDeckTitles(searchKey)
            if found:
                self.__shuffleDeck.pull(index)
            userInput = input("Would you like to remove any more (Y/N)? ")

    '''
    Adding specific cards to the play Deck
    '''

    def saveCards(self):
        userInput = "y"
        while userInput.lower() == "y":
            userInput = input("Do you know the name of the card? (Y/N): ")
            if userInput.lower() == "y":
                found = False
                while not found:
                    searchKey = input("Please type in the name of the card (0 to abort): ")
                    if searchKey == "0":
                        break
                    found, index = self.__shuffleDeck.searchDeckTitles(searchKey)
                    if found:
                        self.__playDeck.addCard(self.__shuffleDeck.pull(index))
            else:
                index = self.searchDeck()
                self.__playDeck.addCard(self.__shuffleDeck.pull(index))

            if self.__playDeck.getSlots() > 0:
                print(self.__playDeck)
                userInput = input("Would you like to reserve any more (Y/N)? ")
            else:
                break

    '''
    Make section
    '''
    def searchDeck(self):
        currentList = []
        userInput = -1
        while userInput != "0":
            print("Do you know the,\n\t1)Edition\n\t2)Type\n\t3)Cost")
            userInput = input("answer (0 to abort): ")
            if userInput == "1":
                print("Available Editions:")
                count = 1
                for edition in self.__editionList:
                    print("\t" + str(count) + ") " + edition)
                    count += 1
                userInput = input("Edition: ")
                if userInput.isdigit() and (0 <= (int(userInput) - 1) < len(self.__editionList)):
                    if len(currentList) == 0:
                        for card in self.__shuffleDeck:
                            if card.getEdition() == self.__editionList[int(userInput) -1]:
                                currentList.append(card)
                    else:
                        for card in currentList:
                            if card.getEdition() != self.__editionList[int(userInput) - 1]:
                                currentList.remove(card)

            elif userInput == "2":
                print("Available Types")
                count = 1
                for type in self.__typeList:
                    print("\t" + str(count) + ") " + type)
                    count += 1
                userInput = input("Type: ")
                if userInput.isdigit() and (0 <= (int(userInput) - 1) < len(self.__typeList)):
                    if len(currentList) == 0:
                        for card in self.__shuffleDeck:
                            if self.__typeList[int(userInput) - 1] in card.getType():
                                currentList.append(card)
                    else:
                        i = 0
                        while i < len(currentList):
                            if self.__typeList[int(userInput) - 1] not in currentList[i].getType():
                                currentList.remove(currentList[i])
                            else:
                                i += 1

            elif userInput == "3":
                print("Available Cost")
                count = 1
                for cost in self.__costList:
                    print("\t" + str(count) + ") " + cost)
                    count += 1
                userInput = input("Cost: ")
                if userInput.isdigit() and (0 <= (int(userInput) - 1) < len(self.__costList)):
                    if len(currentList) == 0:
                        for card in self.__shuffleDeck:
                            if self.__costList[int(userInput) - 1] in card.getCost():
                                currentList.append(card)
                    else:
                        i = 0
                        while i < len(currentList):
                            if self.__costList[int(userInput) - 1] not in currentList[i].getCost():
                                currentList.remove(currentList[i])
                            else:
                                i += 1

            elif userInput == "0":
                break
            else:
                print("Not a valid answer, number inputs only.")
            print("Picked Cards")
            for card in currentList:
                print(repr(card))
            userInput = input("Would you like to continue to refine your search (Y/N)? ")
            if userInput.lower() == "n":
                userInput = input("Is your card in this list (Y/N)? ")
                if userInput.lower() == "y":
                    found = False
                    while not found:
                        userInput = input("Type the name of the card: ")
                        found, index = self.__shuffleDeck.searchDeckTitles(userInput)
                        if found:
                            return index
                elif userInput.lower() == "n":
                    currentList = []


    '''
    This takes all the editions the user chose and builds the shuffle deck
    Then goes through all cards and pulls out all costs and types of cards
    '''
    def buildShuffleDeck(self):
        for i in range(len(self.__editionList)):
            for j in range(len(KINGDOMCARDDECK)):
                if Card(j).getEditionName() == self.__editionList[i]:
                    self.__shuffleDeck.addCard(j)
            self.__shuffleDeck.sortTitle()

        tempList = []
        for card in self.__shuffleDeck:
            # print("1st Run:", card)
            for cost in COST:
                if cost in card.getCost() and cost not in tempList:
                    tempList.append(cost)
            for type in CARDTYPE:
                if type in card.getType() and type not in tempList:
                    tempList.append(type)

        for cost in COST:
            if cost in tempList:
                self.__costList.append(cost)
        for type in CARDTYPE:
            if type in tempList:
                self.__typeList.append(type)


    '''
    for card in self.__shuffleDeck:
        print("2nd run:", card)
    print("Cost list\n", self.__costList)
    print("Type List\n", self.__typeList)
    print("Done")
    '''


test = DominionShuffler()
test.main()
