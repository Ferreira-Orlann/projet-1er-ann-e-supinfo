import socket
import libs.Stockings as Stockings
import json
import libs.richthread as threading
from time import sleep

class NetClient():
    def __init__(self, quoridor):
        self.__stocking = None
        self.__actions = {}
        self__quoridor = quoridor
        self.__stock_error = False
        self.__thread = threading.Thread(target=self.ReadHandler)
        self.__thread.start()
        
    def GetStocking(self):
        return self.__stocking
        
    def AddAction(self, name, func):
        self.__actions[name] = func
    
    def Kick(self, data):
        addr = self.__stocking.addr
        self.quoridor.GetConsole().log("[red]Vous avez été kick de: " + addr[0] + ":" + str(addr[1]) + "\nMessage: " + data.get("message"))
        if self.__stocking == self.__serverlist_stocking:
            self.GetConsole().Quit()
            
    def IsStockError(self):
        return self.__stock_error

    def ReadHandler(self):
        """Read the data from the server"""
        while 1:
            if self .__stocking is not None:
                if not self.__stocking.handshakeComplete or self.__stock_error:
                    continue
                try:
                    string = self.__stocking.read()
                except:
                    self.__stock_error = True
                    break
                if string is not None:
                    if string == None: continue
                    data = json.loads(string)
                    action = data.get("action")
                    if (action is not None):
                        func = self.__actions.get(action)
                        if (func is not None):
                            func(data)
                        else:
                            print("Error: " + string)
            sleep(0.05)
        
    # def RequestServerList(self, gamelistserver_ip, gamelistserver_port, callback):
    #     """Request the server list from the master server"""
    #     self.Connect(gamelistserver_ip, gamelistserver_port)
    #     while self.__stocking.handshakeComplete is not True:
    #         time.sleep(0.1)
    #     self.__stocking.write(json.dumps({
    #         "action": "retreive_servers"
    #     }))
    #     self.__rserver_receiver = callback
    
    def Connect(self, host, port):
        """Connect to the server"""
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)

