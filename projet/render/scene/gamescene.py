from render.scene.basescene import BaseScene
from render.barrerpart import BarrerPart
from math import floor
from utils import CheckJson
from rich import inspect
from render.buttons import Button
import settings

class GameScene(BaseScene):
    def __init__(self, quoridor, game):
        super().__init__(quoridor, "configs/gamescene/gamescene.json")
        inspect(obj=game, methods=True)
        self.LoadGameMapJson("configs/gamescene/custom.json")
        self.LoadGameJson("configs/gamescene/custom.json")
        self.LoadGameUpJson("configs/gamescene/custom.json")
        self.LoadCustomPlayerJson("configs/gamescene/custom.json")


    def LoadCustomPlayerJson(self, json):
        """Load the custom player json"""
        json = CheckJson(json)
        player = settings.NB_PLAYERS
        if player == 2:
            self.LoadCustomJauneJson("configs/gamescene/custom.json")
            self.LoadCustomRougeJson("configs/gamescene/custom.json")
        if player == 4:
            self.LoadCustomJauneJson("configs/gamescene/custom.json")
            self.LoadCustomRougeJson("configs/gamescene/custom.json")
            self.LoadCustomOrangeJson("configs/gamescene/custom.json")
            self.LoadCustomVertJson("configs/gamescene/custom.json")

    def LoadCustomJauneJson(self, json):
        """Load the custom yellow player json """
        json = CheckJson(json)
        x = 130
        for id in range(0, 1, 1):
            pdata=json["playersjaune"][id]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [100+x+((settings.BOARD_SIZE//2)*60),100+x+((settings.BOARD_SIZE-1)*60)],
                "action": "PlayerClick"
            })
            x = x + 1
    def LoadCustomRougeJson(self, json):
        """Load the custom red player json"""
        json = CheckJson(json)
        x = 130
        for id in range(0, 1, 1):
            pdata=json["playersrouge"][id]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [100+x+((settings.BOARD_SIZE//2)*60),100+x],
                "action": "PlayerClick"
            })
            x = x + 1

    def LoadCustomOrangeJson(self, json):
        """Load the custom orange player json"""
        json = CheckJson(json)
        x = 130
        for id in range(0, 1, 1):
            pdata=json["playersorange"][id]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [100+x,100+x+((settings.BOARD_SIZE//2)*60)],
                "action": "PlayerClick"
            })
            x = x + 1

    def LoadCustomVertJson(self, json):
        """Load the custom green player json"""
        json = CheckJson(json)
        x = 130
        for id in range(0, 1, 1):
            pdata=json["playersvert"][id]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [100+x+((settings.BOARD_SIZE-1)*60),100+x+((settings.BOARD_SIZE//2)*60)],
                "action": "PlayerClick"
            })
            x = x + 1
        
    def PlayerCaseClick(self, button):
        """Player click on the board"""
        self.GetQuoridor().GetConsole().log("PlayerClick " + str(button.GetId()))

    def PlayerClick(self, button):
        pass

    def PlayerBarrerClick(self, button):
        pass

    def LoadGameJson(self, json):
        """Load the custom game json"""
        json = CheckJson(json)
        x = 225
        for i in range(0, settings.BOARD_SIZE, 1):
            for j in range(1, settings.BOARD_SIZE, 1):
                for id in range(0, len(json["barrer"])):
                    pdata = json["barrer"][id]
                    self.RegisterButton(Button, str(id), {
                        "path": pdata[1],
                        "size": [50, 10],
                        "pos": [60*i+x+5, 60*j+x-5],
                        "action": "PlayerBarrerClick"
                    })
                    
    def LoadGameUpJson(self, json):
        """Load the custom game json"""
        json = CheckJson(json)
        x=230
        for i in range(1,settings.BOARD_SIZE-1,1):
            k = 0
            for j in range(0,settings.BOARD_SIZE,1):
                pdata = json["barrerup"][0]
                self.RegisterButton(Button, (i,k),{
                    "path": pdata[1],
                    "size": [10, 50],
                    "pos": [60*i+x-10, 60*j+x],
                    "action": "PlayerBarrerClick"
                })
                k+=2
                    
    def LoadGameMapJson(self, json):
        """Load the custom game json"""
        json = CheckJson(json)
        x = 230
        for i in range(0, settings.BOARD_SIZE, 1):
            for j in range(0, settings.BOARD_SIZE, 1):
                pdata = json["board_case"][0]
                self.RegisterButton(Button, (i,j),{
                    "path": pdata[1],
                    "size": [50, 50],
                    "pos": [60*i+x, 60*j+x],
                    "action": "PlayerCaseClick"
                })

    # def LoadCustomConfig(self, json):
    #     json = CheckJson(json)
        
    
    # def ProcessInput(self, events):
    #     for event in events:
    #         game = self.__game
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             barrer = self.__crbarrer
    #             guipos = event.pos
    #             if barrer != None and barrer.collidepoint(guipos) and not barrer.IsPosed():
    #                 game.ProcessBarrer(barrer.GetPos())
    #                 barrer.SetPosed(True)
    #                 return
    #             gridpos = (floor(guipos[1]/50),floor(guipos[0]/50))
    #             if gridpos[0] == 9 or gridpos[1] == 9:
    #                 return
    #             game.ProcessMove(gridpos)
                
    # def PostGameInit(self):
    #     game = self.__game
    #     rectangles = []
    #     barrers = game.GetBarrers()
    #     lenfirst = len(barrers[0])
    #     a = 0
    #     b = 0
    #     for i in range(0,len(barrers)):
    #         if (i % 2 == 0):
    #             for y in range(0,lenfirst):
    #             # Vertical Barriers
    #                 rectangles.append(BarrerPart(y * 50 + 50, a * 50 + 10 ,10,50).SetVertical(True).SetPos((i,y)))
    #             a = a + 1
    #         else:
    #             # Barriers
    #             # pygame.Rect(0,0,25,100)
    #             for y in range(0,lenfirst+1):
    #                 # pygame.draw.rect(screen, (0,0,0), pygame.Rect(i * 70 + 5, 10 + i * 50,70,10))
    #                 rectangles.append(BarrerPart(y * 50 + 10 , b * 50 + 10 + 50,50,10).SetPos((i,y)))
    #             b = b + 1
    #     self.__barrers_rectangles = rectangles
    #     pass         
    # def SetGame(self, game):
    #     self.__game = game
    #     self.PostGameInit()
    #     self.Update()
    #     del self.__configscene

    # def Update(self):
    #     self.ProcessBarrersRectangles()
    #     pos = pygame.mouse.get_pos()
    #     for i in range(0, len(self.__barrers_rectangles)):
    #         rect = self.__barrers_rectangles[i]
    #         if rect.collidepoint(pos):
    #             self.__crbarrer = rect
    #             self.FullRender()
    #             return
    #     self.__crbarrer = None
    #     pass
    
    # def Render(self, screen):
    #     self.FirstRender(screen)
    #     pass

    # def FirstRender(self, screen):
    #     screen.fill((255,255,255))
    #     if not self.__game: 
    #         self.__configscene.Render(screen)
    #         return
    #     game = self.__game
        
    #     # Affichage des Position
    #     possibles_moves = game.GetPossiblesMoves()
    #     for i in range(0,9):
    #         for y in range(0,9):
    #             if (i, y) in possibles_moves:
    #                 pygame.draw.rect(screen, (255,0,255), pygame.Rect(y * 50 + 10 , i * 50 + 10,50,50))
    #             else:
    #                 pygame.draw.rect(screen, (0,255,0), pygame.Rect(y * 50 + 10 , i * 50 + 10,50,50))
        
    #     # Affichage des barrières
    #     for i in range(0,len(self.__barrers_rectangles)):
    #         barrer = self.__barrers_rectangles[i]
    #         color = (0,0,255)
    #         print(barrer.IsPosed())
    #         if barrer.IsPosed():
    #             color = (0,0,0)
    #         pygame.draw.rect(screen, color, barrer)
    #     if self.__crbarrer != None:
    #         pygame.draw.rect(screen, (100,100,100), self.__crbarrer)
            
    #     # Affichage positions des joueurs
    #     list_players_pos = list(map(lambda player: player.GetPos(), game.GetPlayers()))
    #     for i in range(len(list_players_pos)):
    #         i = list_players_pos[i]
    #         pygame.draw.circle(screen, (255,0,0), (i[1] * 50 + 10 + 25, i[0] * 50 + 10 + 25), 5)
        
    # def ProcessBarrersRectangles(self):
    #     game = self.__game
    #     if not game.HasChanged():
    #         return
    #     self.FullRender()
    #     game.SetChanged(False)