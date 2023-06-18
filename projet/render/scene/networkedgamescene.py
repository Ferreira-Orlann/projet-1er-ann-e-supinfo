from render.scene.gamescene import GameScene
from network.client import NetClient
from pygame.transform import scale
import json

class NetworkedGameScene(GameScene):
    def __init__(self, quoridor, game, addr, background=None):
        super().__init__(quoridor, game, background)
        self.__client = NetClient(quoridor)
        self.__client.AddAction("init_data", self.InitData)
        self.__client.AddAction("place_barrer", self.PlaceBarrer)
        self.__client.AddAction("player_move", self.PlayerMove)
        self.__initalized = False
        self.__local_player = None
        self.__client.Connect
        
    def PlaceBarrer(self, data):
        self.__game.ProcessBarrer(tuple(data["pos_one"]), tuple(data["pos_two"]))
        self.SetBarrerCount(self.GetBarrerCount() - 1)
        self.ChangePossiblesSprites()
        return True
    
    def PlayerMove(self, data):
        pid = self.__game.GetCurrentPlayer().GetId()
        pos = tuple(data["pos"])
        self.__game.ProcessMove(pos)
        button = self.GetSpriteById(pos, "players")
        sprite = self.GetSpriteById(pid, "players")
        sprite.SetPos(button.GetPos())
        self.ChangePossiblesSprites()
    
    def InitData(self, data):
        game = self.GetGame()
        game.SetBarrerData(data["barrers"])
        game.SetCPlayer(data["cplayer"])
        self.__local_player = data["local_player"]
        game.SetBarrerCount(data["barrer_count"])
        self.ChangePossiblesSprites()
        sur_manager = self.GetQuoridor().GetSurfaceManager()
        sid
        surface_up = scale(sur_manager.GetSurface(self.GetJson()["barrerup_posed"][1]), (10, 50))
        surface = scale(sur_manager.GetSurface(self.GetJson()["barrer_posed"][1]), (50, 10))
        for sprite in self.GetSpriteGroup("barrers"):
            sid = sprite.GetId()
            if (game.IsPosed(sid)):
                if (sid[0] % 2 == 0):
                    sprite.ChangeSurface(surface_up)
                else:
                    sprite.ChangeSurface(surface)
        players = self.GetSpriteGroup("players")
        for player in players:
            pid = player.GetId()
            gplayer = game.GetPlayer(pid)
            pos = tuple(data["players_pos"][player.GetId()])
            gplayer.SetPos(pos)
            sprite = self.GetSpriteById(pos, "board_case")
            player.SetPos(sprite.GetPos())
        self.__initalized = True
        
    def ChangePossiblesSprites(self):
        sur_manager = self.__quoridor.GetSurfaceManager()
        json = self.GetJson()
        if (not self.CheckLocalPlayer):
            for sprite in self.GetLastPossiblesMovesSprites():
                sprite.ChangeSurface(sur_manager.GetSurface(json["board_case_possible"][1]))
            self.ClearLastPossiblesMovesSprites()
            return
        super().ChangePossiblesSprites()
        
    def CheckLocalPlayer(self):
        if (self.__local_player is None): return False
        if (self.__local_player != self.GetGame().GetCPlayer()): return False
        return True
    
    def PlayerCaseClick(self, button):
        if (not self.CheckLocalPlayer() or not self.__initalized): return
        if(super().PlayerCaseClick(button)):
            self.__client.GetStocking().write(json.dumps({
                "action": "player_move",
                "pos": button.GetPos()
            }))
        
    def PlayerBarrerClick(self, button):
        if (not self.CheckLocalPlayer() or not self.__initalized): return
        next_barrer = self.GetBarrerByDirection(self.GetLastHoveredBarrer(), self.GetDirection())
        if (super().PlayerBarrerClick(button)):
            self.__client.GetStocking().write(json.dumps({
                "action": "place_barrer",
                "pos_one": button.GetId(),
                "pos_two": next_barrer.GetId()
            }))