from Cards import Card
from Deck import Deck
import KingdomCards
import unittest

class CardTests(unittest.TestCase):
    def test_getID(self):
        for i in range(len(CardList) - 2):
            self.assertEqual(TESTLISTID[i], CardList[i].getID(), "Card ID")
        self.assertEqual(CardList[-1].getID(), None, "Test invalid Card")
        self.assertEqual(CardList[-2].getID(), None, "Test invalid Card")


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
            if testCard.getID() is None:
                self.assertEqual(testCard.__repr__(), "Card does not exist", "Invalid Card")
            else:
                msg = f"{testCard.getTitle()} from {testCard.getEditionName()}"
                testmsg = testCard.__str__()
                self.assertEqual(testmsg, msg)

    def test_Repr(self):
        for i in TESTLISTID:
            testCard = Card(i)
            if testCard.getID() is None:
                self.assertEqual(testCard.__repr__(), "Card does not exist", "Invalid Card")
            else:
                msg = f"{testCard.getTitle()} from {testCard.getEditionName()}\n\tCost: {testCard.getCost()}\n\tType: {testCard.getType()}\n"
                testmsg = testCard.__repr__()
                self.assertEqual(testmsg, msg)

    def test_GreaterThan(self):
        testCard1 = Card(3)
        testCard2 = Card(49)
        testCard3 = Card(23)
        testCard4 = Card(400)
        testCard5 = Card(-1)
        self.assertGreater(testCard1, testCard2, "Moat > Harem")
        self.assertGreater(testCard1, testCard2, "Moat > Bandit")
        self.assertGreater(testCard2, testCard3, "Harem > Bandit")
        self.assertGreater(testCard1, testCard4, "Moat > None")
        self.assertGreater(testCard1, testCard5, "Moat > None")

    def test_GreaterEqualTo(self):
        testCard1 = Card(3)
        testCard2 = Card(49)
        testCard3 = Card(23)
        testCard4 = Card(400)
        testCard5 = Card(-1)
        self.assertGreaterEqual(testCard2, testCard1, "Intrigue > Dominion")
        self.assertGreaterEqual(testCard3, testCard1, "Dominion 2nd > Dominion")
        self.assertGreaterEqual(testCard2, testCard3, "Intrigue > Dominion 2nd")
        self.assertGreaterEqual(testCard1, testCard4, "Dominion > None")
        self.assertGreaterEqual(testCard1, testCard5, "Dominion > None")


