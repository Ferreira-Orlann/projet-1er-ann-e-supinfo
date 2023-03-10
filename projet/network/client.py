import socket
import libs.Stockings as Stockings
import json
import threading
import time

class NetClientManager():
    def __init__(self):
        pass
        
class Client():
   
    def __init__(self):
        self.__thread = threading.Thread(target=self.ReadHandler)
        self.__thread.daemon = True
        self.__thread.start()
        self.__stocking = None
        self.__rserver_receiver = None
        
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
                            self.__rserver_receiver(json.load(data.get("servers", [])))
                            self.__rserver_receiver = None
                            self.__stocking.socs.shutdown()
                            self.__stocking = None
                            pass
            
            time.sleep(.5)
            pass
        
    def RequestServerList(self, receiver):
        host, port = "127.0.0.1", 50000
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)
        self.__stocking.write(json.dumps({
            "action": "retreive_servers"
        }))
        self.__rserver_receiver = receiver