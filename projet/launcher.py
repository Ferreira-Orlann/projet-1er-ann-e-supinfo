from rich.traceback import install
install(show_locals=True)
import sys
import quoridor as quoridor
import network.gamelistserver as gamelist
import network.gameserver as gameserver

if len(sys.argv) <= 1:
    print("""
-game => Jeux
-serverlist => GameListServer
-gameserver => GameServer
        """)
    sys.exit(1)

match(sys.argv[1]):
    case "-game":
        QUORIDOR = quoridor.Quoridor()
    case "-serverlist":
        gamelist.GameListServer()
    case "-gameserver":
        gameserver.GameServer()
    case _:
        print("""
-game => Jeux
-serverlist => GameListServer
-gameserver => GameServer
        """)