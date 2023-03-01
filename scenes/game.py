from scenes.scenebase import SceneBase
from math import floor
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
                guipos = event.pos
                gridpos = (floor(guipos[1]/50),floor(guipos[0]/50))
                if gridpos[0] == 9 or gridpos[1] == 9:
                    return
                self.__game.ProcessMove(gridpos,self.__game.GetCurrentPlayer())
            
    def PosEquals(posone, postwo):
        return True

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255,255,255))
        if not self.__game: 
            self.__configscene.Render(screen)
            return
        game = self.__game
        
        # Affichage des Position
        
        possibles_moves = game.GetPossiblesMoves()
        for i in range(0,9):
            for y in range(0,9):
                if (i, y) in possibles_moves:
                    pygame.draw.rect(screen, (255,0,255), pygame.Rect(y * 50 + 10 , i * 50 + 10,50,50))
                else:
                    pygame.draw.rect(screen, (0,255,0), pygame.Rect(y * 50 + 10 , i * 50 + 10,50,50))
        
        # Affichage des barrières
        barrers = game.GetBarrers()
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
                
        list_players_pos = mapped_numbers = list(map(lambda player: player.GetPos(), game.GetPlayers()))
        for i in range(len(list_players_pos)):
            i = list_players_pos[i]
            pygame.draw.circle(screen, (255,0,0), (i[1] * 50 + 10 + 25, i[0] * 50 + 10 + 25), 5)
                        
    def SetGame(self, game):
        self.__game = game
        del self.__configscene