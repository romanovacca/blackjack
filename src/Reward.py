from Logging.Logger import Customlogger


class Rewardmechanism:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.last_reward = []

    def determine_reward(self, player, dealer):
        if not player.has_blackjack:
            if self.is_bust(player.hand.value):
                player.losses += 1
                player.last_reward = "loss"
            elif self.is_bust(dealer.dealer_hand.value):
                player.wins += 1
                player.last_reward = "win"
                player.balance += 2 * player.ante
            elif player.hand.value > dealer.dealer_hand.value:
                player.wins += 1
                player.last_reward = "win"
                player.balance += 2 * player.ante
            elif player.hand.value < dealer.dealer_hand.value:
                player.losses += 1
                player.last_reward = "loss"
            else:
                player.draws += 1
                player.last_reward = "drawx"
                player.balance += player.ante
        else:
            if dealer.has_blackjack:
                player.draws += 1
                player.last_reward = "drawy"
                dealer.has_blackjack = False
                player.balance += player.ante
            else:
                player.wins += 1
                player.last_reward = "Win BJ " + str(player.name)
                player.has_blackjack = False
                player.balance += 2.5 * player.ante

    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False
