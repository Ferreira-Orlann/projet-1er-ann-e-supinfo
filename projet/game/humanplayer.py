from game.player import Player

class HumanPlayer(Player):
    def __init__(self, id, startconfig):
        Player.__init__(self,id, startconfig)