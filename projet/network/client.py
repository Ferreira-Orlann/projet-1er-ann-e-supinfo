import socket
import libs.Stockings as Stockings
import json
import libs.richthread as threading
import time

class NetClientManager():
    def __init__(self):
        pass

class Client():
    def __init__(self, quoridor):
        self.__stocking = None
        self.__rserver_receiver = None
        self.__thread = threading.Thread(target=self.ReadHandler)
        self.__thread.daemon = True
        self.__thread.start()
        self.RequestServerList(lambda x:print(x))
        self__quoridor = quoridor   
        self.__thread.join()
        
    def ReadHandler(self):
        while 1:
            if self .__stocking is not None:
                string = self.__stocking.read()
                if string is not None:
                    if string == None: continue
                    data = json.loads(string)
                    print(data)
                    match (data.get("action")):
                        case "retreive_servers":
                            self.__rserver_receiver(data.get("servers", []))
                            self.__rserver_receiver = None
                            self.__stocking.close()
                            self.__stocking = None
                            pass
                        case "kick":
                            addr = self.__stocking.addr
                            self.quoridor.GetConsole().log("[red]Vous avez été kick de: " + addr[0] + ":" + str(addr[1]) + "\nMessage: " + data.get("message"))
                            if self.__stocking == self.__serverlist_stocking:
                                self.GetConsole().Quit()
            
            time.sleep(.5)
            pass
        
    def RequestServerList(self, receiver):
        host, port = "127.0.0.1", 50000
        self.Connect(host, port)
        while self.__stocking.handshakeComplete is not True:
            time.sleep(0.1)
        self.__stocking.write(json.dumps({
            "action": "retreive_servers"
        }))
        self.__rserver_receiver = receiver
    
    def Connect(self, host, port):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)
