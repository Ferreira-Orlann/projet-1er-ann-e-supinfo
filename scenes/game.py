from scenes.scenebase import SceneBase
from math import ceil
import pygame

class GameScene(SceneBase):
    def __init__(self, screen, quoridor, configscene):
        SceneBase.__init__(self)
        self.__screen = screen
        self.__quoridor = quoridor
        self.__configscene = configscene
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255,255,255))
        if not self.__game: 
            self.__configscene.Render(screen)
            return
        
        
    def SetGame(self, game):
        self.__game = game
        del self.__configscene