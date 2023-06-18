from network.quoridorstoking import QuoridorStocking
import libs.richthread as threading
import socket
import json
from time import sleep
from rich.table import Table

class Server():
    def __init__(self, console, host, port):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        self.__actions = {}
        self.__lsock = lsock
        self.__accept_thread = threading.Thread(target=self.RunAcceptConnection)
        self.__accept_thread.start()
        
        self.__console = console
        self.__console.RegisterCommand("clients", self.ClientsList, "Voir la liste de tout les clients/joueurs")
        self.__console.RegisterCommand("kick", self.KickClient, "Permet d'expulser un client/joueur par son id")
        self.__stockings = []
        self.GetConsole().log("[green]Server initialisé")
        
        self.__thread = threading.Thread(target=self.ReadHandler)
        self.__thread.start()
        
    def GetStocks(self):
        return self.__stockings
    
    def Write(self, stock, data):
        try:
            return stock.write(data)
        except BrokenPipeError as err:
            self.StockError(stock, err)
            self.RemoveStocking(stock)
        except ConnectionResetError as err:
            self.StockError(stock, err)
            self.RemoveStocking(stock)
        return None

    def AddAction(self, name, func):
        self.__actions[name] = func
    
    def StockError(self, stock, err): ...
        
    def ReadHandler(self):
        """Read the data from the server"""
        while 1:
            for stock in self.GetStockings():
                if not stock.handshakeComplete:
                    continue
                string = self.ReadStock(stock)
                if string == None: continue
                data = json.loads(string)
                action = data.get("action")
                if (action is not None):
                    func = self.__actions.get(action)
                    if (func is not None):
                        func(data, stock)
            sleep(0.05)
        
    def RemoveStocking(self, stock):
        """Remove a stocking from the list"""
        if stock in self.__stockings:
            self.__stockings.remove(stock)
        if not stock.IsDisconnected():
            self.GetConsole().log("Client disconnect \n    Id: " + str(stock.GetId()) + " \n    Addresse: " + self.AddrToString(stock.addr), style="light_salmon3", markup=False)
            stock.Disconnect()
        if stock.IsFatal() and not self.GetConsole().IsQuiting():
            self.GetConsole().log("[red]Fatal Client Disconnect")
            self.GetConsole().Quit()
            
    def GetStockings(self):
        """Return the list of stockings"""
        return self.__stockings
    
    def GetSocket(self):
        """Return the main stocking"""
        return self.__lsock
    
    def RunAcceptConnection(self):
        """Accept the connection from the client"""
        while 1:
            conn, addr = self.__lsock.accept()
            self.__console.log("[blue]Client connecté: " + addr[0] + ":" + str(addr[1]))
            if len(self.__stockings) == 0:
                self.__stockings.append(QuoridorStocking(self, conn, 1))
            else:
                self.__stockings.append(QuoridorStocking(self, conn, self.__stockings[-1].GetId() + 1))

    def GetConsole(self):
        """Return the console"""
        return self.__console
    
    def ReadStock(self, stock):
        """Read the stocking"""
        try:
            return stock.read()
        except BrokenPipeError as err:
            self.StockError(stock, err)
            self.RemoveStocking(stock)
        except ConnectionResetError as err:
            self.StockError(stock, err)
            self.RemoveStocking(stock)
        return None
        
    def ClientsList(self, args):
        """Show the list of clients"""
        table = Table()
        table.add_column("Id", justify="right", style="cyan", no_wrap=True)
        table.add_column("Addresse", style="magenta")
        for stock in self.GetStockings():
            addr = stock.addr
            table.add_row(str(stock.GetId()), self.AddrToString(stock.addr))
        self.__console.print(table)
    
    def KickClient(self, args):
        """Kick a client by his id"""
        stock = None
        if (isinstance(args, int)):
            stock = self.GetStockingById(args)
            stock.write(json.dumps({
                "action": "kick",
                "message": ""
            }))
        else:
            if len(args) < 1 or not args[0].isnumeric():
                self.GetConsole().log("[red]Erreur: kick {id}")
                return
            stock = self.GetStockingById(int(args[0]))
            if stock is None:   
                return
            del args[0]
            stock.write(json.dumps({
                "action": "kick",
                "message": " ".join(args)
            }))
        while stock.writeDataQueued() == True:
            sleep(0.1)
        stock.close()
    
    def GetStockingById(self, id):
        """Return the stocking by his id"""
        if id == 0:
            return None
        for stock in self.__stockings:
            if stock.GetId() == id:
                return stock
        return None
    
    def AddrToString(self, addr):
        """Return the address in string"""
        return addr[0] + ":" + str(addr[1])
