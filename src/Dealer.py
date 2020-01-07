from src.Hand import Hand
from Logging.Logger import Customlogger

class Dealer:
    def __init__(self,dealer=True):
        self.logger = Customlogger(__name__)
        self.dealer_hand = Hand()
        self.has_blackjack = False
