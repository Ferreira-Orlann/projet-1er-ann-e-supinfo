class Player():
    def __init__(self):
        self.__pos = (0,0)
        pass
    
    def SetPos(self, pos):
        self.__pos = pos
        
    def GetPos(self):
        return self.__pos