import socket
import libs.richthread as threading
import json
from console import Console
from network.server import Server
from network.quoridorstoking import QuoridorStocking
from time import sleep

class GameServer(Server):
    
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50001)
        self.__servers = []
        
        self.__conn_handler_thread = threading.Thread(target=self.ReadHandler)
        self.__conn_handler_thread.daemon = True
        self.__conn_handler_thread.start()
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(("127.0.0.1", 50000))
        except ConnectionRefusedError as err:
            self.GetConsole().log("[red]Fatal Erreur: Le serveur n'a pas réussi à se connecter au GameListServer")
            self.GetConsole().Quit()
        self.__serverlist_stocking = QuoridorStocking(self, sock, 0, True)
        self.GetStockings().append(self.__serverlist_stocking)
        while self.__serverlist_stocking.handshakeComplete is not True:
            sleep(0.1)
        self.__serverlist_stocking.write(json.dumps({
            "action": "register"
        }))
        
        self.__conn_handler_thread.join()
        
    def ReadHandler(self):
        while 1:
            for stock in self.GetStockings():
                if self.__serverlist_stocking.handshakeComplete is not True:
                    continue
                string = self.ReadStock(stock)
                if string == None: continue
                data = json.loads(string)
                match (data.get("action")):
                    case "register":
                        pass
                    case "kick":
                        self.GetConsole().log("[red]Vous avez été kick de: " + self.AddrToString(stock.addr))
                        if stock == self.__serverlist_stocking:
                            self.GetConsole().Quit()
            sleep(0.1)