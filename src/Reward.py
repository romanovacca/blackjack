
class Rewardmechanism:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def determine_reward(self, players, dealer):
        for player in players:

            if self.is_bust(player.hand.value):
                player.reward.losses += 1
            elif self.is_bust(dealer.dealer_hand.value):
                player.reward.wins += 1
            elif player.hand.value > dealer.dealer_hand.value:
                player.reward.wins += 1
            elif player.hand.value < dealer.dealer_hand.value:
                player.reward.losses += 1
            else:
                player.reward.draws += 1


    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False

    def add_reward(self,reward):
        if reward == 0:
            self.draws += 1
        elif reward == 1:
            self.losses += 1
        else:
            self.wins += 1

    def final_result(self):
        return f"(wins:{self.wins}, losses:{self.losses}, draws: {self.draws})"