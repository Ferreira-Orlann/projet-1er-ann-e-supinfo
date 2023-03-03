import socket

IP = "127.0.0.1"
PORT = 65432

class ListGameServer:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP,PORT))
        self.__socket = s
        self.LauchConnectionHandler()
        pass
    
    def LauchConnectionHandler(self):
        whi
    
if __name__ == '__main__':
    ListGameServer()