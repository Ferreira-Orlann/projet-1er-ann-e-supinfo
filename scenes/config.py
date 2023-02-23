from scenes.scenebase import SceneBase
from math import ceil
import pygame
from json import load as json_load

class SceneConfig(SceneBase):
    def __init__(self, screen, quoridor):
        SceneBase.__init__(self)
        self.__file = open("configs/configpage.json", "r")
        self.__json = json_load(self.__file)
        self.__file.close()
        self.__quoridor = quoridor
        self.__elements = {}
        self.__rects = {}
        
        self.__background = pygame.image.load('./images/page2/background3.jpg')
        
        ### INIT CONFIGURATION ###
        # Images
        for name, data in self.__json["paths"].items():
            self.__elements[name] = pygame.transform.scale(pygame.image.load(data[0]), (data[1], data[2]))
        # Rects
        for name, data in self.__json["rects"].items():
            rect = self.__elements[name].get_rect()
            rect.x = ceil(screen.get_width() / data[0])
            rect.y = ceil(screen.get_width() / data[1])
            self.__rects[name] = rect
            
        self.InitConfig()
            
    def InitConfig(self):
        conf = list()
        conf.append(0) # nb Joueurs
        conf.append(0) # Taille Plateau
        conf.append(0) # Nom de barrières
        self.__config = conf
        
        self.CheckConfig("nbrPlayers2")
        self.CheckConfig("taillePlateau5")
        self.CheckConfig("nbrbarriere4")
        
    def SelectElement(self, name, val, confidx):
        conf = self.__config
        if conf[confidx] == val:
            return
        if conf[confidx] != 0:
            previous_name = ''.join([i for i in name if not i.isdigit()]) + str(conf[confidx])
            data = self.__json["paths"][previous_name]
            self.__elements[previous_name] = pygame.transform.scale(pygame.image.load(data[0]), (data[1], data[2]))
        data = self.__json["paths"][name]
        self.__elements[name] = pygame.transform.scale(pygame.image.load(data[0].replace(".PNG", "ok.PNG")), (data[1], data[2]))
        conf[confidx] = val
        pass
    
    def CheckConfig(self, name):
        conf = self.__config
        if name == "reset":
            self.InitConfig()
        elif "nbrPlayers" in name:
            self.SelectElement(name, int(name.replace("nbrPlayers", "")), 0)
        elif "taillePlateau" in name:
            self.SelectElement(name, int(name.replace("taillePlateau", "")), 1)
        elif"nbrbarriere" in  name:
            self.SelectElement(name, int(name.replace("nbrbarriere", "")), 2)
        
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for name, rect in self.__rects.items():
                    if rect.collidepoint(event.pos):
                        self.CheckConfig(name)

                # if self.__Play_rect.collidepoint(event.pos) and self.__nbrPlayers != 0 and self.__taillePlateau != 0 and self.__nbrBarriere != 0:
                #     self.GamePage()
                #     self.__file.close()
                # if self.__nbrPlayers2_rect.collidepoint(event.pos):
                #     conf[0] = 2
                #     self.__nbrPlayers2 = pygame.transform.scale(pygame.image.load('./images/page2/choix1ok.PNG'), (120, 120))
                # if self.__nbrPlayers4_rect.collidepoint(event.pos):
                #     conf[0] = 4
                #     self.__nbrPlayers4 = pygame.transform.scale(pygame.image.load('./images/page2/choix2ok.PNG'), (120, 120))
                # if self.__taillePlateau5_rect.collidepoint(event.pos):
                #     conf[1] = 5 
                #     self.__taillePlateau5 = pygame.transform.scale(pygame.image.load('./images/page2/5x5ok.PNG'), (280, 70))
                # if self.__taillePlateau7_rect.collidepoint(event.pos):
                #     conf[1] = 7
                #     self.__taillePlateau7 = pygame.transform.scale(pygame.image.load('./images/page2/7x7ok.PNG'), (280, 70))
                # if self.__taillePlateau9_rect.collidepoint(event.pos):
                #     conf[1] = 9
                #     self.__taillePlateau9 = pygame.transform.scale(pygame.image.load('./images/page2/9x9ok.PNG'), (280, 70))
                # if self.__taillePlateau11_rect.collidepoint(event.pos):
                #     conf[1] = 11
                #     self.__taillePlateau11 = pygame.transform.scale(pygame.image.load('./images/page2/11x11ok.PNG'), (280, 70))
                # if self.__nbrbarriere4_rect.collidepoint(event.pos):
                #     conf[2] = 4
                #     self.__nbrbarriere4 = pygame.transform.scale(pygame.image.load('./images/page2/barriere4ok.PNG'), (120, 120))
                # if self.__nbrbarriere8_rect.collidepoint(event.pos):
                #     conf[2] = 8
                #     self.__nbrbarriere8 = pygame.transform.scale(pygame.image.load('./images/page2/barriere8ok.PNG'), (120, 120))
                # if self.__nbrbarriere12_rect.collidepoint(event.pos):
                #     conf[2] = 12
                #     self.__nbrbarriere12 = pygame.transform.scale(pygame.image.load('./images/page2/barriere12ok.PNG'), (120, 120))
                # if self.__nbrbarriere16_rect.collidepoint(event.pos):
                #     conf[2] = 16
                #     self.__nbrbarriere16 = pygame.transform.scale(pygame.image.load('./images/page2/barriere16ok.PNG'), (120, 120))
                # if self.__nbrbarriere20_rect.collidepoint(event.pos):
                #     conf[2] = 20
                #     self.__nbrbarriere20 = pygame.transform.scale(pygame.image.load('./images/page2/barriere20ok.PNG'), (120, 120))
                # if self.__nbrbarriere24_rect.collidepoint(event.pos):
                #     conf[2] = 24
                #     self.__nbrbarriere24 = pygame.transform.scale(pygame.image.load('./images/page2/barriere24ok.PNG'), (120, 120))
                # if self.__nbrbarriere28_rect.collidepoint(event.pos):
                #     conf[2] = 28
                #     self.__nbrbarriere28 = pygame.transform.scale(pygame.image.load('./images/page2/barriere28ok.PNG'), (120, 120))
                # if self.__nbrbarriere32_rect.collidepoint(event.pos):
                #     conf[2] = 32
                #     self.__nbrbarriere32 = pygame.transform.scale(pygame.image.load('./images/page2/barriere32ok.PNG'), (120, 120))
                # if self.__nbrbarriere36_rect.collidepoint(event.pos):
                #     conf[2] = 36
                #     self.__nbrbarriere36 = pygame.transform.scale(pygame.image.load('./images/page2/barriere36ok.PNG'), (120, 120))
                # if self.__nbrbarriere40_rect.collidepoint(event.pos):
                #     conf[2] = 40
                #     self.__nbrbarriere40 = pygame.transform.scale(pygame.image.load('./images/page2/barriere40ok.PNG'), (120, 120))
                # if self.__jouerreseau_rect.collidepoint(event.pos):
                #     self.__PlayInReseau = True
                #     self.__jouerreseau = pygame.transform.scale(pygame.image.load('./images/page2/reseauok.PNG'), (350, 100))
                # if self.__reset_rect.collidepoint(event.pos):
                #     conf[0] = 2
                #     conf[1] = 5
                #     conf[2] = 4
        
    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.__background, (0,0))
        for name,element in self.__elements.items():
            screen.blit(element, self.__rects[name])