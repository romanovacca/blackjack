from src.Hand import Hand
from Logging.Logger import Customlogger

class Dealer:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.dealer_hand = Hand(use_sidebet=False)
        self.has_blackjack = False
