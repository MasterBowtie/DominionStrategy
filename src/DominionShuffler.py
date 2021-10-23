from Deck import Deck, ExceedsLimit
from Cards import Card
from DominionDecks import KINGDOMCARDDECK, CARDTYPE, GAMEEDITIONS
import random


def test():
    editionList = [1.2, 2.2, 6, 9, 10]
    shuffleDeck = Deck()
    buildShuffleDeck(shuffleDeck, editionList)
    playDeck = Deck(10)
    typeSave(shuffleDeck, playDeck, editionList)
    buildDeck(shuffleDeck, playDeck)


def main():
    print("__________Welcome to the Dominion Shuffler__________")
    editionList = []
    editionSelection(editionList)
    shuffleDeck = Deck()
    buildShuffleDeck(shuffleDeck, editionList)
    playDeck = Deck(10)
    userInput = input("Would you like to customize your deck (Y/N)? ")
    if userInput.lower() == "y":
        valid = False
        while userInput.lower() == "y":
            print("1) Remove specific cards.\n2) Save specific cards. \n3) Save cards of a certain cost.\n4) Save cards of a certain type."
                  "\n5) Save cards from a certain set.")
            while not valid:
                userInput = input("What would you like to do: ")
                if userInput.isdigit:
                    if eval(userInput) == 1:
                        removeCards(shuffleDeck, playDeck)
                        valid = True
                    elif eval(userInput) == 2:
                        saveCards(shuffleDeck, playDeck)
                        valid = True
                    elif eval(userInput) == 3:
                        costSave(shuffleDeck, playDeck)
                        valid = True
                    elif eval(userInput) == 4:
                        typeSave(shuffleDeck, playDeck, editionList)
                        valid = True
                    elif eval(userInput) == 5:
                        setSave(shuffleDeck, playDeck, editionList)
                        valid = True
                    else:
                        print("That is not an option")
                else:
                    print("That is not a number")
            if playDeck.getSlots() != 0:
                userInput = input("Would you like to keep customizing (Y/N)?: ")
                valid = False
    buildDeck(shuffleDeck, playDeck)


def editionSelection(editionList):
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
    while eval(userInput) != 0:
        userInput = input("Edition: ")
        if userInput.isdigit:
            if eval(userInput) == 0:
                print(end="")
            elif eval(userInput) > 0 and eval(userInput) < 15:
                editionList.append(eval(userInput))
            else:
                print("That is not an option")
        else:
            print("Oops! That is not a number")
            userInput = "-1"


def setSave(shuffleDeck, playDeck, editions):
    userInput = "y"
    while userInput.lower() == "y":
        reserveDeck = []
        for i in range(len(editions)):
            if editions[i] == 1.1 or editions[i] == 1.2:
                print("1) Dominion")
                if editions[i] == 1.1:
                    print("\t1.1) Dominion 1st Edition")
                if editions[i] == 1.2:
                    print("\t1.2) 2nd Edition")
            elif editions[i] == 2.1 or editions[i] == 2.2:
                print("2) Intrigue")
                if editions[i] == 2.1:
                    print("\t2.1) 2nd Edition")
                if editions[i] == 2.2:
                    print("\t2.2) 2nd Edition")
            else:
                print(str(editions[i]) + ") " + str(GAMEEDITIONS[int(editions[i] - 1)]))
        valid = False
        while not valid:
            userInput = input("What set would you like to reserve from? ")
            if not userInput.isdigit:
                print("Oops! That is not a number")
            else:
                valid = True
        shuffleDeck.searchDeckSet(reserveDeck, eval(userInput))
        random.shuffle(reserveDeck)
        while valid:
            userInput = input("How many would you like to reserve? ")
            if userInput.isdigit:
                if eval(userInput) > int(playDeck.getLimit() - playDeck.getSize()):
                    print("Oops!")
                    print("That exceeds your card limit")
                else:
                    valid = False
            else:
                print("Oops! That is not a number")
        for i in range(eval(userInput)):
            key = reserveDeck.pop()
            found, index = shuffleDeck.searchDeckTitles(key.getTitle())
            if found:
                playDeck.addCard(shuffleDeck.pull(index))
        if playDeck.getSlots() > 0:
            userInput = input("Do you want to reserve more (Y/N)? ")


