from Logging.Logger import Customlogger


class Sidebet:
    def __init__(self):
        self.logger = Customlogger(__name__)
        self.pairs = {
            "perfect_pair_value": 25,
            "coloured_pair": 12,
            "mixed_pair": 6
        }
        self.sidebet_with_dealer = {
            "suited_trips": 100,
            "straight_flush": 40,
            "three_of_a_kind": 30,
            "straight": 10,
            "flush": 5
        }

    def check_for_sidebet(self,hand):
        value = 0
        value += self.perfect_pair(hand)
        value += self.coloured_pair(hand)
        value += self.mixed_pair(hand)
        return value

    def perfect_pair(self, hand):
        if hand[0].suit == hand[1].suit and hand[0].value == hand[1].value:
            return self.pairs["perfect_pair_value"]
        else:
            return 0

    def coloured_pair(self,hand):
        if hand[0].suit != hand[1].suit and hand[0].color == hand[1].color and hand[0].value == hand[1].value:
            return self.pairs["coloured_pair"]
        else:
            return 0

    def mixed_pair(self,hand):
        if hand[0].suit != hand[1].suit and hand[0].color != hand[1].color and hand[0].value == hand[1].value:
            return self.pairs["mixed_pair"]
        else:
            return 0
