from render.scene.basescene import BaseScene
from render.scene.configscene import ConfigScene

class StartScene(BaseScene):
    def __init__(self, quoridor):
        super().__init__(quoridor, "configs/startscene.json")
        pass
    
    def Play(self, button):
        self.Next(ConfigScene(self.GetQuoridor()))