from src.Hand import Hand

class Player:
    def __init__(self,dealer=False):
        self.has_blackjack = False
        self.is_dealer = dealer
        self.balance = 50
        self.player = Hand()