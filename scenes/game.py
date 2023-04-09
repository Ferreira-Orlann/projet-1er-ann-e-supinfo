from scenes.scenebase import SceneBase
from math import floor
from render.barrerpart import BarrerPart
import pygame

class GameScene(SceneBase):
    def __init__(self, screen, quoridor, configscene):
        SceneBase.__init__(self, screen)
        self.__screen = screen
        self.__quoridor = quoridor
        self.__configscene = configscene
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            game = self.__game
            if event.type == pygame.MOUSEBUTTONDOWN:
                barrer = self.__crbarrer
                guipos = event.pos
                if barrer != None and barrer.collidepoint(guipos) and not barrer.IsPosed():
                    game.ProcessBarrer(barrer.GetPos())
                    barrer.SetPosed(True)
                    return
                gridpos = (floor(guipos[1]/50),floor(guipos[0]/50))
                if gridpos[0] == 9 or gridpos[1] == 9:
                    return
                game.ProcessMove(gridpos)
                
    def PostGameInit(self):
        game = self.__game
        rectangles = []
        barrers = game.GetBarrers()
        lenfirst = len(barrers[0])
        a = 0
        b = 0
        for i in range(0,len(barrers)):
            if (i % 2 == 0):
                for y in range(0,lenfirst):
                # Vertical Barriers
                    rectangles.append(BarrerPart(y * 50 + 50, a * 50 + 10 ,10,50).SetVertical(True).SetPos((i,y)))
                a = a + 1
            else:
                # Barriers
                # pygame.Rect(0,0,25,100)
                for y in range(0,lenfirst+1):
                    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(i * 70 + 5, 10 + i * 50,70,10))
                    rectangles.append(BarrerPart(y * 50 + 10 , b * 50 + 10 + 50,50,10).SetPos((i,y)))
                b = b + 1
        self.__barrers_rectangles = rectangles
        pass   
                         
    def SetGame(self, game):
        self.__game = game
        self.PostGameInit()
        self.Update()
        del self.__configscene

    def Update(self):
        self.ProcessBarrersRectangles()
        pos = pygame.mouse.get_pos()
        for i in range(0, len(self.__barrers_rectangles)):
            rect = self.__barrers_rectangles[i]
            if rect.collidepoint(pos):
                self.__crbarrer = rect
                self.FullRender()
                return
        self.__crbarrer = None
        pass
    
    def Render(self, screen):
        self.FirstRender(screen)
        pass

    def FirstRender(self, screen):
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
        for i in range(0,len(self.__barrers_rectangles)):
            barrer = self.__barrers_rectangles[i]
            color = (0,0,255)
            print(barrer.IsPosed())
            if barrer.IsPosed():
                color = (0,0,0)
            pygame.draw.rect(screen, color, barrer)
        if self.__crbarrer != None:
            pygame.draw.rect(screen, (100,100,100), self.__crbarrer)
            
        # Affichage positions des joueurs
        list_players_pos = list(map(lambda player: player.GetPos(), game.GetPlayers()))
        colors = [(255, 0, 0), (117,59,97), (249, 255, 77), (255, 147, 0)] # liste de couleurs
        for i in range(len(list_players_pos)):
            pos = list_players_pos[i]
            color = colors[i % len(colors)] 
            pygame.draw.circle(screen, color, (pos[1] * 50 + 10 + 25, pos[0] * 50 + 10 + 25), 5)

        
    def ProcessBarrersRectangles(self):
        game = self.__game
        if not game.HasChanged():
            return
        self.FullRender()
        game.SetChanged(False)