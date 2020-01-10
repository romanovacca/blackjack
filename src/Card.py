class Card:
    """
    Represents the playing cards. Each card will have a suit (hearts, diamonds,
    spades, and clubs) and a value (ace through king).
    When we call an instance of this class, it will return the value and
    according suit.

    """
    def __init__(self, suit, value):
        self.suit = suit.split(',')[0]
        self.color = suit.split(',')[1]
        self.value = value


    def __repr__(self):

        return " of ".join((self.value, self.suit))
