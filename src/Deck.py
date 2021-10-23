from DominionDecks import KINGDOMCARDDECK
from Cards import Card
from random import shuffle
from modules.sortmodules import Sort

class Deck:
    def __init__(self, limit = len(KINGDOMCARDDECK)):
        self.__deck = []
        self.__limit = limit

    def getLimit(self):
        return self.__limit

    def getSlots(self):
        print("You have " + str(self.__limit - len(self.__deck)) + " cards left")
        return self.__limit - len(self.__deck)

    def getSize(self):
        return len(self.__deck)

    def addCard(self, index):
        if self.__limit == len(self.__deck):
            raise ExceedsLimit
        else:
            self.__deck.append(Card(index))

    def shuffle(self):
        shuffle(self.__deck)

    def sortTitle(self):
        for i in range(1, len(self.__deck)):
            currentElement = self.__deck[i]
            j = i - 1
            while j >= 0 and self.__deck[j] > currentElement:
                self.__deck[j + 1] = self.__deck[j]
                #print(self.__deck)
                j -= 1
            self.__deck[j + 1] = currentElement
            #print(self.__deck)
        return self.__deck

    def sortSet(self):
        for i in range(1, len(self.__deck)):
            currentElement = self.__deck[i]
            j = i - 1
            while j >= 0 and self.__deck[j] >= currentElement:
                self.__deck[j + 1] = self.__deck[j]
                #print(self.__deck)
                j -= 1
            self.__deck[j + 1] = currentElement
            #print(self.__deck)
        return self.__deck

    def searchDeckSet(self, deck, key):
        for i in range(len(self.__deck)):
            if self.__deck[i].getSet() == key:
                deck.append(self.__deck[i])

    def searchDeckCost(self, deck, key):
        for i in range(len(self.__deck)):
            #print(str(self.__deck[i].getCost()) + str(type(self.__deck[i].getCost())))
            if self.__deck[i].getCost() == key:
                deck.append(self.__deck[i])
            elif type(self.__deck[i].getCost()) is list:
                for j in range(len(self.__deck[i].getCost())):
                    if self.__deck[i].getCost()[j] == key:
                        deck.append(self.__deck[i])

    def searchDeckType(self, deck, key):
        for i in range(len(self.__deck)):
            #print(str(self.__deck[i].getCost()) + str(type(self.__deck[i].getCost())))
            if self.__deck[i].getType() == key:
                deck.append(self.__deck[i])
            elif type(self.__deck[i].getType()) is list:
                for j in range(len(self.__deck[i].getType())):
                    if self.__deck[i].getType()[j] == key:
                        deck.append(self.__deck[j])

    def searchDeckTitles(self, key):
        self.sortTitle()
        #self.printDeck()
        key = key.lower()
        #print(key)
        found = False
        low = 0
        high = len(self.__deck) - 1
        #print("Start Search")
        while found == False and low <= high:
            mid = (low + high) // 2
            #print(str(self.__deck[mid].getTitle().lower) + " vs " + str(key) + " " + str(self.__deck[mid].getTitle().lower() == key))
            #print("high " + self.__deck[high].getTitle().lower() + " low " + str(self.__deck[low].getTitle()).lower() + " mid " + self.__deck[mid].getTitle().lower())
            #print("high " + str(high) + " low " + str(low) + " mid " + str(mid))
            if self.__deck[mid].getTitle().lower() == key:
                found = True
                #print("Found")
                return found, mid
            elif key < self.__deck[mid].getTitle().lower():
                #print("Adjust low " + self.__deck[low].getTitle())
                high = mid - 1
            elif key > self.__deck[mid].getTitle().lower():
                #print("Adjust high " + self.__deck[high].getTitle())
                low = mid + 1
            else:
                print("Oops")
        print("Card not found")
        return found, mid

    def draw(self):
        return self.__deck.pop().getID()

    def pull(self, index):
        return self.__deck.pop(index).getID()

    def printDeck(self):
        for i in range(len(self.__deck)):
            print(self.__deck[i])

class ExceedsLimit(BaseException):
    def __init__(self):
        super().__init__()

def test():
    testDeck = Deck()
    for i in range(10):
        testDeck.addCard(i)
    hand = Deck(10)
    searchKey = input("Input ")
    found, index = testDeck.searchDeckTitles(searchKey)
    print(index)
    if found:
        hand.addCard(testDeck.pull(index))
    hand.printDeck()


#test()
