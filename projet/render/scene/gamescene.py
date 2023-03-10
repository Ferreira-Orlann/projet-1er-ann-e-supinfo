from render.scene.basescene import BaseScene
from projet.utils import CheckJson

class GameScene(BaseScene):
    def __init__(self, display_surface, game):
        super().__init__("./assets/page2/background3.jpg", display_surface, "configs/gamescene/custom.json")
        pass
    
    def LoadCustomConfig(self, json):
        json = CheckJson(json)
        