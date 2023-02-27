from game.humanplayer import HumanPlayer
import operator

class Game():
    def __init__(self, quoridor, config, scene):
        self.__quoridor = quoridor
        self.__config = config
        self.__scene = scene
        
        # Création des barrières, dans une grille 2d
        # Chaque entrée sera un int => BarrerID
        self.__barrers = []
        lenboard = config[1]
        for i in range(1,lenboard*2):
            if (i % 2 == 0):
                self.__barrers.append([None]*lenboard)
            else:
                self.__barrers.append([None]*(lenboard-1))
        
        # Ajout des joueurs
        self.__players = []
        for i in range(config[0]):
            self.__players.append(HumanPlayer(self))
            
    def CheckPath(self, player):
        pass
    
    def GetMoves(self, player):
        quoridor = self.__quoridor
        ppos = player.GetPos()
        possibles_moves = []
        for i in [quoridor.MOVE_TYPE_UP, quoridor.MOVE_TYPE_DOWN, quoridor.MOVE_TYPE_LEFT, quoridor.MOVE_TYPE_RIGHT]:
            nextpos = tuple(map(operator.sub, player.GetPos(), i))
            if nextpos[0] < 0 or nextpos[1] < 0:
                continue
            if self.CanMove(ppos, i, nextpos):
                possibles_moves.append(nextpos)
        return possibles_moves
    
    def CanMove(self, pos, movetype, nextpos):
        quoridor = self.__quoridor
        check = None
        match movetype:
            case quoridor.MOVE_TYPE_UP:
                check = (pos[0] * 2 - 1, pos[1])
                pass
            case quoridor.MOVE_TYPE_DOWN:
                check = (nextpos[0] * 2 - 1, nextpos[1])
                pass
            case quoridor.MOVE_TYPE_LEFT:
                check = (pos[0]*2, nextpos[1] - 1)
                pass
            case quoridor.MOVE_TYPE_RIGHT:
                check = (pos[0]*2, nextpos[1])
                pass
        if self.__barrers[check[0]][check[1]] != None:
            return False
        return True