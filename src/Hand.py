class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        self.has_blackjack = False
        self.hidden_dealer_card = None
        self.money = 0

    def draw_card_hidden(self, card):
        self.hidden_dealer_card = card

    def flip_hidden_card(self):
        self.cards.append(self.hidden_dealer_card)

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
