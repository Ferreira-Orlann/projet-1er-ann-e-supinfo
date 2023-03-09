import socket
import libs.Stockings as Stockings
import threading
import json

class Client():
   
    def __init__(self):
        host, port = "127.0.0.1", 50000
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)
        self.ConnectionHandler()
        
    def ConnectionHandler(self):
        while 1:
            pass