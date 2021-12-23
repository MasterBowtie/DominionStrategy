from KingdomCards import GAMEEDITIONS, KINGDOMCARDDECK, CARDTYPE, COST


class Card:
    def __init__(self, id):
        if 0 <= id < len(KINGDOMCARDDECK):
            self.__id = id
        else:
            self.__id = None


    def getID(self):
        return self.__id

    def get(self, index):
        if self.__id is not None:
            return KINGDOMCARDDECK[self.__id][index]


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
        return self.getTitle() + " from " + self.getEditionName() + "\n\tCost: " + self.getCost() + "\n\tType: " + self.getType() + "\n"

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
        selfIndex = -1
        otherIndex = -1
        for i in range(len(GAMEEDITIONS)):
            if self.getEditionName() == GAMEEDITIONS[i]:
                selfIndex = i
            if other.getEditionName() == GAMEEDITIONS[i]:
                otherIndex = i
        return selfIndex > otherIndex

    def __lt__(self, other):
        if self.__id is None:
            return False
        if other.getID() is None:
            return True
        selfIndex = -1
        otherIndex = -1
        for i in range(len(COST)):
            if COST[i] in self.getCost():
                selfIndex = i
            if COST[i] in other.getCost():
                otherIndex = i
        return selfIndex > otherIndex

    def __le__(self, other):
        if self.__id is None:
            return False
        if other.getID() is None:
            return True
        selfIndex = -1
        otherIndex = -1
        for i in range(len(CARDTYPE)):
            if CARDTYPE[i] in self.getCost():
                selfIndex = i
            if CARDTYPE[i] in other.getCost():
                otherIndex = i
        return selfIndex > otherIndex
