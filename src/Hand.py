from Logging.Logger import Customlogger
from src.Reward import Rewardmechanism
from src.Sidebets import Sidebet

class Hand:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.cards = []
        self.value = 500
        self.hidden_dealer_card = None
        #self.reward = Rewardmechanism()
        self.sidebet = Sidebet()

    def draw_card_hidden(self, card):
        self.hidden_dealer_card = card

    def flip_hidden_card(self):
        self.cards.append(self.hidden_dealer_card)
        self.hidden_dealer_card = None

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def check_for_sidebet(self):
        self.sidebet_won_value = self.sidebet.check_for_sidebet(self.cards)
