from scenes.scenebase import SceneBase
from scenes.game import GameScene
from game.game import Game
from math import ceil
import pygame
from json import load as json_load
from utils import LocalRectToGlobalRect

class SceneConfig(SceneBase):
    def __init__(self, screen, quoridor):
        SceneBase.__init__(self, screen)
        file = open("configs/configpage.json", "r")
        self.__json = json_load(file)
        file.close()
        self.__change = False
        self.__quoridor = quoridor
        self.__elements = {}
        self.__rects = {}
        
        self.__background = pygame.image.load('./assets/page2/background3.jpg')
        
        ### INIT CONFIGURATION ###
        # Images
        for name, data in self.__json["paths"].items():
            self.__elements[name] = pygame.transform.scale(pygame.image.load(data[0]).convert_alpha(), (data[1], data[2]))
        # Rects
        for name, data in self.__json["rects"].items():  
            rect = self.__elements[name].get_rect()
            self.__rects[name] = LocalRectToGlobalRect(screen, rect, data[0], data[1])
            
        self.InitConfig()
        self.CheckConfig("reset")
            
    def InitConfig(self):
        conf = list()
        conf.append(0) # nb Joueurs
        conf.append(0) # Taille Plateau
        conf.append(0) # Nom de barrières
        self.__config = conf
        
    def SelectElement(self, name, val, confidx):
        conf = self.__config
        if conf[confidx] == val:
            return
        if conf[confidx] != 0:
            previous_name = ''.join([i for i in name if not i.isdigit()]) + str(conf[confidx])
            data = self.__json["paths"][previous_name]
            self.__elements[previous_name] = pygame.transform.scale(pygame.image.load(data[0]).convert_alpha(), (data[1], data[2]))
        data = self.__json["paths"][name]
        self.__elements[name] = pygame.transform.scale(pygame.image.load(data[0].replace(".PNG", "ok.PNG")).convert_alpha(), (data[1], data[2]))
        conf[confidx] = val
        self.FullRender()
        pass
    
    def CheckConfig(self, name):
        if name == "reset":
            self.CheckConfig("nbrPlayers2")
            self.CheckConfig("taillePlateau9")
            self.CheckConfig("nbrbarriere20")
        elif name == "Play":
            scene = GameScene(self.GetScreen(), self.__quoridor, self)
            game = Game(self.__quoridor, self.__config, scene)
            scene.SetGame(game)
            self.SwitchToScene(scene)
        elif "nbrPlayers" in name:
            self.SelectElement(name, int(name.replace("nbrPlayers", "")), 0)
        elif "taillePlateau" in name:
            self.SelectElement(name, int(name.replace("taillePlateau", "")), 1)
        elif "nbrbarriere" in  name:
            self.SelectElement(name, int(name.replace("nbrbarriere", "")), 2)
        elif name == "options":
            pass
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for name, rect in self.__rects.items():
                    if rect.collidepoint(event.pos):
                        self.CheckConfig(name)

    def FirstRender(self, screen):
        screen.blit(self.__background, (0,0))
        for name,element in self.__elements.items():
            screen.blit(element, self.__rects[name])
            
    def Render(self, screen):
        self.FirstRender(screen)