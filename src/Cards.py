from KingdomCards import GAMEEDITIONS, KINGDOMCARDDECK, CARDTYPE


class Card:
    def __init__(self, id):
        self.__id = id

    def getID(self):
        return self.__id

    def getTitle(self):
        return str(KINGDOMCARDDECK[self.__id][0])

    def getCost(self):
        return KINGDOMCARDDECK[self.__id][1]

    def getEdition(self):
        return KINGDOMCARDDECK[self.__id].index(self.getEditionName())

    def getEditionName(self):
        return KINGDOMCARDDECK[self.__id][3]

    def getType(self):
        return KINGDOMCARDDECK[self.__id][2]

    def __str__(self):
        return str(self.getTitle()) + " from " + str(self.getEditionName())

    def __repr__(self):
        return str(self.getTitle()) + " from " + str(self.getEditionName()) + "\n\tCosts: " + self.getCost() + "\n\tType: " + self.getType()

    def __gt__(self, other):
        if self.getTitle() > other.getTitle():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.getEdition() > other.getEdition():
            return True
        else:
            return False
