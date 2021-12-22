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
        self.sortTitle()
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
        self.sortTitle()
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

    def sort(self, index):
        if index == 0:
            self.sortTitle()
        elif index == 1:
            self.sortCost()
        elif index == 2:
            self.sortType()
        elif index == 3:
            self.sortEdition()

    #TODO: Check Edition Searching
    def searchDeck(self, key, index):
        self.sort(index)
        found = False
        low = 0
        high = len(self.__deck) - 1
        while found == False and low <= high:
            mid = (low + high) // 2
            if index == 3 and key == self.__deck[mid].get(index):
                found = True
                return found, mid
            elif index != 3 and key in self.__deck[mid].get(index):
                found = True
                return found, mid
            elif key < self.__deck[mid].get(index):
                high = mid - 1
            elif key > self.__deck[mid].get(index):
                low = mid + 1
            else:
                print("Oops")
        print("Card not found")
        mid = -1
        return found, mid

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
