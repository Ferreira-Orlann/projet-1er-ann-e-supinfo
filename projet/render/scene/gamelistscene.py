from render.scene.basescene import BaseScene
from network.client import NetClient
from render.server_info import ServerInfo
from render.textentry import TextEntry
from render.scene.networkedgamescene import NetworkedGameScene
from game.game import Game
import json
import settings
from time import sleep
from network.client import NetClient

class GameListScene(BaseScene):
    def __init__(self, quoridor):
        super().__init__(quoridor, "configs/gamelistscene.json")
        self.__area = TextEntry("direct_connect", 100,700,self,self.GetQuoridor().GetFontManager().GetFont("server_info"))
        self.__area.SetText("127.0.0.1:50001")
        self.RegisterSprite(self.__area)
        self.__client = NetClient(quoridor)
        self.__client.AddAction("ping", self.Ping)
        self.__client.AddAction("retreive_servers", self.RetreiveServers)
        self.__current_group = self.AddSpriteGroup("page_1")
        try:
            self.__client.Connect(settings.SERVER_LIST_IP, settings.SERVER_LIST_PORT)
            self.__resfesh = []
            self.__start_pos = (100,100)
            while self.__client.GetStocking().handshakeComplete is not True:
                sleep(0.1)
            self.__client.GetStocking().write(json.dumps({
                "action": "retreive_servers"
            }))
        except:
            ...
            
    def ConnectPrivate(self, button):
        addr = self.__area.GetText().split(":")
        addr[1] = int(addr[1])
        client = NetClient(self.GetQuoridor())
        try:
            def PrivatePing(data):
                    settings.NB_BARRERS = data["nb_barrer"]
                    settings.BOARD_SIZE = data["board_size"]
                    settings.NB_PLAYERS = data["max_player"]
                    client.Disconnect()
                    q = self.GetQuoridor()
                    g = Game(q)
                    scene = NetworkedGameScene(q, g, tuple(addr))
                    self.Next(scene)
            client.AddAction("ping", PrivatePing)
            client.Connect(addr[0], addr[1])
            while client.GetStocking().handshakeComplete is not True:
                sleep(0.1)
            client.GetStocking().write(json.dumps({
                "action": "ping"
            }))
        except:
            from render.scene.startscene import StartScene
            self.Next(StartScene(self.GetQuoridor()))
            
    def RetreiveServers(self, data):
        self.__resfesh = data["servers"]
        self.__client.GetStocking().write(json.dumps({
            "action": "ping"
        }))
        
    def Ping(self, data):
        sprite = self.GetSpriteById(data["addr"], "servers")
        if (sprite != None and isinstance(sprite,ServerInfo)):
            sprite.SetData(data)
        else:
            self.AddServer(data)
            
    def CreatePage(self):
        idx = self.GetNameByGroup(self.__current_group)
        idx = idx.split("_")

    def Render(self, display_surface):
        """Render the scene"""
        rects = []
        rects.extend(self.GetMainGroup().draw(display_surface))
        rects.extend(self.__current_group.draw(display_surface))
        return rects
        
    def AddServer(self, data):
        if (len(self.__current_group.sprites() >= 20)):
            self.CreatePage()
        server_info = ServerInfo(data["addr"], self.__start_pos[0]+(20*len(self.__current_group)), self, self.GetQuoridor().GetFontManager().GetFont("server_info"))
        self.RegisterSprite(server_info, None, True)
        
    def RefreashServer(self, ip):
        ...
    def ServerSelected(self, button):
        ...