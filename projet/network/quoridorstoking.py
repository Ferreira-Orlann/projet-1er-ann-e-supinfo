import libs.Stockings as Stockings

class QuoridorStocking(Stockings.Stocking):    
    def __init__(self, server, conn):
        super().__init__(conn)
        self.__server = server
    
    def close(self):
        self.__server.RemoveStocking(self)
        super().close()