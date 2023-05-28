import libs.richthread as threading
import json
from console import Console
from network.server import Server
from time import sleep

class GameListServer(Server):
    
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50000)
        
        self.__servers = []  # List of servers connected to the master server
        
        self.__conn_handler_thread = threading.Thread(self.ReadHandler)
        self.__conn_handler_thread.daemon = True
        self.__conn_handler_thread.start()
        
        self.__conn_handler_thread.join()
        
    def ReadHandler(self):
        """Read the data from the server"""
        while 1:
            for stock in self.GetStockings():
                if not stock.handshakeComplete:
                    continue
                string = self.ReadStock(stock)
                if string == None: continue
                data = json.loads(string)
                match (data.get("action")):
                    case "retreive_servers":
                        stock.write(json.dumps({
                            "action": "retreive_servers",
                            "servers": [self.AddrToString(server.addr) for server in self.__servers]
                        }))
                        pass
                    case "register":
                        self.__servers.append(stock)
                        stock.write(json.dumps({
                            "action": "register",
                            "result": "OK"
                        }))
                        self.GetConsole().log("[blue]Client " + str(stock.GetId()) + " détecté comme GameServer")
            sleep(0.5)
                        
    def RemoveStocking(self, stock):
        """Remove a stocking from the server"""
        if stock in self.__servers:
            self.__servers.remove(stock)
        super().RemoveStocking(stock)
