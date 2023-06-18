class Player():
    def __init__(self, id, startconfig):
        self.__pos = (startconfig[0], startconfig[1])
        self.__final_pos = (startconfig[2], startconfig[3])
        self.__id = id
        pass
    
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
