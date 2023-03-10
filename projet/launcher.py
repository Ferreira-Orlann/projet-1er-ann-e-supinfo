import sys
import quoridor as quoridor
import network.gamelistserver as gamelist
import network.gameserver as gameserver

if len(sys.argv) <= 1:
    quoridor.Quoridor()
    
match(sys.argv[1]):
    case "game":
        QUORIDOR = quoridor.Quoridor()
    case "serverlist":
        gamelist.GameListServer()
    case "gameserver":
        gameserver.GameServer()