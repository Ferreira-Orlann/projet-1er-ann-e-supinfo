from json import load as json_load
from render.scene.basescene import BaseScene
from render.scene.gamescene import GameScene
from render.scene.gamelistscene import GameListScene
from game.game import Game
import settings as settings

class ConfigScene(BaseScene):
    def __init__(self, quoridor):
        self.__board_size = None  # size of the board
        self.__nbplayers = None  # number of players
        self.__nbbarrers = None  # number of barriers
        self.__quoridor = quoridor
        super().__init__(quoridor, "configs/configscene.json")
        self.__reset_data = ["NbrBarriere20", "BoardSize9", "NbrPlayers2"]
        self.Reset(None)

    def getBoardSize(self):
        """Return the board size"""
        return self.__board_size
    
    def Reset(self, button):
        """Reset the config"""
        [b.Toggle() for b in filter(lambda b: (b.GetId() in self.__reset_data), self.GetMainGroup().sprites()) if not b.IsToggled()]

    def ServerList(self, button):
        """Go to the server list"""
        self.Next(GameListScene(self.GetQuoridor()))

    def Start(self, button):
        """Start the game"""
        q = self.GetQuoridor()
        self.Next(GameScene(q, Game(q)))
        
    def NbBarrers(self, button):
        """Set the number of barriers"""
        if (button.IsToggled()): return
        if self.__nbbarrers is not None and button != self.__nbbarrers:
            self.__nbbarrers.Toggle()
        self.__nbbarrers = button
        settings.NB_BARRERS = int(button.GetId().replace("NbrBarriere", ""))
        button.Toggle()
        
    def NbPlayers(self, button):
        """Set the number of players"""
        if (button.IsToggled()): return
        if self.__nbplayers is not None and button != self.__nbplayers:
            self.__nbplayers.Toggle()
        self.__nbplayers = button
        settings.NB_PLAYERS = int(button.GetId().replace("NbrPlayers", ""))
        button.Toggle()
    
    def BoardSize(self, button):
        """Set the board size"""
        if (button.IsToggled()): return
        if self.__board_size is not None and button != self.__board_size:
            self.__board_size.Toggle()
        self.__board_size = button
        settings.BOARD_SIZE = int(button.GetId().replace("BoardSize", ""))
        button.Toggle()