class Player():
    def __init__(self, id):
        self.__pos = (0,0)
        self.__final_pos = (4,5)
        self.__id = id
        pass
    
    # Tuple(x,y)
    def SetPos(self, pos):
        self.__pos = pos
        
    def GetPos(self):
        return self.__pos
    
    def SetBarrers(self,nbbarrers):
        self.__nbbarrers = nbbarrers
        
    def GetBarrers(self):
        return self.__nbbarrers
    
    def GetFinalPos(self):
        return self.__final_pos
    
    def GetId(self):
        return self.__id