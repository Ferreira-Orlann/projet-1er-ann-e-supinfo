from game.player import Player

class HumanPlayer(Player):
    def __init__(self, id, startconfig):
        super().__init__(id,startconfig)