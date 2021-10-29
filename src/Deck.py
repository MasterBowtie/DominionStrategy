from KingdomCards import KINGDOMCARDDECK, COST , CARDTYPE, GAMEEDITIONS
from Cards import Card
from random import shuffle


class Deck:
    def __init__(self, limit=None):
        self.__deck = []
        self.__limit = limit
        self.__index = 0

    def getLimit(self):
        return self.__limit

    def getSlots(self):
        if self.__limit == None:
            return None
        # print("You have " + str(self.__limit - len(self.__deck)) + " cards left")
        else:
            return self.__limit - len(self.__deck)

    def getSize(self):
        return len(self.__deck)

    def addCard(self, index):
        if 0 <= index < len(KINGDOMCARDDECK):
            self.__deck.append(Card(index))
            return True
        else:
            return False

    def shuffle(self):
        shuffle(self.__deck)

    def sortTitle(self):
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False

            for i in range(len(self.__deck) - sortCount):
                if self.__deck[i] > self.__deck[i + 1]:
                    self.__deck[i], self.__deck[i + 1] = self.__deck[i + 1], self.__deck[i]
                    didSwap = True
            sortCount += 1

    def sortEdition(self):
        self.sortTitle()
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False

            for i in range(len(self.__deck) - sortCount):
                if self.__deck[i] >= self.__deck[i + 1]:
                    self.__deck[i], self.__deck[i + 1] = self.__deck[i + 1], self.__deck[i]
                    didSwap = True
            sortCount += 1

    def searchDeckEdition(self, deck, key):
        for i in range(len(self.__deck)):
            if key in self.__deck[i].getEditionName():
                deck.append(self.__deck[i])

    def searchDeckCost(self, deck, key):
        for i in range(len(self.__deck)):
            if self.__deck[i].getCost().find(COST[key]):
                deck.append(self.__deck[i])

    def searchDeckType(self, deck, key):
        for i in range(len(self.__deck)):
            if self.__deck[i].getType().find(CARDTYPE[key]):
                deck.append(self.__deck[i])


    def searchDeckTitles(self, key):
        self.sortTitle()
        key = key.lower()
        found = False
        low = 0
        high = len(self.__deck) - 1
        while found == False and low <= high:
            mid = (low + high) // 2
            if self.__deck[mid].getTitle().lower() == key:
                found = True
                return found, mid
            elif key < self.__deck[mid].getTitle().lower():
                high = mid - 1
            elif key > self.__deck[mid].getTitle().lower():
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
        for card in self.__deck:
            print(card)

    def __str__(self):
        msg = ""
        for card in self.__deck:
            msg += repr(card)
        return msg

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__deck):
            item = self.__deck[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration
