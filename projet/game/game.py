from game.humanplayer import HumanPlayer
import operator
import settings

class Game():
    def __init__(self, quoridor):
        self.__START_CONFIGS = [(0,4,True,8), (8,4,True,0), (4,0,False,8), (4,8,False,0)]
        self.__quoridor = quoridor
    
        # Création des barrières, dans une grille 2d
        # Chaque entrée sera un int => BarrerID
        self.__barrers = []
        
        lenboard = settings.BOARD_SIZE
        for i in range(1,lenboard*2):
            if (i % 2 == 0):
                self.__barrers.append([None]*lenboard)
            else:
                self.__barrers.append([None]*(lenboard-1))
        
        # Ajout des joueurs
        self.__players = []
        for id in range(settings.NB_PLAYERS):
            self.__players.append(HumanPlayer(id,self.__START_CONFIGS[id]))
        self.__cplayer = 0
        
        self.__has_changed = True
        self.__MOVE_TYPE_UP = (-1,0)
        self.__MOVE_TYPE_DOWN = (1,0)
        self.__MOVE_TYPE_LEFT = (0,-1)
        self.__MOVE_TYPE_RIGHT = (0,1)
        
        self.ProcessPossiblesMoves(self.__players[0])

    def CheckSetting():
        pass

    def CheckWin(self):
        player = self.GetCurrentPlayer()
        fpos = player.GetFinalPos()
        if fpos[0] and player.GetPos()[0] == fpos[1] or fpos[0] and player.GetPos()[1] == fpos[1]:
            print("Player",player.GetId(), "WIN")
            self.__quoridor.GetConsole().Quit()
            return True
        return False
        
    def IsPathExist(self, ):
        
        pass
        
    def HasChanged(self):
        return self.__has_changed
    
    def SetChanged(self,val):
        self.__has_changed = val
        
    def ProcessMove(self,pos):
        player = self.GetCurrentPlayer()
        if not pos in self.__possibles_moves:
            return False
        player.SetPos(pos)
        self.CheckWin()
        self.SwitchPlayer(player)
        return True
        
    def ProcessBarrer(self, pos):
        if (self.__barrers[pos[0]][pos[1]]):
            return False
        self.__barrers[pos[0]][pos[1]] = True
        self.SwitchPlayer(self.GetCurrentPlayer())
        return True
    
    def SwitchPlayer(self, pplayer):
        previous_player = pplayer.GetId()
        if previous_player != self.__cplayer:
            return
        if previous_player >= (len(self.__players)-1):
            self.__cplayer = 0
        else:
            self.__cplayer = previous_player + 1
        self.ProcessPossiblesMoves(self.__players[self.__cplayer])
        self.__has_changed = True
    
    def GetBarrers(self):
        return self.__barrers
    
    def CheckPath(self, player):
        pass
    
    def GetPossiblesMoves(self):
        return self.__possibles_moves
    
    def ProcessPossiblesMoves(self, player, recursifcall=False):
        ppos = player.GetPos()
        possibles_moves = []
        for i in [self.__MOVE_TYPE_UP, self.__MOVE_TYPE_DOWN, self.__MOVE_TYPE_LEFT, self.__MOVE_TYPE_RIGHT]:
            nextpos = tuple(map(operator.sub, player.GetPos(), i))
            if nextpos[0] < 0 or nextpos[1] < 0:
                continue
            if self.CanMove(ppos, i, nextpos):
                isplayerpos, playercheck = self.IsPlayerPos(nextpos)
                if isplayerpos:
                    if not recursifcall:
                        possibles_moves.extend(self.ProcessPossiblesMoves(playercheck, True))
                    continue
                possibles_moves.append(nextpos)
        if not recursifcall:
            self.__possibles_moves = possibles_moves
        else:
            return possibles_moves
        
    def IsPlayerPos(self, pos):
        for i in range(0, len(self.__players)):
            player = self.__players[i]
            if player.GetPos() == pos:
                return True, player
        return False, None
    
    def CanMove(self, pos, movetype, nextpos):
        check = None
        match movetype:
            case self.__MOVE_TYPE_UP:
                check = (nextpos[0] * 2 - 1, nextpos[1])
                pass
            case self.__MOVE_TYPE_DOWN:
                check = (pos[0] * 2 - 1, pos[1])
                pass
            case self.__MOVE_TYPE_LEFT:
                check = (pos[0]*2, nextpos[1] - 1)
                pass
            case self.__MOVE_TYPE_RIGHT:
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
    
    def GetConfig(self):
        return self.__config