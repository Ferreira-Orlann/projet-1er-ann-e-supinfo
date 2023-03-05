import pygame
from json import load as json_load
from render.scene.basescene import BaseScene
from render.buttons import Button, ToggleButton

class ConfigScene(BaseScene):
    def __init__(self, display_surface):
        file = open("configs/configpage.json", "r")
        self.__json_config = json_load(file)
        file.close()
        super().__init__("./assets/page2/background3.jpg", display_surface, self.__json_config)
    
    def Toggle(self):
        print(self)