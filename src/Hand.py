class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        self.hidden_dealer_card = None

    def make_card_hidden(self,card):
        self.hidden_dealer_card = card