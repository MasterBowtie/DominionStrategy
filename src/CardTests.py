from Cards import Card
from Deck import Deck
import unittest

class CardTests(unittest.TestCase):
    def test_getID(self):
        for i in range(len(CardList)):
            self.assertEqual(TESTLISTID[i], CardList[i].getID(), "Card ID")


    def test_getEdition(self):
        self.assertEqual(CardList[0].getEdition(), 0, "getEdition: Moat: 0")
        self.assertEqual(CardList[2].getEdition(), 1, "getEdition: Chancellor: 1")
        self.assertEqual(CardList[1].getEdition(), 2, "getEdition: Bandit: 2")
        self.assertEqual(CardList[3].getEdition(), 3, "getEdition: Harem: 3")
        self.assertEqual(CardList[4].getEdition(), 4, "getEdition: Great Hall: 4")
        self.assertEqual(CardList[5].getEdition(), 5, "getEdition: Secret Passage: 5")
        self.assertEqual(CardList[6].getEdition(), 6, "getEdition: Caravan: 6")
        self.assertEqual(CardList[7].getEdition(), 7, "getEdition: Transmute: 7")
        self.assertEqual(CardList[10].getEdition(), 8, "getEdition: Scrying Pool: 8")
        self.assertEqual(CardList[11].getEdition(), 9, "getEdition: Jester: 9")
        self.assertEqual(CardList[12].getEdition(), 10, "getEdition: Fool's Gold: 10")
        self.assertEqual(CardList[13].getEdition(), 11, "getEdition: Knights: 11")
        self.assertEqual(CardList[16].getEdition(), 12, "getEdition: Soothsayer: 12")
        self.assertEqual(CardList[17].getEdition(), 13, "getEdition: Coin Of The Realm: 13")
        self.assertEqual(CardList[19].getEdition(), 14, "getEdition: Royal Blacksmith: 14")
        self.assertEqual(CardList[20].getEdition(), 15, "getEdition: Guardian: 15")
        self.assertEqual(CardList[25].getEdition(), 16, "getEdition: Research: 16")
        self.assertEqual(CardList[28].getEdition(), 17, "getEdition: Animal Fair: 17")

    def test_getCost(self):
        self.assertEqual(CardList[29].getCost(), 'One', "Poor House: One")
        self.assertEqual(CardList[0].getCost(), 'Two', "Moat: Two")
        self.assertEqual(CardList[2].getCost(), 'Three', "Chancellor: Three")
        self.assertEqual(CardList[1].getCost(), 'Four', "Bandit: Four")
        self.assertEqual(CardList[10].getCost(), 'Five', "City: Five")
        self.assertEqual(CardList[3].getCost(), 'Six', "Harem: Six")
        self.assertEqual(CardList[15].getCost(), 'Seven', "Expand: Seven")
        self.assertEqual(CardList[14].getCost(), 'Eight', "Peddler: Eight")
        self.assertEqual(CardList[7].getCost(), 'Potion', "Transmute: Potion")
        self.assertEqual(CardList[8].getCost(), 'Potion/Two', "Scrying Pool: Potion/Two")
        self.assertEqual(CardList[9].getCost(), 'Potion/Three', "Alchemist: Potion/Three")

    def test_getTitle(self):
        self.assertEqual(CardList[0].getTitle(), 'Moat', "Moat Title")

    def test_getEditionName(self):
        self.assertEqual(CardList[0].getEditionName(), "Dominion", "getEditionName: Moat: 0")
        self.assertEqual(CardList[2].getEditionName(), "Dominion 1st Edition", "getEditionName: Chancellor: 1")
        self.assertEqual(CardList[1].getEditionName(), "Dominion 2nd Edition", "getEditionName: Bandit: 2")
        self.assertEqual(CardList[3].getEditionName(), "Intrigue", "getEditionName: Harem: 3")
        self.assertEqual(CardList[4].getEditionName(), "Intrigue 1st Edition", "getEditionName: Great Hall: 4")
        self.assertEqual(CardList[5].getEditionName(), "Intrigue 2nd Edition", "getEditionName: Secret Passage: 5")
        self.assertEqual(CardList[6].getEditionName(), "Seaside", "getEditionName: Caravan: 6")
        self.assertEqual(CardList[7].getEditionName(), "Alchemy", "getEditionName: Transmute: 7")
        self.assertEqual(CardList[10].getEditionName(), "Prosperity", "getEditionName: Scrying Pool: 8")
        self.assertEqual(CardList[11].getEditionName(), "Cornucopia", "getEditionName: Jester: 9")
        self.assertEqual(CardList[12].getEditionName(), "Hinterlands", "getEditionName: Fool's Gold: 10")
        self.assertEqual(CardList[13].getEditionName(), "Dark Ages", "getEditionName: Knights: 11")
        self.assertEqual(CardList[16].getEditionName(), "Guilds", "getEditionName: Soothsayer: 12")
        self.assertEqual(CardList[17].getEditionName(), "Adventures", "getEditionName: Coin Of The Realm: 13")
        self.assertEqual(CardList[19].getEditionName(), "Empires", "getEditionName: Royal Blacksmith: 14")
        self.assertEqual(CardList[20].getEditionName(), "Nocturne", "getEditionName: Guardian: 15")
        self.assertEqual(CardList[25].getEditionName(), "Renaissance", "getEditionName: Research: 16")
        self.assertEqual(CardList[28].getEditionName(), "Menagerie", "getEditionName: Animal Fair: 17")

    def test_getType(self):
        self.assertEqual(CardList[2].getType(), "Action", "Chancellor: Action")
        self.assertEqual(CardList[0].getType(), "Reaction", "Moat: Reaction")
        self.assertEqual(CardList[1].getType(), "Attack", "Bandit: Attack")
        self.assertEqual(CardList[6].getType(), "Duration", "Caravan: Duration")
        self.assertEqual(CardList[3].getType(), "Victory/Treasure", "Harem: Victory/Treasure")

    def test_String(self):
        for i in TESTLISTID:
            testCard = Card(i)
            msg = f"{testCard.getTitle()} from {testCard.getEditionName()}"
            testmsg = testCard.__str__()
            self.assertEqual(testmsg, msg)

    def test_Repr(self):
        for i in TESTLISTID:
            testCard = Card(i)
            msg = f"{testCard.getTitle()} from {testCard.getEditionName()}\n\tCosts: {testCard.getCost()}\n\tType: {testCard.getType()}"
            testmsg = testCard.__repr__()
            self.assertEqual(testmsg, msg)



