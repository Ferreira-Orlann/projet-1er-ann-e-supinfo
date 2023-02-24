from scenes.scenebase import SceneBase
from math import ceil
import pygame

class GameScene(SceneBase):
    def __init__(self, screen, quoridor):
        SceneBase.__init__(self)
        self.__screen = screen
        self.__quoridor = quoridor
        
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def Update(self):
        pass

    def Render(self, screen):
        self.__screen.fill((255,255,255))
        pass
    
    def SetGame(self, game):
        self.__game = game