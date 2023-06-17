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
import copy

class GameServer(Server):
    
    def __init__(self):
        super().__init__(Console(), '127.0.0.1', 50001)
        if (not self.ProcessArgs(sys.argv)):
            sys.exit()
        self.__game = Game(self)
        self.__players = []
        
        self.AddAction("register", self.Register)
        
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
        
    def Register(self, data, stock):
        if (data["result"] == "OK"):
            self.GetConsole().log("[green]Serveur enregistrès après du GameListServer: " + self.AddrToString(stock.addr))
        
    def Kick(self, data, stock):
        self.GetConsole().log("[red]Vous avez été kick de: " + self.AddrToString(stock.addr) + "\nMessage: " + data.get("message"))
                
    def RegisterClient(self, data, stock):
        if len(self.__players) == settings.NB_BARRERS:
            self.KickClient(stock)
                            
    def CheckClient(self, stock):
        """Check if the client is a valid client"""
        if stock not in self.__players:
            return False
        else:
            return True
    
    def ProcessArgs(self, sysargs):
        """Process the arguments"""
        args = copy.copy(sysargs)
        while (len(args) > 0):
            if len(args) == 1:
                self.PrintArgsHelp()
                return False
            match(args[0]):
                case "-b":
                    settings.NB_BARRERS = int(args[1])
                case "-p":
                    settings.NB_PLAYERS = int(args[1])
                case "-s":
                    settings.BOARD_SIZE = int(args[1])
                case _:
                    self.PrintArgsHelp()
                    return False
            del args[0]
            del args[0]
            
    def PrintArgsHelp(self):
        """Print the help for the arguments"""
        table = Table()
        table.add_column("Argument", justify="right", style="cyan", no_wrap=True)
        table.add_column("Usage", style="magenta")
        table.add_row("","-p 'nombre de joueurs'")
        table.add_row("","-b 'nombre de barrières'")
        table.add_row("","-s 'taille du plateau'")
        self.GetConsole().print(table)
