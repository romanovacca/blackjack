import numpy as np

class Cards(object):
    def __init__(self, decks=8, cut=.5):
        self.pile = decks*[1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.folded = None

    def draw(self):
        card = self.pile[ np.random.randint( len(self.pile) ) ]
        self.pile.remove(card)
        return card

    def blind_bank(self):
        self.folded = self.draw()

    def flip_folded(self):
        dum = self.folded
        self.folded = None
        return dum

    def possible_cards(self):
        if self.folded:
            return sorted(self.pile + [self.folded])
        else:
            return sorted(self.pile)
        
    def as_tens(self, hand):
        return [min(10, x) for x in hand]

    def card_odds(self):
        return [self.possible_cards().count(x)/len(self.possible_cards()) for x in range(1,14)]

    def number_odds(self):
        return self.card_odds()[0:9] + [sum(self.card_odds()[9::])]