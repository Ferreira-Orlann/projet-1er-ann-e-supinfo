from render.scene.basescene import BaseScene
from render.scene.configscene import ConfigScene
from json import load as json_load

class StartScene(BaseScene):
    def __init__(self, display_surface):
        super().__init__(display_surface, "configs/startscene.json")
        pass
    
    def Play(self, button):
        self.Next(ConfigScene(self.GetDisplaySurface()))