from game.humanplayer import HumanPlayer

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
            print(i)
            if (i % 2 == 0):
                self.__barrers.append([None]*lenboard)
            else:
                self.__barrers.append([None]*(lenboard-1))
        
        # Ajout des joueurs
        self.__players = []
        for i in range(config[0]):
            self.__players.append(HumanPlayer())
            
        