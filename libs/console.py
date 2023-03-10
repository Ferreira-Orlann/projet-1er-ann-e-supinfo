import threading

from os import kill
from os import getpid
from signal import SIGTERM
from rich import print as rprint
from rich.console import Console as RConsole

class Console(RConsole):
    def __init__(self):
        super().__init__()
        self.__commands = {}
        self.__thread = threading.Thread(target=self.Run)
        self.__thread.daemon = True
        self.__thread.start()
        self.RegisterCommand("exit", lambda: kill(getpid(), SIGTERM))
        self.RegisterCommand("help", lambda: rprint(self.__commands))
        
    def RegisterCommand(self,command, func):
        self.__commands[command] = func
        
    def Call(self, command):
        func = self.__commands.get(command, None)
        if func is not None:
            self.log("[green]Execution: " + command + "[/green]")
            func()
        else:
            self.log("[red]Erreur: Commande inconnue")
            
    def Run(self):
        while 1:
            try:
                self.Call(str(input()))
            except:
                self.log("[red]Interuption")
                kill(getpid(), SIGTERM)