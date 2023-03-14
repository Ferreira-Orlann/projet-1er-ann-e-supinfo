from network.quoridorstoking import QuoridorStocking
import libs.richthread as threading
import socket
from json import dumps
from time import sleep
from rich.table import Table

class Server():
    def __init__(self, console, host, port):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        self.__lsock = lsock
        self.__accept_thread = threading.Thread(target=self.RunAcceptConnection)
        self.__accept_thread.daemon = True
        self.__accept_thread.start()
        
        self.__console = console
        self.__console.RegisterCommand("clients", self.ClientsList, "Voir la liste de tout les clients/joueurs")
        self.__console.RegisterCommand("kick", self.Kick, "Permet d'expulser un client/joueur par son id")
        self.__stockings = []
        self.GetConsole().log("[green]Server initialisé")
        
        self.__quit = False
        
    def RemoveStocking(self, stock):
        if stock in self.__stockings:
            self.__stockings.remove(stock)
        if not stock.IsDisconnected():
            self.GetConsole().log("Client disconnect \n    Id: " + str(stock.GetId()) + " \n    Addresse: " + self.AddrToString(stock.addr), style="light_salmon3", markup=False)
            stock.Disconnect()
        if stock.IsFatal() and self.__quit == False:
            self.__quit = True
            self.GetConsole().log("[red]Fatal Client Disconnect")
            self.GetConsole().Quit()
            
    def GetStockings(self):
        return self.__stockings
    
    def GetMainStock(self):
        return self.__lsock
    
    def RunAcceptConnection(self):
        while 1:
            conn, addr = self.__lsock.accept()
            self.__console.log("[blue]Client connecté: " + addr[0] + ":" + str(addr[1]))
            if len(self.__stockings) == 0:
                self.__stockings.append(QuoridorStocking(self, conn, 1))
            else:
                self.__stockings.append(QuoridorStocking(self, conn, self.__stockings[-1].GetId() + 1))

    def GetConsole(self):
        return self.__console
    
    def ReadStock(self, stock):
        try:
            return stock.read()
        except BrokenPipeError as err:
            self.RemoveStocking(stock)
        except ConnectionResetError as err:
            self.RemoveStocking(stock)
            return None
        
    def ClientsList(self, args):        
        table = Table()
        table.add_column("Id", justify="right", style="cyan", no_wrap=True)
        table.add_column("Addresse", style="magenta")
        for stock in self.GetStockings():
            addr = stock.addr
            table.add_row(str(stock.GetId()), self.AddrToString(stock.addr))
        self.__console.print(table)
    
    def Kick(self, args):
        if len(args) < 1 or not args[0].isnumeric():
            self.GetConsole().log("[red]Erreur: kick {id}")
            return
        stock = self.GetStockingById(int(args[0]))
        if stock is None:   
            return
        del args[0]
        stock.write(dumps({
            "action": "kick",
            "message": " ".join(args)
        }))
        while stock.writeDataQueued() == True:
            sleep(0.1)
        stock.close()
    
    def GetStockingById(self, id):
        if id == 0:
            return None
        for stock in self.__stockings:
            if stock.GetId() == id:
                return stock
        return None
    
    def AddrToString(self, addr):
        return addr[0] + ":" + str(addr[1])