def typeSave(shuffleDeck, playDeck, editions):
    valid = True
    userInput = "y"
    while userInput.lower() == "y":
        reserveDeck = []
        for i in range(6):
            print(str(i + 1) + ") " + str(CARDTYPE[i]))
        for i in range(len(editions)):
            if editions[i] == 8:
                print("8) Looter")
            if editions[i] == 10:
                print("7) Reserve\n9) Traveller")
            if editions[i] == 11:
                print("10) Gathering")
            if editions[i] == 12:
                print("11) Night\n12) Fate\n13) Doom")
        while valid:
            userInput = input("What type do you want to reserve? ")
            if userInput.isdigit():
                valid = False
            else:
                print()
        shuffleDeck.searchDeckType(reserveDeck, eval(userInput))
        random.shuffle(reserveDeck)
        while not valid:
            while not valid:
                userInput = input("How many do you want to reserve? ")
                if userInput.isdigit():
                    valid = True
                else:
                    print()
            if eval(userInput) > int(playDeck.getLimit() - playDeck.getSize()) == True:
                print("That exceeds your play limit")
                valid = False
        for i in range(eval(userInput)):
            key = reserveDeck.pop()
            found, index = shuffleDeck.searchDeckTitles(key.getTitle())
            if found:
                playDeck.addCard(shuffleDeck.pull(index))
        if playDeck.getSlots() > 0:
            userInput = input("Do you want to reserve more (Y/N)? ")


def costSave(shuffleDeck, playDeck):
    valid = True
    userInput = "y"
    while userInput.lower() == "y":
        reserveDeck = []
        while valid:
            userInput = input("What cost do you want to reserve? ")
            if userInput.isdigit() == False:
                print("That is not a number")
            else:
                shuffleDeck.searchDeckCost(reserveDeck, eval(userInput))
                random.shuffle(reserveDeck)
                valid = False
        while not valid:
            userInput = input("How many do you want to reserve? ")
            if userInput.isdigit():
                if eval(userInput) > (int(playDeck.getLimit() - playDeck.getSize())) == True:
                    print("That exceeds your play limit")
                else:
                    valid = True
                    for i in range(eval(userInput)):
                        key = reserveDeck.pop()
                        found, index = shuffleDeck.searchDeckTitles(key.getTitle())
                        if found:
                            playDeck.addCard(shuffleDeck.pull(index))
        if playDeck.getSlots() > 0:
            userInput = input("Do you want to reserve more (Y/N)? ")


def buildDeck(shuffleDeck, playDeck):
    shuffleDeck.shuffle()
    while playDeck.getSize() < 10:
        playDeck.addCard(shuffleDeck.draw())
    playDeck.sortSet()
    print("\nYour Kingdom Cards for this game\n")
    playDeck.printDeck()

def removeCards(shuffleDeck, playDeck):
    userInput = "y"
    while userInput.lower() == "y":
        searchKey = input("Please type in the name of the card: ")
        found, index = shuffleDeck.searchDeckTitles(searchKey)
        if found:
            shuffleDeck.pull(index)
        userInput = input("Would you like to remove any more (Y/N)? ")

def saveCards(shuffleDeck, playDeck):
    userInput = "y"
    while userInput.lower() == "y":
        searchKey = input("Please type in the name of the card: ")
        found, index = shuffleDeck.searchDeckTitles(searchKey)
        if found:
            playDeck.addCard(shuffleDeck.pull(index))
        if playDeck.getSlots() > 0:
            userInput = input("Would you like to reserve any more (Y/N)? ")
    


def buildShuffleDeck(deck, editions):
    for i in range(len(editions)):
        if editions[i] == 1.1 or editions[i] == 1.2:
            for k in range(len(KINGDOMCARDDECK)):
                if Card(k).getSet() == 1:
                    deck.addCard(k)
        if editions[i] == 2.1 or editions[i] == 2.2:
            for k in range(len(KINGDOMCARDDECK)):
                if Card(k).getSet() == 2:
                    deck.addCard(k)
        for j in range(len(KINGDOMCARDDECK)):
            if Card(j).getSet() == editions[i]:
                deck.addCard(j)


#test()
main()
