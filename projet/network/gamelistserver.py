import socket
import threading
import json
from console import Console
from network.server import Server

class GameListServer(Server):
    
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50000)
        self.GetConsole().log("[green]Server initialisé")
        
        self.__servers = []
        
        self.__conn_handler_thread = threading.Thread(target=self.ReadHandler)
        self.__conn_handler_thread.daemon = True
        self.__conn_handler_thread.start()
        
        self.__conn_handler_thread.join()
        self.__lsock_thread.join()
        
    def ReadHandler(self):
        while 1:
            for stock in self.GetStockings():
                string = stock.read()
                if string == None: continue
                data = json.loads(string)
                print(data)
                match (data.get("action")):
                    case "retreive_servers":
                        stock.write(json.dumps({
                            "action": "retreive_servers",
                            "servers": [server.addr for server in self.__servers]
                        }))
                        pass
                    case "register":
                        self.__servers.append(stock)
                        
    def RemoveStocking(self, stock):
        self.GetStockings().remove(stock)
        if stock in self.__servers:
            self.__servers.remove(stock)