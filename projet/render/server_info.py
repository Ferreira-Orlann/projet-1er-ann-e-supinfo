from render.label import Label

class ServerInfo(Label):
    def __init__(self, id, x, y, scene, font, data):
        super().__init__(id, x, y, scene, font)
        self.__data = data
        
    def SetGata(self, data):
        self.__data = data
        
    def GetData(self):
        return self.__data
    