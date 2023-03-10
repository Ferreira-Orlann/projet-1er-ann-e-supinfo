import socket
import libs.Stockings as Stockings
import threading
import json
import time
from libs.console import Console

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
        
        self.__console = Console()
        
        self.__lsock_thread = threading.Thread(target=self.RunAcceptConnection)
        self.__lsock_thread.daemon = True
        self.__lsock_thread.start()
        self.__conn_handler_thread = threading.Thread(target=self.ConnectionHandler)
        self.__conn_handler_thread.daemon = True
        self.__conn_handler_thread.start()
        
        self.__conn_handler_thread.join()
        self.__lsock_thread.join()
        
    def ConnectionHandler(self):
        while 1:
            for stock in self.__stockings:
                string = stock.read()
                if string == None: continue
                data = json.loads(string)
                print(data)
                match (data.get("action")):
                    case "retreive_servers":
                        stock.write(json.dumps({
                            "servers": [server.addr for server in self.__servers]
                        }))
                        pass
                    case "register":
                        self.__servers.append(stock)
                        
            time.sleep(.5)

    def RunAcceptConnection(self):
        while 1:
            conn, addr = self.__lsock.accept()
            self.__stockings.append(GameServerStocking(self, conn))

    def RemoveStocking(self, stock):
        self.__stockings.remove(stock)
        if stock in self.__servers:
            self.__servers.remove(stock)

class GameServerStocking(Stockings.Stocking):
    def __init__(self, gameserver, conn):
        super().__init__(conn)
        self.__gameserver = gameserver
    
    def close(self):
        self.__gameserver.RemoveStocking(self)
        super().close()