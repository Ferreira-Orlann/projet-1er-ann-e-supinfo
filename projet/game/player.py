class Player():
    def __init__(self, id, startconfig):
        self.__pos = (startconfig[0], startconfig[1])
        self.__final_pos = (startconfig[2], startconfig[3])
        self.__id = id  # id of the player
        pass
    
    # Tuple(x,y)
    def SetPos(self, pos):
        """Set the position of the player"""
        self.__pos = pos
        
    def GetPos(self):
        """Return the position of the player"""
        return self.__pos
    
    def SetBarrers(self,nbbarrers):
        """Set the number of barrers of the player"""
        self.__nbbarrers = nbbarrers
        
    def GetBarrers(self):
        """Return the number of barrers of the player"""
        return self.__nbbarrers
    
    def GetFinalPos(self):
        """Return the final position of the player"""
        return self.__final_pos
    
    def GetId(self):
        """Return the id of the player"""
        return self.__id
