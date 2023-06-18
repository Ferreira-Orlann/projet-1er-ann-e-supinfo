from json import load as json_load
from render.scene.basescene import BaseScene
from render.scene.gamescene import GameScene
from game.game import Game
import settings as settings
from render.scene.networkedgamescene import NetworkedGameScene
from render.scene.gamelistscene import GameListScene
from render.buttons import ToggleButton

class ConfigScene(BaseScene):
    def __init__(self, quoridor):
        self.__board_size = None
        self.__nbplayers = None
        self.__nbbarrers = None
        self.__quoridor = quoridor
        super().__init__(quoridor, "configs/configscene.json")
        self.__reset_data = ["NbrBarriere20", "BoardSize9", "NbrPlayers2"]
        self.Reset(None)

    def getBoardSize(self):
        return self.__board_size
    
    def Reset(self, button):
        [b.Toggle() for b in filter(lambda b: isinstance(b, ToggleButton), self.GetMainGroup().sprites()) if b.IsToggled()]
        [b.Toggle() for b in filter(lambda b: (b.GetId() in self.__reset_data), self.GetMainGroup().sprites()) if not b.IsToggled()]

    def ServerList(self, button):
        self.Next(GameListScene(self.GetQuoridor()))

    def Start(self, button):
        q = self.GetQuoridor()
        self.Next(GameScene(q, Game(q)))
        
    def NbBarrers(self, button):
        if (button.IsToggled()): return
        if self.__nbbarrers is not None and button != self.__nbbarrers:
            self.__nbbarrers.Toggle()
        self.__nbbarrers = button
        settings.NB_BARRERS = int(button.GetId().replace("NbrBarriere", ""))
        button.Toggle()
        
    def NbPlayers(self, button):
        if (button.IsToggled()): return
        if self.__nbplayers is not None and button != self.__nbplayers:
            self.__nbplayers.Toggle()
        self.__nbplayers = button
        settings.NB_PLAYERS = int(button.GetId().replace("NbrPlayers", ""))
        button.Toggle()
    
    def BoardSize(self, button):
        if (button.IsToggled()): return
        if self.__board_size is not None and button != self.__board_size:
            self.__board_size.Toggle()
        self.__board_size = button
        settings.BOARD_SIZE = int(button.GetId().replace("BoardSize", ""))
        button.Toggle()