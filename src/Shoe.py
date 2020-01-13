import random

from src.Deck import Deck
from Logging.Logger import Customlogger


class Shoe:
    def __init__(self, decks=8):
        self.logger = Customlogger(__name__)
        self.decks = decks
        #self.shoe = []
        self.create_shoe()
        self.max_number_of_cards_in_deck = len(self.shoe)


    def get_shoe(self):
        return self.shoe

    def draw_card(self):
        """
        Draws a card from the shoe. It is also checked if a card is the cutting
        card or not, so this is handled properly.

        """
        if len(self.shoe) > 0:
            if self.shoe[0] == "CC":
                self.shoe.pop(0)
                self.cutting_card_shown = True

            card = self.shoe.pop(0)
            self.percentage_of_deck_left = (len(self.shoe) /
                                            self.max_number_of_cards_in_deck) * 100
            self.calculate_counts(card)

            return card

    def calculate_counts(self, card):
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
        if not (len(self.shoe)) == 0:
            self.true_count = self.running_count / (len(self.shoe) / 52)
        else:
            print("x")

    def determine_cutting_card_index(self):
        return random.randrange(
            round(len(self.shoe) * 0.48),
            round(len(self.shoe) - (len(self.shoe) * 0.48))
        )

    def add_cutting_card(self):
        """ Adds a cutting card to the deck.
        """
        cutting_card_name = "CC"
        self.shoe.insert(self.cutting_card_index, cutting_card_name)

    def create_shoe(self):
        """ A collection of decks.

        This creates the whole shoe and all the parameters that are needed to
        make sure that all the information about the shoe is properly updated
        and maintained. This will be called everytime after the cutting card is
        shown.

        """
        #self.logger.log_message("New shoe in play.")

        self.shoe = []

        for i in range(self.decks):
            deck = Deck()
            self.shoe += deck.cards

        random.shuffle(self.shoe)
        random.shuffle(self.shoe)
        random.shuffle(self.shoe)
        random.shuffle(self.shoe)
        random.shuffle(self.shoe)
        random.shuffle(self.shoe)
        random.shuffle(self.shoe)

        self.cutting_card_index = self.determine_cutting_card_index()
        self.percentage_of_deck_left = 0
        self.running_count = 0
        self.true_count = 0
        self.add_cutting_card()
        self.cutting_card_shown = False

    def check_shoe_replacement(self):
        """
        If the cutting card is shown, the shoe should be replaced.

        """
        if self.cutting_card_shown == True:
            self.create_shoe()
            self.cutting_card_shown == False

        return
