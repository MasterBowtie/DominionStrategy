from DominionDecks import GAMEEDITIONS, KINGDOMCARDDECK, CARDTYPE

class Card:
    def __init__(self, id):
        self.__id = id

    def getID(self):
        return self.__id

    def getTitle(self):
        return KINGDOMCARDDECK[self.__id][0]

    def getCost(self):
        return KINGDOMCARDDECK[self.__id][1]

    def getSet(self):
        return KINGDOMCARDDECK[self.__id][3]

    def getSetName(self):
        try:
            if KINGDOMCARDDECK[self.__id][3] == 1:
                return GAMEEDITIONS[0][0]
            elif KINGDOMCARDDECK[self.__id][3] == 1.1:
                return GAMEEDITIONS[0][0] + " " + GAMEEDITIONS[0][1]
            elif KINGDOMCARDDECK[self.__id][3] == 1.2:
                return GAMEEDITIONS[0][0] + " " + GAMEEDITIONS[0][2]
            elif KINGDOMCARDDECK[self.__id][3] == 2:
                return GAMEEDITIONS[1][0]
            elif KINGDOMCARDDECK[self.__id][3] == 2.1:
                return GAMEEDITIONS[1][0] + " " + GAMEEDITIONS[1][1]
            elif KINGDOMCARDDECK[self.__id][3] == 2.2:
                return GAMEEDITIONS[1][0] + " " + GAMEEDITIONS[1][2]
            else:
                return GAMEEDITIONS[(KINGDOMCARDDECK[self.__id][3]) - 1]
        except():
            return "Not Available"


    def getType(self):
            return KINGDOMCARDDECK[self.__id][2]


    def __str__(self):
        return str(self.getTitle()) + " from " + str(self.getSetName())

    def __repr__(self):
        return str(self.getTitle()) + " from " + str(self.getSetName())

    def __gt__(self, other):
        if self.getTitle() > other.getTitle():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.getSet() > other.getSet():
            return True
        else:
            return False

    def __add__(self, other):
        if self.getCost() > other.getCost():
            return True
        else:
            return False

    def __sub__(self, other):
        if self.getType() > other.getType():
            return True
        else:
            return False