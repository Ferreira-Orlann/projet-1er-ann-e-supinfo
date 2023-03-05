from json import load as json_load
from render.scene.basescene import BaseScene

class ConfigScene(BaseScene):
    def __init__(self, display_surface):
        file = open("configs/configscene.json", "r")
        self.__json_config = json_load(file)
        file.close()
        super().__init__("./assets/page2/background3.jpg", display_surface, self.__json_config)
    
    def Reset(self, button):
        print(button)
        
    def Button(self, button):
        print(self)