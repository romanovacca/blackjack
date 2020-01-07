from Logging.Logger import Customlogger

class Rewardmechanism:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.last_reward = []

    def determine_reward(self, players, dealer):
        for player in players:

            if self.is_bust(player.hand.value):
                player.reward.losses += 1
                player.last_reward = "loss"
            elif self.is_bust(dealer.dealer_hand.value):
                player.reward.wins += 1
                player.last_reward = "win"
            elif player.hand.value > dealer.dealer_hand.value:
                player.reward.wins += 1
                player.last_reward = "win"
            elif player.hand.value < dealer.dealer_hand.value:
                player.reward.losses += 1
                player.last_reward = "loss"
            else:
                player.reward.draws += 1
                player.last_reward = "draw"


    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False

    def final_result(self):
        return f"(wins:{self.wins}, losses:{self.losses}, draws: {self.draws})"