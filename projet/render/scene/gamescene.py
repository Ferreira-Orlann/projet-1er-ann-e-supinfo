from render.scene.basescene import BaseScene
from utils import CheckJson
from render.buttons import Button
from pygame import K_r as KEY_R
import settings
from pygame.transform import scale
from render.label import Label

class GameScene(BaseScene):
    def __init__(self, quoridor, game, background=None):
        self.__game = game
        self.__hovered_barrers = (None, None)
        self.__direction = False
        self.__quoridor = quoridor
        self.__display_surface = quoridor.GetDisplaySurface()
        self.__last_possibles_moves  = []
        self.__last_hovered_barrer = None
        self.__barrers_count = settings.NB_BARRERS
        json = CheckJson("configs/gamescene/custom.json")
        super().__init__(quoridor, json, background)
        self.AddSpriteGroup("players")
        self.AddSpriteGroup("board_case")
        self.AddSpriteGroup("barrers")
        data = json["barrer_count_label"]
        self.__barrers_count_label = self.RegisterSprite(Label("barrer_count_label", data[0], data[1], self, self.__quoridor.GetFontManager().GetFont("barrer_count_label")))
        self.__barrers_count_label.SetText(str(self.__barrers_count))
        self.__players_surfaces = []
        self.LoadGameMapJson(json)
        self.LoadGameJson(json)
        self.LoadGameUpJson(json)
        self.LoadCustomPlayerJson(json)
        self.ChangePossiblesSprites()

    def InputPressed(self, key):
        if key == KEY_R:
            self.ChangeDirection()
            
    def ChangeDirection(self):
        sur_manager = self.__quoridor.GetSurfaceManager()
        if (self.__last_hovered_barrer is not None):
            next_barrer = self.GetBarrerByDirection(self.__last_hovered_barrer, self.__direction)
            game = self.__game
            if (game.IsPosed(self.__last_hovered_barrer.GetId()) or game.IsPosed(next_barrer.GetId())):
                surface = None
                if (self.__last_hovered_barrer.GetId()[0] % 2 == 0):
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrerup"][1]), (10, 50))
                else:
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrer"][1]), (50, 10))
                self.__last_hovered_barrer.ChangeSurface(surface)
                next_barrer.ChangeSurface(surface)
                self.__last_hovered_barrer = None
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
            self.RegisterButton(Button, 1,{
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
            self.RegisterButton(Button, 0,{
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
            self.RegisterButton(Button, 2,{
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
            self.RegisterButton(Button, 3,{
                "path": pdata[1],
                "size": [45, 45],
                "pos": [2+x+((settings.BOARD_SIZE-1)*60), 2+y+((settings.BOARD_SIZE//2)*60)],
                "action": "PlayerClick"
            }, "players")
            x = x + 1
        
    def PlayerCaseClick(self, button):
        """Player click on the board"""
        self.GetQuoridor().GetConsole().log("PlayerCaseClick " + str(button.GetId()))
        pid = self.__game.GetCurrentPlayer().GetId()
        if(not self.__game.ProcessMove(button.GetId())): return
        sur_manager = self.__quoridor.GetSurfaceManager()
        sprite = self.GetSpriteById(pid, "players")
        sprite.SetPos(button.GetPos())
        self.ChangePossiblesSprites()
    
    def ChangePossiblesSprites(self):
        pmove = self.__game.GetPossiblesMoves()
        sprites = self.GetSpritesById(pmove, "board_case")
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
        self.__last_possibles_moves = sprites

    def PlayerClick(self, button):
        self.GetQuoridor().GetConsole().log("PlayerClick " + str(button.GetId()))

    def SpriteHover(self, sprite):
        group = self.GetSpriteGroup("barrers")
        if (group is not None):
            if (sprite == self.__last_hovered_barrer or sprite not in group): return
            sur_manager = self.__quoridor.GetSurfaceManager()
            game = self.__game
            if (self.__last_hovered_barrer is not None):
                next_barrer = self.GetBarrerByDirection(self.__last_hovered_barrer, self.__direction)
                surface = None
                if (self.__last_hovered_barrer.GetId()[0] % 2 == 0):
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrerup"][1]), (10, 50))
                else:
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrer"][1]), (50, 10))
                if (game.IsPosed(self.__last_hovered_barrer.GetId())):
                    self.__last_hovered_barrer.ChangeSurface(surface)
                if (game.IsPosed(next_barrer.GetId())):
                    next_barrer.ChangeSurface(surface)
            next_barrer = self.GetBarrerByDirection(sprite, self.__direction)
            if (next_barrer is None):
                self.ChangeDirection()
                return
            if (game.IsPosed(sprite.GetId()) and game.IsPosed(next_barrer.GetId())):
                if (sprite.GetId()[0] % 2 == 0):
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrerup_posed"][1]), (10, 50))
                else:
                    surface = scale(sur_manager.GetSurface(self.GetJson()["barrer_posed"][1]), (50, 10))
                sprite.ChangeSurface(surface)
                next_barrer.ChangeSurface(surface)
                self.__last_hovered_barrer = sprite

    def GetBarrerByDirection(self, start_barrer, direction):
        next_barrer = None
        if (start_barrer.GetId()[0] % 2 != 0):
            if (direction): # Gauche
                id = start_barrer.GetId()
                next_barrer = self.GetSpriteById((id[0], id[1] + 1), "barrers")
            else: # Droite
                id = start_barrer.GetId()
                next_barrer = self.GetSpriteById((id[0], id[1] - 1), "barrers")
        else: 
            if (direction): # Haut
                id = start_barrer.GetId()
                next_barrer = self.GetSpriteById((id[0] - 2, id[1]), "barrers")
            else: # Bas
                id = start_barrer.GetId()
                next_barrer = self.GetSpriteById((id[0] + 2, id[1]), "barrers")
        return next_barrer
            
    def PlayerBarrerClick(self, button):
        if (self.__barrers_count <= 0 or self.__last_hovered_barrer != button): return
        next_barrer = self.GetBarrerByDirection(self.__last_hovered_barrer, self.__direction)
        if (not self.__game.ProcessBarrer(self.__last_hovered_barrer.GetId(), next_barrer.GetId())): return
        self.ChangePossiblesSprites()
        self.__barrers_count -= 1
        self.__barrers_count_label.SetText(str(self.__barrers_count))

    def LoadGameJson(self, json):
        """Load the custom game json --"""
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for i in range(0, settings.BOARD_SIZE, 1):
            for j in range(1, settings.BOARD_SIZE, 1):
                pdata = json["barrer"]
                self.RegisterButton(Button, (j*2-1,i), {
                    "path": pdata[1],
                    "size": [50, 10],
                    "pos": [60*i+x, 60*j+y-10],
                    "action": "PlayerBarrerClick"
                }, "barrers")

    def LoadGameUpJson(self, json):
        """Load the custom game json || """
        json = CheckJson(json)
        x, y = self.CenterBoard()
        for i in range(1,settings.BOARD_SIZE,1):
            k = 0
            for j in range(0,settings.BOARD_SIZE,1):
                pdata = json["barrerup"]
                self.RegisterButton(Button, (k,i-1),{
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