from render.scene.basescene import BaseScene
from utils import CheckJson

class GameScene(BaseScene):
    def __init__(self, quoridor, game):
        super().__init__(quoridor, "configs/gamescene/custom.json", "./assets/page2/background3.jpg")
        pass
    
    def LoadCustomConfig(self, json):
        json = CheckJson(json)
        