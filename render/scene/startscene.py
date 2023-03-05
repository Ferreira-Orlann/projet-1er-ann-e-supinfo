from render.scene.basescene import BaseScene
from render.scene.configscene import ConfigScene
from render.buttons import Button
from json import load as json_load

class StartScene(BaseScene):
    def __init__(self, display_surface):
        file = open("configs/startscene.json", "r")
        self.__json_config = json_load(file)
        file.close()
        super().__init__("./assets/page1/background1.jpg", display_surface, self.__json_config)
        pass
    
    def Play(self, button):
        self.Next(ConfigScene(self.GetDisplaySurface()))