class DeckTests(unittest.TestCase):
    def test_getLimit(self):
        for i in range(10, 1000, 10):
            msg = f"Testing Deck Limit: {i}"
            testDeck = Deck(i)
            self.assertEqual(testDeck.getLimit(), i , msg)

    def test_getSlots(self):
        for i in range(10, 100, 10):
            testDeck = Deck(i)
            for j in range(10):
                msg = f"Testing Deck Slots: {i} - {j} = {i - j}"
                testDeck.addCard(j)
                self.assertEqual(testDeck.getSlots(), (i - (j + 1)), msg)



TESTLISTID = [3,    # 0['Moat', '[Two]', '[Reaction]', 'Dominion']
              23,   # 1['Bandit', '[Four]', '[Attack]', 'Dominion 2nd Edition']
              26,   # 2['Chancellor', '[Three]', '[Action]', 'Dominion 1st Edition']
              49,   # 3['Harem', '[Six]', '[Victory/Treasure]', 'Intrigue']
              52,   # 4['Great Hall', '[Three]', '[Action/Victory]', 'Intrigue 1st Edition']
              60,   # 5['Secret Passage', '[Three]', '[Action]', 'Intrigue 2nd Edition']
              74,   # 6['Caravan', '[Four]', '[Duration]', 'Seaside']
              89,   # 7['Transmute', '[Potion]', '[Action]', 'Alchemy']
              93,   # 8['Scrying Pool', '[Potion/Two]', '[Attack]', 'Alchemy']
              95,   # 9['Alchemist', '[Potion/Three]', '[Action]', 'Alchemy']
              109,  # 10['City', '[Five]', '[Action]', 'Prosperity']
              137,  # 11['Jester', '[Five]', '[Attack]', 'Cornucopia']
              141,  # 12["Fool's Gold", '[Two]', '[Reaction/Treasure]', 'Hinterlands']
              193,  # 13['Knights', '[Five]', '[Attack/Looter]', 'Dark Ages']
              125,  # 14['Peddler', '[Eight]', '[Action]', 'Prosperity']
              122,  # 15['Expand', '[Seven]', '[Action]', 'Prosperity']
              212,  # 16['Soothsayer', '[Five]', '[Attack]', 'Guilds']
              213,  # 17['Coin Of The Realm', '[Two]', '[Treasure/Reserve]', 'Adventures']
              214,  # 18['Page', '[Two]', '[Traveller]', 'Adventures']
              246,  # 19['Royal Blacksmith', '[Eight]', '[Action]', 'Empires']
              274,  # 20['Guardian', '[Two]', '[Duration/Night]', 'Nocturne']
              276,  # 21['Pixie', '[Two]', '[Fate]', 'Nocturne']
              281,  # 22['Leprechaun', '[Three]', '[Doom]', 'Nocturne']
              262,  # 23['Temple', '[Four]', '[Gathering]', 'Empires']
              297,  # 24['Idol', '[Five]', '[Attack/Treasure/Fate]', 'Nocturne']
              318,  # 25['Research', '[Four]', '[Duration]', 'Renaissance']
              133,  # 26['Young Witch', '[Four]', '[Attack]', 'Cornucopia']
              357,  # 27['Destrier', '[Six]', '[Action]', 'Menagerie']
              359,  # 28['Animal Fair', '[Seven]', '[Action]', 'Menagerie']
              165]  # 29['Poor House', '[One]', '[Action]', 'Dark Ages']

CardList = []
for i in TESTLISTID:
    CardList.append(Card(i))