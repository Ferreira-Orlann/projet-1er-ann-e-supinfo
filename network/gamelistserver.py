import socket
import libs.Stockings as Stockings
import threading
import json

class GameListServer():
   
    def __init__(self):
        host, port = "127.0.0.1", 50000
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        print(f"Listening on {(host, port)}")
        self.__lsock = lsock
        
        self.__servers = []
        self.__stockings = []
        
        self.__lsock_thread = threading.Thread(target=self.RunAcceptConnection)
        self.__lsock_thread.start()
        self.__conn_handler_thread = threading.Thread(target=self.ConnectionHandler)
        self.__conn_handler_thread.start()
        
        
    def ConnectionHandler(self):
        while 1:
            for stock in self.__stockings:
                data = stock.read()
                if data == None: continue
                if data == "server": pass

    def RunAcceptConnection(self):
        while 1:
            conn, addr = self.__lsock.accept()
            self.__stockings.append(GameServerStocking(self, conn))

    pass

class GameServerStocking(Stockings.Stocking):
    def __init__(self, gameserver, conn):
        super().__init__(conn)
        self.__gameserver = gameserver
    
    def close(self):
        super().close()