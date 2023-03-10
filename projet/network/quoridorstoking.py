import libs.Stockings as Stockings

class QuoridorStocking(Stockings.Stocking):    
    def __init__(self, server, conn, id, fatal=False):
        super().__init__(conn)
        self.__server = server
        self.__id = id
        self.__fatal = fatal
        self.__disconnect = False
    
    def close(self):
        self.__server.RemoveStocking(self)
        super().close()
        
    def GetId(self):
        return self.__id
    
    def IsFatal(self):
        return self.__fatal
    
    def IsDisconnected(self):
        return self.__disconnect
    
    def Disconnect(self):
        self.__disconnect = True