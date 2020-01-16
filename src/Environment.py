import gym
from gym import spaces
from gym.utils import seeding
from Logging.Logger import Customlogger
from src.Shoe import Shoe
from src.Player import Player
from src.Dealer import Dealer
from src.Reward import Rewardmechanism


class BlackjackEnv(gym.Env):
    """ Blackjack environment
    """

    def __init__(self,env_players):
        self.logger = Customlogger(__name__)
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),
            spaces.Discrete(11),
            spaces.Discrete(2)))
        self.seed()
        self.shoe = Shoe()
        self.cutting_card_showed = self.shoe.cutting_card_shown
        self.env_players = env_players
        self.players = []
        self.reward = Rewardmechanism()

    def reset(self, i_episode, number_of_players, strategies):
        #print(f"Starting iteration number {i_episode}")
        try:
            assert number_of_players >= 1
        except AssertionError as e:
            e.args += ('There needs to be at least 1 player to play the '
                       'game.', '.')
            raise

        self.shoe.check_shoe_replacement()
        if i_episode == 0:
            self.create_players(number_of_players, strategies)
            self.create_dealer()
        self.dealer.has_blackjack = False
        print("balance is :",self.players[0].balance)
        print("balance is :", self.players[1].balance)
        self.deal_initial_cards(number_of_players)
        return

    def create_players(self):
        for person in self.env_players:
            self.players.append(Player(person["name"],
                                       person["ante"],
                                       person["use_sidebet"],
                                       person["sidebet_ante"]))

    def create_dealer(self):
        self.dealer = Dealer()

    def deal_initial_cards(self, number_of_players):
        number_of_initial_cards = 2
        for i in range(number_of_initial_cards):
            for j in range(number_of_players):
                if i == 0:
                    self.dealer.dealer_hand.cards = []
                    self.players[j].hand.cards = []
                    self.players[j].hand.cards.append(self.shoe.draw_card())
                    self.dealer.dealer_hand.cards.append(self.shoe.draw_card())
                elif i == 1:
                    self.players[j].hand.cards.append(self.shoe.draw_card())
                    self.dealer.dealer_hand.draw_card_hidden(
                        self.shoe.draw_card())
                    print("player",self.players[j].name, self.players[j].hand.cards)

                    self.players[j].balance -= self.players[j].ante

                    if self.players[j].use_sidebet:
                        self.players[j].balance -= self.players[j].sidebet_size
                        print("balance after dealing :", self.players[j].balance)
                        self.players[j].balance += (self.players[
                                                        j].hand.check_for_sidebet())
                else:
                    pass

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, stand_on_17):
        players_busted = 0
        for player in self.players:
            if player.hand.get_value() == 21 and len(player.hand.cards) == 2:
                player.has_blackjack = True
                action = 0
            else:
                if stand_on_17 == True:
                    if player.hand.get_value() >= 17:
                        action = 0
                    else:
                        action = self.take_action()
                else:
                    action = self.take_action()

            assert self.action_space.contains(action)
            while action == 1:
                player.hand.cards.append(self.shoe.draw_card())
                if self.is_bust(player.hand.get_value()) or player.hand.get_value() == 21:
                    if self.is_bust(player.hand.get_value()):
                        players_busted += 1
                    action = 0
                else:
                    action = self.take_action()

        self.dealer.dealer_hand.flip_hidden_card()

        if self.dealer.dealer_hand.get_value() == 21 and len(
                self.dealer.dealer_hand.cards) == 2:
            self.dealer.has_blackjack = True
        else:
            while self.dealer.dealer_hand.get_value() < 17 and players_busted< len(self.players):
                self.dealer.dealer_hand.cards.append(self.shoe.draw_card())
        for player in self.players:
            self.reward.determine_reward(player, self.dealer)
            #print(self.players[j].last_reward)

    def take_action(self):
        action = self.action_space.sample()
        return action

    def is_bust(self, value):
        if value > 21:
            return True
        else:
            return False

    def has_blackjack(self, hand):
        if len(hand.cards) == 2 and hand.value == 21:
            return True
        else:
            return False

    def result(self, result_type):
        for player in self.players:
            if result_type == "individual":
                print(f"player{player.name} last result : "
                      f"{player.hand.get_value()} vs"
                      f" {self.dealer.dealer_hand.get_value()}"
                      f" {player.last_reward} | Final Balance:"
                      f" {player.balance}|")

                print("Round ended.\n")

            elif result_type == "summary":
                print(f"player{player.name}: "
                      f"{player.final_result()} |"
                      f"Final Balance: {player.balance}")
                print("Game finished.\n")

            else:
                raise NotImplementedError
