from src.Hand import Hand
from src.Reward import Rewardmechanism
from Logging.Logger import Customlogger


class Player:
    def __init__(self, i, strategy,use_sidebet):
        self.logger = Customlogger(__name__)
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.balance = 10
        self.name = i
        self.has_blackjack = False
        self.hand = Hand(use_sidebet)
        self.strategy = strategy

    def final_result(self):
        return f"wins:{self.wins}, losses:{self.losses}, draws: {self.draws}"