from src.Hand import Hand

class Dealer:
    def __init__(self,dealer=True):
        self.dealer_hand = Hand()
        #self.is_dealer = dealer
        self.has_blackjack = False
