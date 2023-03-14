import socket
import libs.richthread as threading
import json
import sys
import settings
from console import Console
from network.server import Server
from network.quoridorstoking import QuoridorStocking
from time import sleep
from game.game import Game
from rich.table import Table

class GameServer(Server):
    
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50001)
        self.ProcessArgs(sys.argv)
        self.__game = Game(self)
        self.__players = []
        
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
                    case "register-client":
                        if len(self.__players) == settings.NB_BARRERS:
                            self.Kick(stock)
                        # Send game data
                    case "kick":
                        self.GetConsole().log("[red]Vous avez été kick de: " + self.AddrToString(stock.addr))
                        if stock == self.__serverlist_stocking:
                            self.GetConsole().Quit()
                    case "move":
                        if self.__players[self.__game.GetCurrentPlayer()[1]] == stock:
                            pass
                        pass
            sleep(0.1)
            
    def CheckClient(self, stock):
        if stock not in self.__players:
            return False
        else:
            return True
    
    def ProcessArgs(self, args):
        while (len(args) > 0):
            if len(args) == 1:
                self.PrintArgsHelp()
                break
            match(args[0]):
                case "-b":
                    settings.NB_BARRERS = int(args[1])
                case "-p":
                    settings.NB_PLAYERS = int(args[1])
                case "-s":
                    settings.BOARD_SIZE = int(args[1])
            del args[0]
            del args[0]
            
    def PrintArgsHelp(self):
        table = Table()
        table.add_column("Argument", justify="right", style="cyan", no_wrap=True)
        table.add_column("Usage", style="magenta")
        table.add_row("","-p 'nombre de joueurs'")
        table.add_row("","-b 'nombre de barrières'")
        table.add_row("","-s 'taille du plateau'")
        self.GetConsole().print(table)