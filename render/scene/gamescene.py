from render.scene.basescene import BaseScene
from utils import CheckJson

class GameScene(BaseScene):
    def __init__(self, display_surface, game):
        pass
    
    def LoadCustomConfig(self, json):
        json = CheckJson(json)
        