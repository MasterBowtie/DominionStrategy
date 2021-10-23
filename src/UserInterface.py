import Deck, Cards, KingdomCards


class UserInterface:

    def __init__(self):
        self.__deck = Deck.Deck()
        self.__playDeck = Deck.Deck(10)
        self.__trimDeck = Deck.Deck()

    def run(self):

        print("Welcome to the Dominion Card Game card shuffler!")

