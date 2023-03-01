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
            self.__players.append(HumanPlayer(i))
        self.__players[1].SetPos((8,8))
        self.__cplayer = 0
        self.ProcessPossiblesMoves(self.__players[0])
        
    def ProcessMove(self,pos, player):
        if not pos in self.__possibles_moves:
            return
        player.SetPos(pos)
        print(self.__cplayer)
        self.SwitchPlayer(player)
        self.ProcessPossiblesMoves(self.__players[self.__cplayer])
        
    def ProcessBarrer():
        pass
    
    def SwitchPlayer(self, previous_player):
        previous_player = previous_player.GetId()
        if previous_player != self.__cplayer:
            return
        if previous_player == len(self.__players)-1:
            self.__cplayer = 0
            return
        self.__cplayer = previous_player + 1
    
    def GetBarrers(self):
        return self.__barrers
    
    def CheckPath(self, player):
        pass
    
    def GetPossiblesMoves(self):
        return self.__possibles_moves
    
    def ProcessPossiblesMoves(self, player):
        quoridor = self.__quoridor
        ppos = player.GetPos()
        possibles_moves = []
        for i in [quoridor.MOVE_TYPE_UP, quoridor.MOVE_TYPE_DOWN, quoridor.MOVE_TYPE_LEFT, quoridor.MOVE_TYPE_RIGHT]:
            nextpos = tuple(map(operator.sub, player.GetPos(), i))
            if nextpos[0] < 0 or nextpos[1] < 0:
                continue
            if self.CanMove(ppos, i, nextpos):
                possibles_moves.append(nextpos)
        self.__possibles_moves = possibles_moves
        print(self.__possibles_moves)
    
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
        try:
            if self.__barrers[check[0]][check[1]] != None:
                return False
        except:
            return False
        return True
    
    def GetPlayers(self):
        return self.__players
    
    def GetCurrentPlayer(self):
        return self.__players[self.__cplayer]