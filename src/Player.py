from src.Hand import Hand
from Logging.Logger import Customlogger


class Player:
    def __init__(self, name, ante, use_sidebet, sidebet_size):
        self.logger = Customlogger(__name__)
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.balance = 0
        self.name = name
        self.ante = ante
        self.use_sidebet = use_sidebet
        self.sidebet_size = sidebet_size
        self.has_blackjack = False
        self.hand = Hand(self.use_sidebet, sidebet_size)

    def final_result(self):
        return f"wins:{self.wins}, losses:{self.losses}, draws: {self.draws}"
