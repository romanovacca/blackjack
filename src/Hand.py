from Logging.Logger import Customlogger

class Hand:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.cards = []
        self.value = 0
        self.hidden_dealer_card = None
        self.sidebet = []

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

    def has_perfect_pair(self):
        if self.cards[0] == self.cards[1]:
            return "HAS PERFECT PAIR"
