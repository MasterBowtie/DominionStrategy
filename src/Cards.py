from KingdomCards import GAMEEDITIONS, KINGDOMCARDDECK, CARDTYPE


class Card:
    def __init__(self, id):
        if 0 <= id < len(KINGDOMCARDDECK):
            self.__id = id
        else:
            self.__id = None


    def getID(self):
        return self.__id

    def getElement(self):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id]


    def getTitle(self):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id][0]

    def getCost(self):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id][1].strip('[]')

    def getEdition(self):
        if self.__id is not None:
            return GAMEEDITIONS.index(self.getEditionName())

    def getEditionName(self):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id][3]

    def getType(self):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id][2].strip('[]')

    def __str__(self):
        if self.__id == None:
            return "Card does not exist"
        return self.getTitle() + " from " + self.getEditionName()

    def __repr__(self):
        if self.__id == None:
            return "Card does not exist"
        return self.getTitle() + " from " + self.getEditionName() + "\n\tCosts: " + self.getCost() + "\n\tType: " + self.getType()

    def __gt__(self, other):
        if self.__id is None:
            return False
        if other.getID() is None:
            return True
        if self.getTitle() > other.getTitle():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__id is None:
            return False
        if other.getID() is None:
            return True
        if self.getEdition() > other.getEdition():
            return True
        else:
            return False
