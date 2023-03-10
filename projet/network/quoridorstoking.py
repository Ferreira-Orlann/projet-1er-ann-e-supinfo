import libs.Stockings as Stockings

class QuoridorStocking(Stockings.Stocking):    
    def __init__(self, server, conn, id):
        super().__init__(conn)
        self.__server = server
        self.__id = id
    
    def close(self):
        self.__server.RemoveStocking(self)
        super().close()
        
    def GetId(self):
        return self.__id