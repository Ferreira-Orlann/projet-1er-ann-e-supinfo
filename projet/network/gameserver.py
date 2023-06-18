import socket
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
        print("Register")
        super().__init__(Console(), '127.0.0.1', 50001)
        self.ProcessArgs(sys.argv)
        print("Register")
        self.__game = Game(self)
        self.__players = [None]*settings.NB_PLAYERS
        
        self.AddAction("register", self.Register)
        self.AddAction("place_barrer", self.PlaceBarrer)
        self.AddAction("player_move", self.PlayerMove)
        
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
        
    def StockError(self, stock, err):
        pid = self.GetPlayerId(stock)
        if (pid != False):
            self.__players[pid] = None
        
    def GetPlayerId(self, stock):
        for i in range(len(self.__players)):
            if (self.__players[i] == stock):
                return i
        return False
    
    def PlaceBarrer(self, data, stock):
        print("PlaceBarrer")
        pid = self.GetPlayerId(stock)
        if (self.__game.GetCPlayer() == pid):
            if (self.__game.ProcessBarrer(tuple(data["pos_one"]), tuple(data["pos_two"]))):
                for player in self.__players:
                    if (player == stock): continue
                    player.write(json.dumps({
                        "action": "place_barrer",
                        "pos_one": data["pos_one"],
                        "pos_two": data["pos_two"]
                    }))
    def PlayerMove(self, data, stock):
        print("PlayerMove")
        print(self.__players    )
        print(stock)
        pid = self.GetPlayerId(stock)
        print(pid)
        print(self.__game.GetCPlayer())
        if (self.__game.GetCPlayer() == pid):
            print(tuple(data["pos"]))
            if (self.__game.ProcessMove(tuple(data["pos"]))):
                for player in self.__players:
                    if (player == stock or player == None): continue
                    player.write(json.dumps({
                        "action": "player_move",
                        "pos": data["pos"]
                    }))
                print("Ok")

    def Register(self, data, stock):
        if (stock == self.__serverlist_stocking):
            if (data["result"] == "OK"):
                self.GetConsole().log("[green]Serveur enregistrès après du GameListServer: " + self.AddrToString(stock.addr))
        else:
            self.RegisterClient(data, stock)
        
    def Kick(self, data, stock):
        self.GetConsole().log("[red]Vous avez été kick de: " + self.AddrToString(stock.addr) + "\nMessage: " + data.get("message"))
        
    def AddClient(self, stock):
        print(self.__players)
        for i in range(len(self.__players)):
            print(self.__players[i])
            if (self.__players[i] == None):
                self.__players[i] = stock
                return True
        return False
    
    def RegisterClient(self, data, stock):
        if (not self.AddClient(stock)):
            self.KickClient(stock.GetId())
        game = self.__game
        ppos = [None]*settings.NB_PLAYERS
        for player in game.GetPlayers():
            ppos[player.GetId()] = player.GetPos()
        stock.write(json.dumps({
            "action": "init_data",
            "barrers": game.GetBarrerData(),
            "cplayer": game.GetCPlayer(),
            "local_player": self.GetPlayerId(stock),
            "barrer_count": game.GetBarrerCount(),
            "players_pos": ppos
        }))
                            
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
            match(args[0]):
                case "-b":
                    settings.NB_BARRERS = int(args[1])
                    if (settings.NB_BARRERS not in [4,8,12,16,20,24,28,32,36,40]):
                        self.PrintArgsHelp()
                case "-p":
                    settings.NB_PLAYERS = int(args[1])
                    if (settings.NB_PLAYERS not in [2,4]):
                        self.PrintArgsHelp()
                case "-s":
                    settings.BOARD_SIZE = int(args[1])
                    if (settings.BOARD_SIZE not in [5,7,9,11]):
                        self.PrintArgsHelp()
            del args[0]
            del args[0]
            
    def PrintArgsHelp(self):
        """Print the help for the arguments"""
        table = Table()
        table.add_column("Argument", justify="right", style="cyan", no_wrap=True)
        table.add_column("Usage", style="magenta")
        table.add_row("-p","-p 'nombre de joueurs' | [2,4]")
        table.add_row("-b","-b 'nombre de barrières' | [4,8,12,16,20,24,28,32,36,40]")
        table.add_row("-s","-s 'taille du plateau' | [5,7,9,11]")
        self.GetConsole().print(table)
        self.GetConsole().Quit()