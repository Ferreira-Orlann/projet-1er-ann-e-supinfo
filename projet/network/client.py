import socket
import libs.Stockings as Stockings
import json
import libs.richthread as threading
import time

class NetClient():
    def __init__(self, quoridor):
        self.__stocking = None
        self.__rserver_receiver = None
        self.__actions = {}
        self__quoridor = quoridor
        self.__thread = threading.Thread(target=self.ReadHandler)
        self.__thread.daemon = True
        self.__thread.start()
        self.__thread.join()
        
    def AddAction(self, name, func):
        self.__actions[name] = func
        
    def RetreiveServers(self, data):
        self.__rserver_receiver(data.get("servers", []))
        self.__rserver_receiver = None
        self.__stocking.close()
        self.__stocking = None
    
    def Kick(self, data):
        addr = self.__stocking.addr
        self.quoridor.GetConsole().log("[red]Vous avez été kick de: " + addr[0] + ":" + str(addr[1]) + "\nMessage: " + data.get("message"))
        if self.__stocking == self.__serverlist_stocking:
            self.GetConsole().Quit()

    def ReadHandler(self):
        """Read the data from the server"""
        while 1:
            if self .__stocking is not None:
                string = self.__stocking.read()
                if string is not None:
                    if string == None: continue
                    data = json.loads(string)
                    action = data.get("action")
                    if (action is not None):
                        self.__actions.get(action)(data)
            time.sleep(.5)
            pass
        
    def RequestServerList(self, gamelistserver_ip, gamelistserver_port, callback):
        """Request the server list from the master server"""
        self.Connect(gamelistserver_ip, gamelistserver_port)
        while self.__stocking.handshakeComplete is not True:
            time.sleep(0.1)
        self.__stocking.write(json.dumps({
            "action": "retreive_servers"
        }))
        self.__rserver_receiver = callback
    
    def Connect(self, host, port):
        """Connect to the server"""
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.connect((host, port))
        self.__lsock = lsock
        self.__stocking = Stockings.Stocking(self.__lsock)

