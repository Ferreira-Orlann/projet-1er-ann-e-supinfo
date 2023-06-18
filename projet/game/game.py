from game.humanplayer import HumanPlayer
import operator
import settings

class Game():
    def __init__(self, quoridor):
        # self.__START_CONFIGS = [(0,4,True,8), (8,4,True,0), (4,0,False,8), (4,8,False,0)]
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
        # for id in range(settings.NB_PLAYERS):
            # self.__players.append(HumanPlayer(id,self.__START_CONFIGS[id]))
            # self.__players.append(HumanPlayer(id,())
        minus_one = settings.BOARD_SIZE-1
        middle = int(minus_one/2)
        if (settings.NB_PLAYERS == 2):
            self.__players.append(HumanPlayer(0,(0, middle, True, minus_one)))
            self.__players.append(HumanPlayer(1,(minus_one, middle, True, 0)))
        else:
            self.__players.append(HumanPlayer(0,(0, middle, True, minus_one)))
            self.__players.append(HumanPlayer(1,(minus_one, middle, True, 0)))
            self.__players.append(HumanPlayer(2,(middle, 0, False, minus_one)))
            self.__players.append(HumanPlayer(3,(middle, minus_one, False, minus_one)))
            
            
        self.__cplayer = 0
        
        self.__has_changed = True
        self.__MOVE_TYPE_UP = (-1,0)
        self.__MOVE_TYPE_DOWN = (1,0)
        self.__MOVE_TYPE_LEFT = (0,-1)
        self.__MOVE_TYPE_RIGHT = (0,1)
        
        self.__barrer_count = settings.NB_BARRERS
        
        player = self.__players[0]
        self.__possibles_moves = self.ProcessPossiblesMoves(player.GetPos())
        
    def GetBarrerCount(self):
        return self.__barrer_count
    
    def SetCPlayer(self, id):
        self.__cplayer = id
        player = self.__players[self.__cplayer]
        self.__possibles_moves = self.ProcessPossiblesMoves(player.GetPos())
        self.__has_changed = True
        
    def SetPlayers(self, players):
        self.__players = players
        
    def SetBarrerData(self, data):
        self.__barrers = data
        
    def GetBarrerData(self):
        return self.__barrers
        
    def IsPosed(self, barrer_pos):
        try:
            if self.__barrers[barrer_pos[0]][barrer_pos[1]] != None:
                return False
        except:
            return False
        return True
    def CheckSetting():
        pass

    def CheckWin(self, player, pos):
        fpos = player.GetFinalPos()
        if fpos[0] and pos[0] == fpos[1] or (not fpos[0]) and pos[1] == fpos[1]:
            print("Player Win")
            return True
        print("Player Not Win")
        return False
        
    def IsPathsExist(self):
        for player in self.GetPlayers():
            if (not self.PathRecursive(player)):
                return False
            print("Path Exists")
        return True
    
    def PathRecursive(self, player, tested_moves={}, pos=None):
        if (pos == None):
            pos = player.GetPos()
        ppos = self.ProcessPossiblesMoves(pos)
        print(tested_moves)
        for pos in ppos:
            print(pos)
            posstr = self.PosToString(pos)
            if (tested_moves.get(posstr) != None):
                continue
            if (self.CheckWin(player, pos)):
                return True
            tested_moves[posstr] = True
            if (self.PathRecursive(player, tested_moves, pos)):
                return True
        return False
    
    def PosToString(self, pos):
        return str(pos[0]) + "-" + str(pos[1])
        
    def HasChanged(self):
        return self.__has_changed
    
    def SetChanged(self,val):
        self.__has_changed = val
        
    def ProcessMove(self,pos):
        player = self.GetCurrentPlayer()
        if not pos in self.__possibles_moves:
            return False
        player.SetPos(pos)
        self.CheckWin(player, pos)
        self.SwitchPlayer(player)
        return True
    
    def ProcessBarrer(self, pos, pos2):
        if (self.__barrers[pos[0]][pos[1]] or self.__barrers[pos2[0]][pos2[1]]):
            return False
        self.__barrers[pos[0]][pos[1]] = True
        self.__barrers[pos2[0]][pos2[1]] = True
        if (not self.IsPathsExist()):
            self.__barrers[pos[0]][pos[1]] = None
            self.__barrers[pos2[0]][pos2[1]] = None
            return False
        self.__barrer_count -= 2
        self.SwitchPlayer(self.GetCurrentPlayer())
        return True
    
    def DestroyBarrer(self, pos):
        self.__barrers[pos[0]][pos[1]] = None
    
    def SwitchPlayer(self, pplayer):
        previous_player = pplayer.GetId()
        if previous_player != self.__cplayer:
            return
        if previous_player >= (len(self.__players)-1):
            self.__cplayer = 0
        else:
            self.__cplayer = previous_player + 1
        player = self.__players[self.__cplayer]
        self.__possibles_moves = self.ProcessPossiblesMoves(player.GetPos())
        self.__has_changed = True
    
    def GetPossiblesMoves(self):
        return self.__possibles_moves
    
    def ProcessPossiblesMoves(self, pos, recursifcall=False):
        possibles_moves = []
        for i in [self.__MOVE_TYPE_UP, self.__MOVE_TYPE_DOWN, self.__MOVE_TYPE_LEFT, self.__MOVE_TYPE_RIGHT]:
            nextpos = tuple(map(operator.sub, pos, i))
            if nextpos[0] < 0 or nextpos[1] < 0:
                continue
            if self.CanMove(pos, i, nextpos):
                isplayerpos, playercheck = self.IsPlayerPos(nextpos)
                if isplayerpos:
                    if not recursifcall:
                        possibles_moves.extend(self.ProcessPossiblesMoves(playercheck.GetPos(), True))
                    continue
                possibles_moves.append(nextpos)
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
        return self.IsPosed(check)
    
    def GetPlayers(self):
        return self.__players
    
    def GetPlayer(self, pid):
        return self.__players[pid]
    
    def GetCurrentPlayer(self):
        return self.__players[self.__cplayer]