import gym
from gym import spaces
from gym.utils import seeding
from Logging.Logger import Customlogger
from src.Shoe import Shoe
from src.Player import Player
from src.Dealer import Dealer
from src.Reward import Rewardmechanism


class BlackjackEnv(gym.Env):
    """Simple blackjack environment
    Blackjack is a card game where the goal is to obtain cards that sum to as
    near as possible to 21 without going over.  They're playing against a fixed
    dealer.
    Face cards (Jack, Queen, King) have point value 10.
    Aces can either count as 11 or 1, and it's called 'usable' at 11.
    This game is placed with an infinite deck (or with replacement).
    The game starts with each (player and dealer) having one face up and one
    face down card.
    The player can request additional cards (hit=1) until they decide to stop
    (stick=0) or exceed 21 (bust).
    After the player sticks, the dealer reveals their facedown card, and draws
    until their sum is 17 or greater.  If the dealer goes bust the player wins.
    If neither player nor dealer busts, the outcome (win, lose, draw) is
    decided by whose sum is closer to 21.  The reward for winning is +1,
    drawing is 0, and losing is -1.
    The observation of a 3-tuple of: the players current sum,
    the dealer's one showing card (1-10 where 1 is ace),
    and whether or not the player holds a usable ace (0 or 1).
    This environment corresponds to the version of the blackjack problem
    described in Example 5.1 in Reinforcement Learning: An Introduction
    by Sutton and Barto.
    http://incompleteideas.net/book/the-book-2nd.html
    """

    def __init__(self):
        self.logger = Customlogger(__name__)
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),
            spaces.Discrete(11),
            spaces.Discrete(2)))
        self.seed()
        self.shoe = Shoe()
        self.cutting_card_showed = self.shoe.cutting_card_shown
        self.players = []
        self.reward = Rewardmechanism()




    def reset(self,i_episode,number_of_players,strategies):
        try:
            assert number_of_players >= 1
        except AssertionError as e:
            e.args += ('There needs to be at least 1 player to play the '
                       'game.', '.')
            raise

        self.shoe.check_shoe_replacement()
        if i_episode == 0:
            self.create_players(number_of_players,strategies)
            self.create_dealer()
        self.dealer.has_blackjack = False
        self.deal_initial_cards(number_of_players)
        return

    def create_players(self,number_of_players,strategies):
        for i in range(number_of_players):
            self.players.append(Player(i,strategies[i]))

    def create_dealer(self):
        self.dealer = Dealer()

    def deal_initial_cards(self,number_of_players):
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
                    self.dealer.dealer_hand.draw_card_hidden(self.shoe.draw_card())
                    self.players[j].hand.check_for_sidebet()
                else:
                    pass

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self,stand_on_17):
        for player in self.players:
            if player.hand.get_value() == 21 and len(player.hand.cards)  == 2:
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
                if self.is_bust(player.hand.get_value()):
                    action = 0
                else:
                    action = self.take_action()

        self.dealer.dealer_hand.flip_hidden_card()

        if self.dealer.dealer_hand.get_value() == 21 and len(
                self.dealer.dealer_hand.cards) == 2:
            self.dealer.has_blackjack = True
        else:
            while self.dealer.dealer_hand.get_value() < 17 and player.hand.get_value() <= 21:
                self.dealer.dealer_hand.cards.append(self.shoe.draw_card())

        self.reward.determine_reward(self.players,self.dealer)

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

    def result(self,result_type):
        for player in self.players:
            if result_type == "individual":
                print(f"player{player.name} last result : "
                      f"{player.hand.get_value()} vs"
                      f" {self.dealer.dealer_hand.get_value()}"
                      f" {player.last_reward}")
                print("Round ended.\n")

            elif result_type == "summary":
                print(f"player{player.name} last result : "
                                        f"{player.reward.final_result()} |"
                      f"Final Balance: {player.reward.rewardbalance}|"
                      f" Strategy: {player.strategy}|")
                print("Game finished.\n")

            else:
                raise NotImplementedError


