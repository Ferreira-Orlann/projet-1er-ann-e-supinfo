class Player():
    def __init__(self):
        self.__pos = (0,0)
        pass
    
    def SetPos(self, pos):
        self.__pos = pos
        
    # Tuple(x,y)
    def GetPos(self):
        return self.__pos
    
    def SetBarrers(self,barrers):
        self.__barrers = barrers
        
    def GetBarrers(self):
        return self.__barrers