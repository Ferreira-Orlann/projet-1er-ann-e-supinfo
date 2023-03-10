from network.quoridorstoking import QuoridorStocking
import threading
import socket

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
        self.__stockings = []
        
    def RemoveStocking(self, stock):
        self.__stockings.remove(stock)
        
    def GetStockings(self):
        return self.__stockings
    
    def RunAcceptConnection(self):
        while 1:
            conn, addr = self.__lsock.accept()
            self.__console.log("[blue] Joueur connecté: " + addr)
            self.__stockings.append(QuoridorStocking(self, conn))

    def GetConsole(self):
        return self.__console