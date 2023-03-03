from game.player import Player

class HumanPlayer(Player):
    def __init__(self, id):
        Player.__init__(self,id)