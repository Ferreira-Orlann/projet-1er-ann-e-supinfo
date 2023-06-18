import libs.richthread as threading
import json
from console import Console
from network.server import Server
from time import sleep

class GameListServer(Server):
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50000)
        
        self.__servers = []  # List of servers connected to the master server
        self.AddAction("retreive_servers", self.RetreiveServers)
        self.AddAction("register", self.Register)
        
    def RetreiveServers(self, data, stock):
        self.Write(stock,json.dumps({
            "action": "retreive_servers",
            "servers": [self.AddrToString(server.addr) for server in self.__servers]
        }))
        
    def Register(self, data, stock):
        self.__servers.append(stock)
        self.Write(stock, json.dumps({
            "action": "register",
            "result": "OK"
        }))
        self.GetConsole().log("[blue]Client " + str(stock.GetId()) + " détecté comme GameServer")
                        
    def RemoveStocking(self, stock):
        """Remove a stocking from the server"""
        if stock in self.__servers:
            self.__servers.remove(stock)
        super().RemoveStocking(stock)