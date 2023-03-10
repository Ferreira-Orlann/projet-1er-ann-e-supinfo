import socket
import libs.Stockings as Stockings
import json

class NetClientManager():
    def __init__(self):
        pass
        
class Client():
   
    def __init__(self):
        host, port = "127.0.0.1", 50000
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)
        while not (self.__stocking.handshakeComplete):
            pass
        self.__stocking.write(json.dumps({
            "action": "retreive_servers"
        }))
        while 1:
            data = self.__stocking.read()
            if data == None: continue
            print(json.loads(data))
            break
        pass
        
    def ConnectionHandler(self):
        while 1:
            pass