from render.scene.gamescene import GameScene
from network.client import NetClient

class NetworkedGameScene(GameScene):
    def __init__(self, quoridor, game, background=None):
        super().__init__(quoridor, game, background)
        self.__client = NetClient(quoridor)
        self.__client.AddAction("init_data", self.InitData)
    
    def InitData(self):
        self