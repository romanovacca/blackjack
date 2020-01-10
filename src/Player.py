from src.Hand import Hand
from src.Reward import Rewardmechanism
from Logging.Logger import Customlogger

class Player:
    def __init__(self,i,strategy,dealer=False):
        self.logger = Customlogger(__name__)
        self.name = i
        self.has_blackjack = False
        self.is_dealer = dealer
        self.hand = Hand()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.balance = 50
        #self.reward = Rewardmechanism()
        #self.last_reward = self.reward.last_reward
        self.strategy = strategy
