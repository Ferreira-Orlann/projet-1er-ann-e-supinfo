from scenes.scenebase import SceneBase
from scenes.config import SceneConfig
from math import ceil
import pygame

class SceneRule(SceneBase):
    def __init__(self, screen, quoridor):
        self.__quoridor = quoridor
        SceneBase.__init__(self)

    def ProcessInput(self, events, keys, screen):
        for event in events:
            pass
        
    def Update(self):
        pass

    def Render(self, screen):
        pass