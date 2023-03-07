from json import load as json_load
from render.scene.basescene import BaseScene
import settings

class ConfigScene(BaseScene):
    def __init__(self, display_surface):
        self.__board_size = None
        self.__nbplayers = None
        self.__nbbarrers = None
        super().__init__("./assets/page2/background3.jpg", display_surface, "configs/configscene.json")
    
    def Reset(self, button):
        pass

    def ServerList(self, button):
        pass

    def Start(self, button):
        pass

        
    def NbBarrers(self, button, toggle):
        if self.__nbbarrers is not None and button != self.__nbbarrers:
            self.__nbbarrers.Toggle()
        self.__nbbarrers = button
        settings.NB_BARRERS = int(button.GetId().replace("NbrBarriere", ""))
        
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