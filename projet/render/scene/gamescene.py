from render.scene.basescene import BaseScene
from utils import CheckJson
from render.buttons import Button
from pygame import K_r as KEY_R
import settings


class GameScene(BaseScene):
    def __init__(self, quoridor, game, background=None):
        self.__game = game
        self.__hovered_barrers = (None, None)
        self.__direction = False
        self.__quoridor = quoridor
        self.__display_surface = quoridor.GetDisplaySurface()
        self.__last_possibles_moves  = []
        json = CheckJson("configs/gamescene/custom.json")
        super().__init__(quoridor, json, background)
        self.AddSpriteGroup("players")
        self.AddSpriteGroup("board_case")
        self.AddSpriteGroup("barrers")
        self.__players_surfaces = []
        self.LoadGameMapJson(json)
        self.LoadGameJson(json)
        self.LoadGameUpJson(json)
        self.LoadCustomPlayerJson(json)
        self.ChangePossiblesSprites()

    def InputPressed(self, key):
        if key == KEY_R:
            self.__direction = not self.__direction

    def LoadCustomPlayerJson(self, json):
        """Load the custom player json"""
        player = settings.NB_PLAYERS
        if player == 2:
            self.LoadCustomJauneJson(json)
            self.LoadCustomRougeJson(json)
        if player == 4:
            self.LoadCustomJauneJson(json)
            self.LoadCustomRougeJson(json)
            self.LoadCustomOrangeJson(json)
            self.LoadCustomVertJson(json)

    def CenterBoard(self):
        #DISPLAY_SIZE = (1160,920)
        if settings.BOARD_SIZE == 5:
            return 450, 330
        if settings.BOARD_SIZE == 7:
            return 397, 277
        if settings.BOARD_SIZE == 9:
            return 344, 224
        if settings.BOARD_SIZE == 11:
            return 291, 171

    def LoadCustomJauneJson(self, json):
        """Load the custom yellow player json """
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for id in range(0, 1, 1):
            pdata=json["playersjaune"]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [2+x+((settings.BOARD_SIZE//2)*60), 2+y+((settings.BOARD_SIZE-1)*60)],
                "action": "PlayerClick"
            }, "players")
            x = x + 1
    def LoadCustomRougeJson(self, json):
        """Load the custom red player json"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for id in range(0, 1, 1):
            pdata=json["playersrouge"]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45,45],
                "pos": [2+x+((settings.BOARD_SIZE//2)*60), y+2],
                "action": "PlayerClick"
            }, "players")
            x = x + 1

    def LoadCustomOrangeJson(self, json):
        """Load the custom orange player json"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for id in range(0, 1, 1):
            pdata=json["playersorange"]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45, 45],
                "pos": [2+x, 2+y+((settings.BOARD_SIZE//2)*60)],
                "action": "PlayerClick"
            }, "players")
            x = x + 1

    def LoadCustomVertJson(self, json):
        """Load the custom green player json"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for id in range(0, 1, 1):
            pdata=json["playersvert"]
            self.RegisterButton(Button, str(id),{
                "path": pdata[1],
                "size": [45, 45],
                "pos": [2+x+((settings.BOARD_SIZE-1)*60), 2+y+((settings.BOARD_SIZE//2)*60)],
                "action": "PlayerClick"
            }, "players")
            x = x + 1
        
    def PlayerCaseClick(self, button):
        """Player click on the board"""
        self.GetQuoridor().GetConsole().log("PlayerCaseClick " + str(button.GetId()))
        if(not self.__game.ProcessMove(button.GetId())): return
        sur_manager = self.__quoridor.GetSurfaceManager()
        print(button.GetId())
        self.ChangePossiblesSprites()

    def GetSpriteById(self, ids, group = "default"):
        returnList = []
        g = self.GetSpriteGroup(group)
        print(g)
        for sprite in g:
            print(sprite.GetId())
            print("TEST")
            if (sprite.GetId() in ids):
                returnList.append(sprite)
        return returnList
    
    def ChangePossiblesSprites(self):
        pmove = self.__game.GetPossiblesMoves()
        print(pmove)
        sprites = self.GetSpriteById(pmove, "board_case")
        print(sprites)
        sur_manager = self.__quoridor.GetSurfaceManager()
        json = self.GetJson()
        for sprite in sprites:
            if (sprite in self.__last_possibles_moves):
                continue
            sprite.ChangeSurface(sur_manager.GetSurface(json["board_case_possible"][1]))
        for sprite in self.__last_possibles_moves:
            if (sprite in sprites):
                continue
            sprite.ChangeSurface(sur_manager.GetSurface(json["board_case"][1]))

    def PlayerClick(self, button):
        self.GetQuoridor().GetConsole().log("PlayerClick " + str(button.GetId()))

    def PlayerBarrerClick(self, button):
        if(not self.__game.ProcessBarrer(button.GetId())): return
        sur_manager = self.__quoridor.GetSurfaceManager()
        button.ChangeSurface(sur_manager.GetSurface(self.GetJson()["barrerup_posed"][1]))
        self.ChangePossiblesSprites()

    def LoadGameJson(self, json):
        """Load the custom game json --"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        k = 0
        for i in range(0, settings.BOARD_SIZE, 1):
            for j in range(1, settings.BOARD_SIZE, 1):
                pdata = json["barrer"]
                self.RegisterButton(Button, (i,k), {
                    "path": pdata[1],
                    "size": [50, 10],
                    "pos": [60*i+x, 60*j+y-10],
                    "action": "PlayerBarrerClick"
                }, "barrers")
            k+=2
                    
    def LoadGameUpJson(self, json):
        """Load the custom game json || """
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for i in range(1,settings.BOARD_SIZE,1):
            k = 0
            for j in range(0,settings.BOARD_SIZE,1):
                pdata = json["barrerup"]
                self.RegisterButton(Button, (i-1,k),{
                    "path": pdata[1],
                    "size": [10, 50],
                    "pos": [60*i+x-10, 60*j+y],
                    "action": "PlayerBarrerClick"
                }, "barrers")
                k+=2

    def LoadGameMapJson(self, json):
        """Load the custom game json"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for i in range(0, settings.BOARD_SIZE, 1):
            for j in range(0, settings.BOARD_SIZE, 1):
                pdata = json["board_case"]
                self.RegisterButton(Button, (j,i),{
                    "path": pdata[1],
                    "size": [50, 50],
                    "pos": [60*i+x, 60*j+y],
                    "action": "PlayerCaseClick"
                }, "board_case")

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