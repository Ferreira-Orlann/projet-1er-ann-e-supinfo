import threading

from os import kill
from os import getpid
from signal import SIGTERM
from rich.console import Console as RConsole
from rich.table import Table

class Console(RConsole):
    def __init__(self):
        super().__init__()
        self.__commands = {}
        self.__thread = threading.Thread(target=self.Run)
        self.__thread.daemon = True
        self.__thread.start()
        self.RegisterCommand("help", self.HelpCommand, "Afficher la liste des commandes disponibles")
        self.RegisterCommand("exit", self.Exit, "Permet de quiter le processus en cour")
        
    def Exit(self):
        self.log("[red]EXIT[/red]")
        kill(getpid(), SIGTERM)
    
    def RegisterCommand(self,command, func, desc):
        self.__commands[command] = [func, desc]
        
    def Call(self, command):
        data = self.__commands.get(command, None)
        if data is not None:
            self.log("[green]Execution: " + command + "[/green]")
            data[0]()
        else:
            self.log("[red]Erreur: Commande inconnue")
            
    def Run(self):
        while 1:
            try:
                self.Call(str(self.input()))
            except:
                for thread in threading.enumerate():
                    print(thread)
                self.log("[red]Interuption => CTRL + C")
                kill(getpid(), SIGTERM)
                
    def HelpCommand(self):
        table = Table()
        table.add_column("Commande", justify="right", style="cyan", no_wrap=True)
        table.add_column("Desciption", style="magenta")
        for cmd, cmddata in self.__commands.items():
            table.add_row(cmd, cmddata[1])
        self.print(table)