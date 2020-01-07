from src.Hand import Hand
from src.Reward import Rewardmechanism
class Player:
    def __init__(self,dealer=False):
        self.has_blackjack = False
        self.is_dealer = dealer
        self.balance = 50
        self.hand = Hand()
        self.reward = Rewardmechanism()
        self.last_reward = -9999