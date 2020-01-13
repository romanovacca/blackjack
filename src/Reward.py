from Logging.Logger import Customlogger


class Rewardmechanism:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.last_reward = []
        self.minimum_bet_multiplier = 1

    def determine_reward(self, players, dealer):
        for player in players:
            if not player.has_blackjack:
                if self.is_bust(player.hand.value):
                    player.losses += 1
                    player.last_reward = "loss"
                    player.balance -= self.minimum_bet_multiplier
                    #player.balance += player.hand.sidebet_won_value
                elif self.is_bust(dealer.dealer_hand.value):
                    player.wins += 1
                    player.last_reward = "win"
                    player.balance += self.minimum_bet_multiplier
                    #player.balance += player.hand.sidebet_won_value
                elif player.hand.value > dealer.dealer_hand.value:
                    player.wins += 1
                    player.last_reward = "win"
                    player.balance += self.minimum_bet_multiplier
                    #player.balance += player.hand.sidebet_won_value
                elif player.hand.value < dealer.dealer_hand.value:
                    player.losses += 1
                    player.last_reward = "loss"
                    player.balance -= self.minimum_bet_multiplier
                    #player.balance += player.hand.sidebet_won_value
                else:
                    player.draws += 1
                    player.last_reward = "draw"
                    #player.balance += player.hand.sidebet_won_value
            else:
                if dealer.has_blackjack:
                    player.draws += 1
                    player.last_reward = "draw"
                    dealer.has_blackjack = False
                    #player.balance += player.hand.sidebet_won_value
                else:
                    player.wins += 1
                    player.last_reward = "Win BJ" +str(player.name)
                    player.has_blackjack = False
                    player.balance += 1.5 * self.minimum_bet_multiplier
                    #player.balance += player.hand.sidebet_won_value

        #player.balance += player.hand.sidebet_won_value

    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False
