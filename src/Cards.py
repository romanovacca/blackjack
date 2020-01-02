import numpy as np
from random import shuffle


class Cards(object):
    def __init__(self, decks=8, cut=.5):
        self.number_of_suits_in_deck = 4
        self.pile_dict = {"A": 1,
                          "2": 2,
                          "3": 3,
                          "4": 4,
                          "5": 5,
                          "6": 6,
                          "7": 7,
                          "8": 8,
                          "9": 9,
                          "10": 10,
                          "J": 10,
                          "Q": 10,
                          "K": 10
                          }
        self.pile = decks * self.number_of_suits_in_deck * ["A", 2, 3, 4, 5,
                                                            6, 7, 8, 9, 10, "J",
                                                            "Q", "K"]
        shuffle(self.pile)
        self.max_number_of_cards_in_deck = len(self.pile)
        self.percentage_of_deck_left = 0
        self.hidden_dealer_card = None
        self.running_count = 0
        self.true_count = 0

    def draw_card(self):
        card = self.pile[np.random.randint(len(self.pile))]
        self.pile.remove(card)
        self.percentage_of_deck_left = (len(self.pile) /
                                        self.max_number_of_cards_in_deck) * 100
        self.calculate_running_count(card)

        return [v for k, v in self.pile_dict.items() if k == str(card)][0]

    # def draw_hand(self):
    #     return [self.draw_card(), self.draw_card()]

    def blind_bank(self):
        self.hidden_dealer_card = self.draw_card()

    def flip_hidden_dealer_card(self):
        dum = self.hidden_dealer_card
        self.hidden_dealer_card = None
        return dum

    def possible_cards(self):
        if self.hidden_dealer_card:
            return sorted(self.pile + [self.hidden_dealer_card])
        else:
            return sorted(self.pile)

    def as_tens(self, hand):
        return [min(10, x) for x in hand]

    def faces_odds(self):
        return [self.possible_cards().count(x) / len(self.possible_cards()) for
                x in range(1, 14)]

    def number_odds(self):
        return self.faces_odds()[0:9] + [sum(self.faces_odds()[9::])]

    def calculate_running_count(self, card):
        """
        2 - 6 = +1
        7 - 9 = 0
        10 - Ace = -1
        :return:
        :rtype:
        """
        if card == 'Q':
            card = 10
        if card == 'J':
            card = 10
        if card == 'K':
            card = 10
        if card == 'A':
            card = 1

        if card >= 2 and card <= 6:
            self.running_count += 1
        elif card >= 7 and card <= 9:
            pass
        else:
            self.running_count -= 1

        self.calculate_true_count()
        return

    def calculate_true_count(self):
        self.true_count = self.running_count / (len(self.pile)/52)
