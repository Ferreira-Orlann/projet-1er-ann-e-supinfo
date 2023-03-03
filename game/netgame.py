from game.humanplayer import HumanPlayer
import operator
from sys import exit
from game.game import Game

class NetGame(Game):
    def __init__(self, quoridor, config, scene, networkconfig):
        
        Game.__init__(self, quoridor, config, scene)