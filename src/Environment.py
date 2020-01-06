import gym
from gym import spaces
from gym.utils import seeding
# from Logging.Logger import Customlogger
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
        #self.natural = natural
        self.cutting_card_showed = self.deck.cutting_card_shown

    def reset(self):
        self.player = Hand()
        self.dealer = Hand(dealer=True)

        self.player.cards.append(self.deck.draw_card())
        self.dealer.cards.append(self.deck.draw_card())
        self.player.cards.append(self.deck.draw_card())
        self.dealer.draw_card_hidden(self.deck.draw_card())
        return

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self):
        if self.player.get_value() == 21 and len(self.player.cards) == 2:
            done = True
            self.player.has_blackjack = True
            self.dealer.flip_hidden_card()
            reward = self.determine_reward(self.player.get_value(),
                                           self.dealer.get_value()) -0.5
            action = 0
        else:
            action = self.take_action()

        assert self.action_space.contains(action)

        if action:  # hit: add a card to players hand and return
            self.player.cards.append(self.deck.draw_card())
            if self.is_bust(self.player.get_value()):
                done = True
                self.dealer.flip_hidden_card()
                reward = self.determine_reward(self.player.get_value(),
                                               self.dealer.get_value())
            else:
                done = False
                reward = 0

        else:  # stick: play out the dealers hand, and score
            done = True
            self.dealer.flip_hidden_card()
            if self.dealer.get_value() == 21 and len(self.dealer.cards) == 2:
                self.dealer.has_blackjack = True
                reward = self.determine_reward(self.player.get_value(),
                                               self.dealer.get_value())
            else:
                while self.dealer.get_value() < 17:
                    self.dealer.cards.append(self.deck.draw_card())

                reward = self.determine_reward(self.player.get_value(),
                                               self.dealer.get_value())

            # if self.natural and is_natural(self.player) and reward == 1:
            #     reward = 1.5
        #self.cutting_card_showed
        return reward, ((f"player value:",self.player.get_value()),(f"dealer",self.dealer.get_value())), done

    def take_action(self):
        action = self.action_space.sample()
        return action

    def cmp(self, a, b):
        return float(a > b) - float(a < b)

    def determine_reward(self, player_value, dealer_value):
        if self.is_bust(player_value):
            return 1
        elif self.is_bust(dealer_value):
            return -1
        elif player_value > dealer_value:
            return -1
        elif player_value < dealer_value:
            return 1
        else:
            return 0

    def is_bust(self,value):
        if value > 21:
            return True
        else:
            return False
    def has_blackjack(self,hand):
        if len(hand.cards) == 2 and hand.value == 21:
            return True
        else:
            return False
