import random

from src.Deck import Deck


class Playingdeck:
    def __init__(self, decks=8):
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

        self.cutting_card_index = self.determine_cutting_card_index()

        self.max_number_of_cards_in_deck = len(self.playing_deck)
        self.percentage_of_deck_left = 0

        self.running_count = 0
        self.true_count = 0
        self.add_cutting_card()
        self.cutting_card_shown = False

    def get_playing_deck(self):
        return self.playing_deck

    def draw_card(self):
        if self.playing_deck[0] == "CC":
            self.playing_deck.pop(0)
            self.cutting_card_shown = True
        card = self.playing_deck.pop(0)
        self.percentage_of_deck_left = (len(self.playing_deck) /
                                        self.max_number_of_cards_in_deck) * 100
        self.calculate_counts(card)

        return card

    def calculate_counts(self,card):
        self.calculate_running_count(card)
        self.calculate_true_count()

    def calculate_running_count(self, card):
        """
        2 - 6 = +1
        7 - 9 = 0
        10 - Ace = -1

        The higher the running count is, the more 'faces' are still in the deck
        which is advantages for the player.
        """
        if not card.value.isnumeric() or int(card.value) == 10:
            self.running_count -= 1
        elif int(card.value) >= 2 and int(card.value) <= 6:
            self.running_count += 1
        elif int(card.value) >= 7 and int(card.value) <= 9:
            pass
        else:
            raise ValueError

        return

    def calculate_true_count(self):
        """https://www.countingedge.com/card-counting/true-count/
        In a 6 shoe deck, each additional true count point gives the player a
        0,5 advantage. So when the true count is 1, you have even odds with the
        dealer.
        """
        self.true_count = self.running_count / (len(self.playing_deck)/52)

    def determine_cutting_card_index(self):
        return random.randrange(
            round(len(self.playing_deck) * 0.4), round(len(self.playing_deck) - (len(self.playing_deck) *0.4))
        )
    def add_cutting_card(self):
        self.playing_deck.insert(self.cutting_card_index,"CC")
