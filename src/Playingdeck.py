import random

from src.Deck import Deck

class Playingdeck:
    def __init__(self,decks=8):
        self.playing_deck = []

        for i in range(decks):
            deck = Deck()
            self.playing_deck += deck.cards
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)
        random.shuffle(self.playing_deck)

        self.max_number_of_cards_in_deck = len(self.playing_deck)
        self.percentage_of_deck_left = 0

        self.running_count = 0
        self.true_count = 0

        #self.hidden_dealer_card = None


    def remove_card(self):
        raise NotImplementedError

    def get_playing_deck(self):
        return self.playing_deck

    def draw_card(self):
        card = self.playing_deck.pop(0)
        self.percentage_of_deck_left = (len(self.playing_deck) /
                                        self.max_number_of_cards_in_deck) * 100

        return card

    #def blind_bank(self):
    #    return self.draw_card()