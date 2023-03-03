from scenes.scenebase import SceneBase
from math import ceil, floor
from utils import RoundUP
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
                pos = event.pos
                print((floor(pos[0]/50),floor(pos[1]/50)))
                pass
            
    def PosEquals(posone, postwo):
        return True

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255,255,255))
        if not self.__game: 
            self.__configscene.Render(screen)
            return
        
        # Affichage des Position
        for i in range(0,9):
            for y in range(0,9):
                pygame.draw.rect(screen, (255,0,255), pygame.Rect(y * 50 + 10 , i * 50 + 10,50,50))
        
        # Affichage des barrières
        barrers = self.__game.GetBarrers()
        lenfirst = len(barrers[0])
        a = 0
        b = 0
        for i in range(0,len(barrers)):
            if (i % 2 == 0):
                for y in range(0,lenfirst):
                # Vertical Barriers
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(y * 50 + 50, a * 50 + 10 ,10,50))
                a = a + 1
            else:
                #  Barriers
                # pygame.Rect(0,0,25,100)
                for y in range(0,lenfirst+1):
                    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(i * 70 + 5, 10 + i * 50,70,10))
                    pygame.draw.rect(screen, (0,0,255), pygame.Rect(y * 50 + 10 , b * 50 + 10 + 50,50,10))
                b = b + 1
                        
    def SetGame(self, game):
        self.__game = game
        del self.__configscene