class DeckTests(unittest.TestCase):
    def test_getLimit(self):
        for i in range(10, 1000, 10):
            msg = f"Testing Deck Limit: {i}"
            testDeck = Deck(i)
            self.assertEqual(testDeck.getLimit(), i , msg)
        testDeck = Deck()
        self.assertEqual(testDeck.getLimit(), None , "Limit of default")

    def test_getSlots(self):
        for i in range(10, 100, 10):
            testDeck = Deck(i)
            for j in range(10):
                msg = f"Testing Deck Slots: {i} - {j + 1} = {i - j + 1}"
                testDeck.addCard(j)
                self.assertEqual(testDeck.getSlots(), (i - (j + 1)), msg)
        testDeck = Deck()
        self.assertEqual(testDeck.getSlots(), None, "Test slot of Default")

    def test_getSize(self):
        for i in range(10, 100, 10):
            testDeck = Deck(i)
            for j in range(10):
                msg = f"Testing Deck Size: {j + 1}"
                testDeck.addCard(j)
                self.assertEqual(testDeck.getSize(), (j + 1), msg)

    def test_addCard(self):
        testDeck = Deck()
        for i in range(-100, 400):
            if -1 < i < 360:
                self.assertTrue(testDeck.addCard(i), f"{i} is not in range of Cards")
            else:
                self.assertFalse(testDeck.addCard(i), f"{i} is in range of Cards")

    def test_Shuffle(self):
        testDeck = Deck()
        testDeckShuffled = Deck()
        for i in range(10):
            testDeck.addCard(i)
            testDeckShuffled.addCard(i)
        for i in range(10):
            self.assertEqual(testDeck.draw(), testDeckShuffled.draw(), "Same decks")
        for i in range(10):
            testDeck.addCard(i)
            testDeckShuffled.addCard(i)
        testDeckShuffled.shuffle()
        testList = []
        testShuffled = []
        for i in range(10):
            testList.append(testDeck.draw())
            testShuffled.append(testDeckShuffled.draw())
        self.assertNotEqual(testList, testShuffled, "Shuffled")

    def test_Draw(self):
        testDeck = Deck()
        for i in range(10):
            testDeck.addCard(i)
        for i in range(9, -1, -1):
            self.assertEqual(testDeck.draw(), i, "Draw Cards")

    def test_Pull(self):
        testDeck = Deck()
        for i in range(10):
            testDeck.addCard(i)
        i = 0
        while testDeck.getSize() != 0:
            self.assertEqual(testDeck.pull(0), i, "pulling index")
            i += 1

    def test_SortTitle(self):
        testDeck = Deck()
        for i in TESTLISTID:
            testDeck.addCard(i)
        testDeck.sortTitle()
        self.assertEqual(testDeck.pull(0), 95, "Test Title Sort")
        self.assertEqual(testDeck.draw(), 133, "Test Title Sort")

    def test_SortEdition(self):
        testDeck = Deck()
        for i in TESTLISTID:
            testDeck.addCard(i)
        testDeck.shuffle()
        testDeck.sortEdition()
        self.assertEqual(testDeck.pull(0), 3, "Test Edition Sort")
        self.assertEqual(testDeck.draw(), 357, "Test Edition Sort")
        self.assertEqual(testDeck.draw(), 359, "Test Edition Sort")
        self.assertEqual(testDeck.draw(), 318, "Test Edition Sort")
        self.assertEqual(testDeck.draw(), 276, "Test Edition Sort")
        self.assertEqual(testDeck.draw(), 281, "Test Edition Sort")

    def test_SearchDeckEdition(self):
        print("\nSearch Edition Test\n")
        trimmedDeck = Deck()
        TestDeck.searchDeckEdition(trimmedDeck, "Dominion")
        for i in trimmedDeck:
            self.assertTrue("Dominion" in i.getEditionName(), str(i))
        print("\tSearched Dominion:")
        trimmedDeck.printDeck()
        print("\n\tSearched Intrigue 1st Edition:")
        trimmedDeck = Deck()
        TestDeck.searchDeckEdition(trimmedDeck, "Intrigue 1st Edition")
        for i in trimmedDeck:
            self.assertTrue("Intrigue 1st Edition" in i.getEditionName(), str(i))
        trimmedDeck.printDeck()
        print("\n\tSearched Fantastic:")
        trimmedDeck = Deck()
        TestDeck.searchDeckEdition(trimmedDeck, "Fantastic")
        self.assertTrue(trimmedDeck.getSize() == 0)
        trimmedDeck.printDeck()

    def test_SearchDeckCost(self):
        print("\nSearch Deck Cost\n")
        trimmedDeck = Deck()
        TestDeck.searchDeckCost(trimmedDeck, "Three")
        for i in trimmedDeck:
            self.assertTrue("Three" in i.getCost(), i.__repr__)
        print("\tSearched Three:")
        trimmedDeck.printDeck()
        trimmedDeck = Deck()
        TestDeck.searchDeckCost(trimmedDeck, "Potion")
        for i in trimmedDeck:
            self.assertTrue("Potion" in i.getCost(), i.__repr__)
        print("\n\tSearched Potion:")
        trimmedDeck.printDeck()
        trimmedDeck = Deck()
        TestDeck.searchDeckCost(trimmedDeck, "Ten")
        self.assertTrue(trimmedDeck.getSize() == 0)

    def test_SearchDeckType(self):
        print("\nSearch Deck Type")
        trimmedDeck = Deck()
        TestDeck.searchDeckType(trimmedDeck, "Attack")
        for i in trimmedDeck:
            self.assertTrue("Attack" in i.getType(), i.__repr__)
        print("\n\tSearched Attack:")
        trimmedDeck.printDeck()
        trimmedDeck = Deck()
        TestDeck.searchDeckType(trimmedDeck,"Treasure")
        for i in trimmedDeck:
            self.assertTrue("Treasure" in i.getType(), i.__repr__)
        print("\n\tSearched Treasure:")
        trimmedDeck.printDeck()
        trimmedDeck = Deck()
        TestDeck.searchDeckType(trimmedDeck,"Altruistic")
        self.assertTrue(trimmedDeck.getSize() == 0)

    def test_SearchDeckTitle(self):
        cardFound, index = TestDeck.searchDeckTitles("Bandit")
        self.assertTrue(cardFound)
        testCard = Card(TestDeck.pull(index))
        self.assertEqual(testCard.getTitle(), "Bandit")
        cardFound, index = TestDeck.searchDeckTitles("Young Witch")
        self.assertTrue(cardFound)
        testCard = Card(TestDeck.pull(index))
        self.assertEqual(testCard.getTitle(), "Young Witch")
        cardFound, index = TestDeck.searchDeckTitles("Cody")
        self.assertFalse(cardFound)
        testCard = Card(TestDeck.pull(index))
        self.assertIsNone(testCard.getID())

    def test_PrintingDeck(self):
        print("\nTesting Printing Deck")
        trimmed = Deck()
        for i in range(3):
            trimmed.addCard(TestDeck.draw())
        trimmed.printDeck()
        print("\nTesting str(deck)")
        print(trimmed)

    def test_DeckIteration(self):
        msg = ""
        for i in TestDeck:
            msg += str(i) + "\n"
        msgTest = TestDeck.printDeck()
        self.assertEqual(msg, msgTest)

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
              165,  # 29['Poor House', '[One]', '[Action]', 'Dark Ages']
              400,
              -1]

CardList = []
for i in TESTLISTID:
    CardList.append(Card(i))
TestDeck = Deck()
for i in TESTLISTID:
    TestDeck.addCard(i)