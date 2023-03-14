"""
Module de lancement du jeu et des serveur

.. code-block:: python

    # Lancer le jeu
    python launcher.py
    python launcher.py game
    
    # Lancer un serveur de jeu
    python launcher.py gameserver

    # Lancer le GameListServer
    python launcher.py serverlist
    
"""
from rich.traceback import install
install(show_locals=True)
import sys
import quoridor as quoridor
import network.gamelistserver as gamelist
import network.gameserver as gameserver
import network.client as client

if len(sys.argv) <= 1:
    quoridor.Quoridor()

match(sys.argv[1]):
    case "game":
        QUORIDOR = quoridor.Quoridor()
    case "serverlist":
        gamelist.GameListServer()
    case "gameserver":
        gameserver.GameServer()
    case "netclient":
        client.Client()
print("game, serverlist, gameserver")