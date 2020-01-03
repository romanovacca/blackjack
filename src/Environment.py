import gym
from gym import spaces
from gym.utils import seeding
#from Logging.Logger import Customlogger
from src.Playingdeck import Playingdeck
from src.Hand import Hand

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
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),
            spaces.Discrete(11),
            spaces.Discrete(2)))
        self.seed()
        self.deck = Playingdeck()
        self.natural = natural

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        if action:  # hit: add a card to players hand and return
            self.player.append(self.cards.draw_card())
            if is_bust(self.player):
                done = True
                reward = -1

            else:
                done = False
                reward = 0
        else:  # stick: play out the dealers hand, and score
            done = True
            self.dealer.append(self.cards.flip_hidden_dealer_card())
            while sum_hand(self.dealer) < 17:
                self.dealer.append(self.cards.draw_card())
            reward = cmp(score(self.player), score(self.dealer))
            if self.natural and is_natural(self.player) and reward == 1:
                reward = 1.5

        if done == True:
            self.calculate_reward(reward)

        return self._get_obs(), done, {}

    def calculate_reward(self,reward):
        if reward == 0:
            self.logger.log_message("DRAW")
        elif reward == 1 or reward == 1.5:
            self.logger.log_message("WIN")
        elif reward == -1:
            self.logger.log_message("LOSE")


    def reset(self):
        self.player = Hand()
        self.dealer = Hand(dealer=True)

        self.player.cards.append(self.deck.draw_card())
        self.dealer.cards.append(self.deck.draw_card())
        self.player.cards.append(self.deck.draw_card())
        self.dealer.make_card_hidden(self.deck.draw_card())

        return

    # def _get_obs(self):
    #     "This makes sure that the player only knows the first card the dealer has."
    #
    #     return (sum_hand(self.player), self.dealer[0], usable_ace(self.player))

    # def readable_observation(self):
    #     player_hand,dealer_hand,has_usable_ace = self._get_obs()
    #     if is_natural(self.player):
    #         natural_blackjack = True
    #     else:
    #         natural_blackjack = False
    #     return player_hand,dealer_hand,natural_blackjack

    def take_action(self):
        action = self.action_space.sample()
        return self.translate_action(action)
