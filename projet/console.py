import libs.richthread as richthread
import threading
from os import kill
from os import getpid
from signal import SIGTERM
from rich.console import Console as RConsole
from rich.table import Table
import libs.Stockings as Stockings

class Console(RConsole):
    def __init__(self):
        super().__init__()
        self.__commands = {}
        self.__thread = richthread.Thread(target=self.Run)
        self.__thread.daemon = True
        self.__thread.start()
        self.RegisterCommand("help", self.HelpCommand, "Afficher la liste des commandes disponibles")
        self.RegisterCommand("exit", self.Quit, "Permet de quiter le processus en cour")
        self.log("[green3][link=https://github.com/Ferreira-Orlann/projet-1er-ann-e-supinfo]Lien Github du projet[/link]")

    def RegisterCommand(self,command, func, desc):
        """Register a command"""
        self.__commands[command] = [func, desc]
        
    def Call(self, args):
        """Call a command"""
        args = args.split(" ")
        data = self.__commands.get(args[0], None)
        if data is not None:
            self.log("[green]Execution: " + args[0] + "[/green]")
            args.remove(args[0])
            data[0](args)
        else:
            self.log("[red]Erreur: Commande inconnue")
            
    def Run(self):
        """Run the console"""
        while 1:
            try:
                self.Call(str(self.input()))
            except KeyboardInterrupt:
                self.log("[red]Interuption => CTRL + C")
                self.Quit()
            except EOFError:
                self.log("[red]Interuption => CTRL + C")
                self.Quit()
            
    def Quit(self, args=None):
            """Quit the console"""
            for thread in threading.enumerate():
                if isinstance(thread, Stockings.Stocking):
                    thread.close()
            self.log("[red]EXIT[/red]")
            kill(getpid(), SIGTERM)
            
    def HelpCommand(self, args):
        """Display the help"""
        table = Table()
        table.add_column("Commande", justify="right", style="cyan", no_wrap=True)
        table.add_column("Desciption", style="magenta")
        for cmd, cmddata in self.__commands.items():
            table.add_row(cmd, cmddata[1])
        self.print(table)