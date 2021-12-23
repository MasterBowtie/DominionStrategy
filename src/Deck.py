import sys

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

    def addCard(self, card):
        if type(card) == Card:
            self.__deck.append(card)
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

    def sortCost(self):
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False

            for i in range(len(self.__deck) - sortCount):
                if self.__deck[i] < self.__deck[i + 1]:
                    self.__deck[i], self.__deck[i + 1] = self.__deck[i + 1], self.__deck[i]
                    didSwap = True
            sortCount += 1

    def sortType(self):
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False

            for i in range(len(self.__deck) - sortCount):
                if self.__deck[i] <= self.__deck[i + 1]:
                    self.__deck[i], self.__deck[i + 1] = self.__deck[i + 1], self.__deck[i]
                    didSwap = True
            sortCount += 1

    def sortEdition(self):
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False

            for i in range(len(self.__deck) - sortCount):
                if self.__deck[i] >= self.__deck[i + 1]:
                    self.__deck[i], self.__deck[i + 1] = self.__deck[i + 1], self.__deck[i]
                    didSwap = True
            sortCount += 1

    def sort(self, index):
        if index == 0:
            self.sortTitle()
        elif index == 1:
            self.sortCost()
        elif index == 2:
            self.sortType()
        elif index == 3:
            self.sortEdition()

    def searchDeck(self, key, index):
        found = False
        location = -1
        if (index == 0 or index == 3):
            for i in range(len(self.__deck)):
                if self.__deck[i].get(index) == key:
                    found = True
                    location = i
        else:
            for i in range(len(self.__deck)):
                if key in self.__deck[i].get(index):
                    found = True
                    location = i
        if location == -1 and index == 0:
            print("Card not found")
        return found, location

    def draw(self):
        return self.__deck.pop()

    def pull(self, index):
        if 0 <= index < len(self.__deck):
            return self.__deck.pop(index)

    def clearDeck(self):
        self.__deck = []

    def printDeck(self, file=sys.stdout):
        msg = ""
        for card in self.__deck:
            msg += str(card) + "\n"
        print("\n" + msg, file=file)
        return msg

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
