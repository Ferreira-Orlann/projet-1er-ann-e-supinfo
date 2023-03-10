from render.scene.basescene import BaseScene
from game.game import Game
from utils import CheckJson

class GameScene(BaseScene):
    def __init__(self, quoridor, game):
        super().__init__(quoridor, "configs/gamescene/custom.json")
        pass
    
    def LoadCustomConfig(self, json):
        json = CheckJson(json)
        