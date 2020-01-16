from Logging.Logger import Customlogger


class Sidebet:
    def __init__(self, sidebet_ante):
        self.logger = Customlogger(__name__)
        self.sidebet_ante = sidebet_ante
        self.pairs = {
            "perfect_pair_value": (25 * self.sidebet_ante) + self.sidebet_ante,
            "coloured_pair": (12 * self.sidebet_ante) + self.sidebet_ante,
            "mixed_pair": (6 * self.sidebet_ante) + self.sidebet_ante
        }
        self.sidebet_with_dealer = {
            "suited_trips": 100 * self.sidebet_ante,
            "straight_flush": 40 * self.sidebet_ante,
            "three_of_a_kind": 30 * self.sidebet_ante,
            "straight": 10 * self.sidebet_ante,
            "flush": 5 * self.sidebet_ante
        }
        self.sidebet_ante = sidebet_ante

    def sidebets(self, hand):
        value = 0
        value += self.perfect_pair(hand)
        value += self.coloured_pair(hand)
        value += self.mixed_pair(hand)
        return value

    def perfect_pair(self, hand):
        if hand[0].suit == hand[1].suit and hand[0].value == hand[1].value:
            # print("has perfect pair")
            return self.pairs["perfect_pair_value"]
        else:
            return 0

    def coloured_pair(self, hand):
        if hand[0].suit != hand[1].suit and hand[0].color == hand[1].color and \
                hand[0].value == hand[1].value:
            # print("has coloured pair")
            return self.pairs["coloured_pair"]
        else:
            return 0

    def mixed_pair(self, hand):
        if hand[0].suit != hand[1].suit and hand[0].color != hand[1].color and \
                hand[0].value == hand[1].value:
            # print("has mixed pair")
            return self.pairs["mixed_pair"]
        else:
            return 0
