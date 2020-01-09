from Logging.Logger import Customlogger

class Rewardmechanism:
    def __init__(self,minimum_bet):
        self.logger = Customlogger(__name__)
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.last_reward = []
        self.minimum_bet_multiplier = minimum_bet
        self.rewardbalance = 0

    def determine_reward(self, players, dealer):
        for player in players:
            if not player.has_blackjack:
                if self.is_bust(player.hand.value):
                    player.reward.losses += 1
                    player.last_reward = "loss"
                    player.reward.rewardbalance -= self.minimum_bet_multiplier
                elif self.is_bust(dealer.dealer_hand.value):
                    player.reward.wins += 1
                    player.last_reward = "win"
                    player.reward.rewardbalance += self.minimum_bet_multiplier
                elif player.hand.value > dealer.dealer_hand.value:
                    player.reward.wins += 1
                    player.last_reward = "win"
                    player.reward.rewardbalance += self.minimum_bet_multiplier
                elif player.hand.value < dealer.dealer_hand.value:
                    player.reward.losses += 1
                    player.last_reward = "loss"
                    player.reward.rewardbalance -= self.minimum_bet_multiplier
                else:
                    player.reward.draws += 1
                    player.last_reward = "draw"
            else:
                if dealer.has_blackjack:
                    player.reward.draws += 1
                    player.last_reward = "draw"
                    dealer.has_blackjack = False
                else:
                    player.reward.wins += 1.5
                    player.last_reward = "Win BJ"
                    player.has_blackjack = False
                    player.reward.rewardbalance += 1.5 * self.minimum_bet_multiplier


    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False

    def final_result(self):
        return f"(wins:{self.wins}, losses:{self.losses}, draws: {self.draws})"