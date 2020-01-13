import random

from src.Card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in
                      ["Spades,Black", "Clubs,Black", "Hearts,Red",
                       "Diamonds,Red"] for v in ["A", "2", "3", "4", "5", "6",
                                                 "7", "8", "9", "10", "J", "Q",
                                                 "K"]]
        random.shuffle(self.cards)
