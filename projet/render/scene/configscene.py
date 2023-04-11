from json import load as json_load
from render.scene.basescene import BaseScene
from render.scene.gamescene import GameScene
from render.scene.gamelistscene import GameListScene
from game.game import Game
import settings as settings

class ConfigScene(BaseScene):
    def __init__(self, quoridor):
        self.__board_size = None
        self.__nbplayers = None
        self.__nbbarrers = None
        self.__quoridor = quoridor
        super().__init__(quoridor, "configs/configscene.json")
        self.__reset_data = ["NbrBarriere20", "BoardSize9", "NbrPlayers2"]

    def getBoardSize(self):
        return self.__board_size

    def InitConfig(self):
        conf = list()
        conf.append(settings.NB_PLAYERS) # nb Joueurs
        conf.append(settings.BOARD_SIZE) # Taille Plateau
        conf.append(settings.NB_BARRERS) # Nom de barrières
        self.__config = conf
    
    def Reset(self, button):
        [b.Toggle() for b in filter(lambda b: (b.GetId() in self.__reset_data), self.GetMainGroup().sprites()) if not b.IsToggled()]

    def ServerList(self, button):
        self.Next(GameListScene(self.GetQuoridor()))

    def Start(self, button):
        self.InitConfig()
        self.Next(GameScene(self.GetQuoridor(), Game(self.__config)))
        
    def NbBarrers(self, button, toggle):
        if self.__nbbarrers is not None and button != self.__nbbarrers:
            self.__nbbarrers.Toggle()
        self.__nbbarrers = button
        settings.NB_BARRERS = int(button.GetId().replace("NbrBarriere", ""))
        print(settings.NB_BARRERS)
        
    def NbPlayers(self, button, toggle):
        if self.__nbplayers is not None and button != self.__nbplayers:
            self.__nbplayers.Toggle()
        self.__nbplayers = button
        settings.NB_PLAYERS = int(button.GetId().replace("NbrPlayers", ""))
    
    def BoardSize(self, button, toggle):
        if self.__board_size is not None and button != self.__board_size:
            self.__board_size.Toggle()
        self.__board_size = button
        settings.BOARD_SIZE = int(button.GetId().replace("BoardSize", ""))