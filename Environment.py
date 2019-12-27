import gym
from gym import spaces
from gym.utils import seeding
from Logging.Logger import Customlogger


def cmp(a, b):
    return float(a > b) - float(a < b)


# 1 = Ace, 2-10 = Number cards, Jack/Queen/King = 10
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(np_random):
    return int(np_random.choice(deck))


def draw_hand(np_random):
    return [draw_card(np_random), draw_card(np_random)]


def usable_ace(hand):  # Does this hand have a usable ace?
    return 1 in hand and sum(hand) + 10 <= 21


def sum_hand(hand):  # Return current hand total
    if usable_ace(hand):
        return sum(hand) + 10
    return sum(hand)


def is_bust(hand):  # Is this hand a bust?
    return sum_hand(hand) > 21


def score(hand):  # What is the score of this hand (0 if bust)
    return 0 if is_bust(hand) else sum_hand(hand)


def is_natural(hand):  # Is this hand a natural blackjack?
    return sorted(hand) == [1, 10]


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
    def __init__(self, natural=False):
        self.logger = Customlogger(__name__)
        self.logger.log_message("Setting up the BlackJack environment.\n")
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),
            spaces.Discrete(11),
            spaces.Discrete(2)))
        self.seed()
        self.natural = natural

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        if action:  # hit: add a card to players hand and return
            self.player.append(draw_card(self.np_random))
            self.logger.log_message(f"Player hits an {self.player[-1]}")
            self.logger.log_message(f"Player new total: {sum(self.player)}")
            if is_bust(self.player):
                done = True
                reward = -1
            else:
                done = False
                reward = 0
        else:  # stick: play out the dealers hand, and score
            done = True
            self.logger.log_message(f"Dealer hits an {self.dealer[-1]}")
            self.logger.log_message(f"Dealer new total: {sum(self.dealer)}")
            while sum_hand(self.dealer) < 17:
                self.dealer.append(draw_card(self.np_random))
                self.logger.log_message(f"Dealer hits an {self.dealer[-1]}")
                self.logger.log_message(f"Dealer new total: {sum(self.dealer)}")
            reward = cmp(score(self.player), score(self.dealer))
            if self.natural and is_natural(self.player) and reward == 1:
                reward = 1.5

        if done == True:
            self.calculate_reward(reward)

        return self._get_obs(), done, {}

    def calculate_reward(self,reward):
        #TODO: Check if logic makes sense
        if reward == 0:
            self.logger.log_message("DRAW")
        elif reward == 1 or reward == 1.5:
            self.logger.log_message("WIN")
        elif reward == -1:
            self.logger.log_message("LOSE")


    def _get_obs(self):
        "This makes sure that the player only knows the first card the dealer has."

        return (sum_hand(self.player), self.dealer[0], usable_ace(self.player))

    def reset(self):
        self.player = [draw_card(self.np_random)]
        self.dealer = [draw_card(self.np_random)]
        self.player.append(draw_card(self.np_random))
        self.dealer.append(draw_card(self.np_random))
        self.logger.log_message(f"Player: {self.player} -> {sum(self.player)}")
        self.logger.log_message(f"Dealer: {self.dealer[0]}")
        self.logger.log_message(f"Player has a usable Ace is: {usable_ace(self.player)}")

        return self.readable_observation()

    def readable_observation(self):
        player_hand,dealer_hand,has_usable_ace = self._get_obs()
        return player_hand,dealer_hand

    def take_action(self):
        action = self.action_space.sample()
        return self.translate_action(action)

    def translate_action(self,action):
        if action == 0:
            self.logger.log_message("The player doesn't draw another card.")
            return 0
        elif action == 1:
            self.logger.log_message("The player hits another card. ")
            return 1
        else:
            raise NotImplementedError