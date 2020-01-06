class Errors(BaseException):
    def __init__(self):
        self.name = __name__

    def NotEnoughPlayersError(self):
        return "There needs to be at least 1 player to play the game."