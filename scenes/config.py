from scenes.scenebase import SceneBase
from math import ceil
import pygame
import json
from io import StringIO

class SceneConfig(SceneBase):
    def __init__(self, screen, quoridor):
        SceneBase.__init__(self)
        self.__file = open("../configs/configpage.json", "r")
        self.__json = json.load(f)
        print(self.__json.getvalue())
        self.__quoridor = quoridor
        self.__background = pygame.image.load('./images/page2/background3.jpg')
        # self.__banner_rect.x,self.__banner_rect.y = 2000,1000
        # self.__play_button_rect.x,self.__play_button_rect.y = 2000,1000

        self.__titre = pygame.transform.scale(pygame.image.load('./images/page2/titre.PNG'), (700, 150))
        self.__titre_rect = self.__titre.get_rect()
        self.__titre_rect.x = ceil(screen.get_width() / 4.7)
        self.__titre_rect.y = ceil(screen.get_width() / 65)

        self.__titrenbrPlayers = pygame.transform.scale(pygame.image.load('./images/page2/nbrplayers.PNG'), (320, 50))
        self.__titrenbrPlayers_rect = self.__titrenbrPlayers.get_rect()
        self.__titrenbrPlayers_rect.x = ceil(screen.get_width() / 2.7)
        self.__titrenbrPlayers_rect.y = ceil(screen.get_width() / 6)

        self.__nbrPlayers2 = pygame.transform.scale(pygame.image.load('./images/page2/choix1.PNG'), (120, 120))
        self.__nbrPlayers2_rect = self.__nbrPlayers2.get_rect()
        self.__nbrPlayers2_rect.x = ceil(screen.get_width() / 3.1)
        self.__nbrPlayers2_rect.y = ceil(screen.get_width() / 4.6)

        self.__nbrPlayers4 = pygame.transform.scale(pygame.image.load('./images/page2/choix2.PNG'), (120, 120))
        self.__nbrPlayers4_rect = self.__nbrPlayers4.get_rect()
        self.__nbrPlayers4_rect.x = ceil(screen.get_width() / 1.7)
        self.__nbrPlayers4_rect.y = ceil(screen.get_width() / 4.6)

        self.__titretaillePlateau = pygame.transform.scale(pygame.image.load('./images/page2/tailleplateau.PNG'), (320, 50))
        self.__titretaillePlateau_rect = self.__titretaillePlateau.get_rect()
        self.__titretaillePlateau_rect.x = ceil(screen.get_width() / 2.7)
        self.__titretaillePlateau_rect.y = ceil(screen.get_width() / 3.2)

        self.__taillePlateau5 = pygame.transform.scale(pygame.image.load('./images/page2/5x5.PNG'), (280, 70))
        self.__taillePlateau5_rect = self.__taillePlateau5.get_rect()
        self.__taillePlateau5_rect.x = ceil(screen.get_width() / 22)
        self.__taillePlateau5_rect.y = ceil(screen.get_width() / 2.5)

        self.__taillePlateau7 = pygame.transform.scale(pygame.image.load('./images/page2/7x7.PNG'), (280, 70))
        self.__taillePlateau7_rect = self.__taillePlateau7.get_rect()
        self.__taillePlateau7_rect.x = ceil(screen.get_width() / 3.7)
        self.__taillePlateau7_rect.y = ceil(screen.get_width() / 2.5)

        self.__taillePlateau9 = pygame.transform.scale(pygame.image.load('./images/page2/9x9.PNG'), (280, 70))
        self.__taillePlateau9_rect = self.__taillePlateau9.get_rect()
        self.__taillePlateau9_rect.x = ceil(screen.get_width() / 2)
        self.__taillePlateau9_rect.y = ceil(screen.get_width() / 2.5)

        self.__taillePlateau11 = pygame.transform.scale(pygame.image.load('./images/page2/11x11.PNG'), (280, 70))
        self.__taillePlateau11_rect = self.__taillePlateau11.get_rect()
        self.__taillePlateau11_rect.x = ceil(screen.get_width() / 1.37)
        self.__taillePlateau11_rect.y = ceil(screen.get_width() / 2.5)

        self.__titrenbrbarriere = pygame.transform.scale(pygame.image.load('./images/page2/nbrBarriere.PNG'), (320, 50))
        self.__titrenbrbarriere_rect = self.__titrenbrbarriere.get_rect()
        self.__titrenbrbarriere_rect.x = ceil(screen.get_width() / 2.5)
        self.__titrenbrbarriere_rect.y = ceil(screen.get_width() / 2.5)

        self.__nbrbarriere4 = pygame.transform.scale(pygame.image.load('./images/page2/barriere4.PNG'), (120, 120))
        self.__nbrbarriere4_rect = self.__nbrbarriere4.get_rect()
        self.__nbrbarriere4_rect.x = ceil(screen.get_width() / 30)
        self.__nbrbarriere4_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere8 = pygame.transform.scale(pygame.image.load('./images/page2/barriere8.PNG'), (120, 120))
        self.__nbrbarriere8_rect = self.__nbrbarriere8.get_rect()
        self.__nbrbarriere8_rect.x = ceil(screen.get_width() / 8)
        self.__nbrbarriere8_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere12 = pygame.transform.scale(pygame.image.load('./images/page2/barriere12.PNG'), (120, 120))
        self.__nbrbarriere12_rect = self.__nbrbarriere12.get_rect()
        self.__nbrbarriere12_rect.x = ceil(screen.get_width() / 4.6)
        self.__nbrbarriere12_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere16 = pygame.transform.scale(pygame.image.load('./images/page2/barriere16.PNG'), (120, 120))
        self.__nbrbarriere16_rect = self.__nbrbarriere16.get_rect()
        self.__nbrbarriere16_rect.x = ceil(screen.get_width() / 3.25)
        self.__nbrbarriere16_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere20 = pygame.transform.scale(pygame.image.load('./images/page2/barriere20.PNG'), (120, 120))
        self.__nbrbarriere20_rect = self.__nbrbarriere20.get_rect()
        self.__nbrbarriere20_rect.x = ceil(screen.get_width() / 2.5)
        self.__nbrbarriere20_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere24 = pygame.transform.scale(pygame.image.load('./images/page2/barriere24.PNG'), (120, 120))
        self.__nbrbarriere24_rect = self.__nbrbarriere24.get_rect()
        self.__nbrbarriere24_rect.x = ceil(screen.get_width() / 2.05)
        self.__nbrbarriere24_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere28 = pygame.transform.scale(pygame.image.load('./images/page2/barriere28.PNG'), (120, 120))
        self.__nbrbarriere28_rect = self.__nbrbarriere28.get_rect()
        self.__nbrbarriere28_rect.x = ceil(screen.get_width() / 1.73)
        self.__nbrbarriere28_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere32 = pygame.transform.scale(pygame.image.load('./images/page2/barriere32.PNG'), (120, 120))
        self.__nbrbarriere32_rect = self.__nbrbarriere32.get_rect()
        self.__nbrbarriere32_rect.x = ceil(screen.get_width() / 1.48)
        self.__nbrbarriere32_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere36 = pygame.transform.scale(pygame.image.load('./images/page2/barriere36.PNG'), (120, 120))
        self.__nbrbarriere36_rect = self.__nbrbarriere36.get_rect()
        self.__nbrbarriere36_rect.x = ceil(screen.get_width() / 1.3)
        self.__nbrbarriere36_rect.y = ceil(screen.get_width() / 1.8)

        self.__nbrbarriere40 = pygame.transform.scale(pygame.image.load('./images/page2/barriere40.PNG'), (120, 120))
        self.__nbrbarriere40_rect = self.__nbrbarriere40.get_rect()
        self.__nbrbarriere40_rect.x = ceil(screen.get_width() / 1.17)
        self.__nbrbarriere40_rect.y = ceil(screen.get_width() / 1.8)

        self.__jouerreseau = pygame.transform.scale(pygame.image.load('./images/page2/reseau.PNG'), (350, 100))
        self.__jouerreseau_rect = self.__jouerreseau.get_rect()
        self.__jouerreseau_rect.x = ceil(screen.get_width() / 2.1)
        self.__jouerreseau_rect.y = ceil(screen.get_width() / 1.55)
        
        self.__reset = pygame.transform.scale(pygame.image.load('./images/page2/reset.PNG'), (350, 100))
        self.__reset_rect = self.__reset.get_rect()
        self.__reset_rect.x = ceil(screen.get_width() / 1.475)
        self.__reset_rect.y = ceil(screen.get_width() / 17.5)
        
        self.__Play = pygame.transform.scale(pygame.image.load('./images/page2/play.PNG'), (350, 100))
        self.__Play_rect = self.__Play.get_rect()
        self.__Play_rect.x = ceil(screen.get_width() / 4)
        self.__Play_rect.y = ceil(screen.get_width() / 1.55)
        
    def ProcessInput(self, events, keys, screen):
        conf = self.__quoridor.GetConfig()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__Play_rect.collidepoint(event.pos) and self.__nbrPlayers != 0 and self.__taillePlateau != 0 and self.__nbrBarriere != 0:
                    self.GamePage()
                    self.__file.close()
                if self.__nbrPlayers2_rect.collidepoint(event.pos):
                    conf[0] = 2
                    self.__nbrPlayers2 = pygame.transform.scale(pygame.image.load('./images/page2/choix1ok.PNG'), (120, 120))
                if self.__nbrPlayers4_rect.collidepoint(event.pos):
                    conf[0] = 4
                    self.__nbrPlayers4 = pygame.transform.scale(pygame.image.load('./images/page2/choix2ok.PNG'), (120, 120))
                if self.__taillePlateau5_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                    conf[1] = 5 
                    self.__taillePlateau5 = pygame.transform.scale(pygame.image.load('./images/page2/5x5ok.PNG'), (280, 70))
                if self.__taillePlateau7_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                    conf[1] = 7
                    self.__taillePlateau7 = pygame.transform.scale(pygame.image.load('./images/page2/7x7ok.PNG'), (280, 70))
                if self.__taillePlateau9_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                    conf[1] = 9
                    self.__taillePlateau9 = pygame.transform.scale(pygame.image.load('./images/page2/9x9ok.PNG'), (280, 70))
                if self.__taillePlateau11_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                    conf[1] = 11
                    self.__taillePlateau11 = pygame.transform.scale(pygame.image.load('./images/page2/11x11ok.PNG'), (280, 70))
                if self.__nbrbarriere4_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 4
                    self.__nbrbarriere4 = pygame.transform.scale(pygame.image.load('./images/page2/barriere4ok.PNG'), (120, 120))
                if self.__nbrbarriere8_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 8
                    self.__nbrbarriere8 = pygame.transform.scale(pygame.image.load('./images/page2/barriere8ok.PNG'), (120, 120))
                if self.__nbrbarriere12_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 12
                    self.__nbrbarriere12 = pygame.transform.scale(pygame.image.load('./images/page2/barriere12ok.PNG'), (120, 120))
                if self.__nbrbarriere16_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 16
                    self.__nbrbarriere16 = pygame.transform.scale(pygame.image.load('./images/page2/barriere16ok.PNG'), (120, 120))
                if self.__nbrbarriere20_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 20
                    self.__nbrbarriere20 = pygame.transform.scale(pygame.image.load('./images/page2/barriere20ok.PNG'), (120, 120))
                if self.__nbrbarriere24_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 24
                    self.__nbrbarriere24 = pygame.transform.scale(pygame.image.load('./images/page2/barriere24ok.PNG'), (120, 120))
                if self.__nbrbarriere28_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 28
                    self.__nbrbarriere28 = pygame.transform.scale(pygame.image.load('./images/page2/barriere28ok.PNG'), (120, 120))
                if self.__nbrbarriere32_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 32
                    self.__nbrbarriere32 = pygame.transform.scale(pygame.image.load('./images/page2/barriere32ok.PNG'), (120, 120))
                if self.__nbrbarriere36_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 36
                    self.__nbrbarriere36 = pygame.transform.scale(pygame.image.load('./images/page2/barriere36ok.PNG'), (120, 120))
                if self.__nbrbarriere40_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                    conf[2] = 40
                    self.__nbrbarriere40 = pygame.transform.scale(pygame.image.load('./images/page2/barriere40ok.PNG'), (120, 120))
                if self.__jouerreseau_rect.collidepoint(event.pos):
                    self.__PlayInReseau = True
                    self.__jouerreseau = pygame.transform.scale(pygame.image.load('./images/page2/reseauok.PNG'), (350, 100))
                if self.__reset_rect.collidepoint(event.pos):
                    self.__nbrBarriere= 0
                    self.__taillePlateau = 0
                    self.__nbrPlayers = 0
        
    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.__background, (0,0))
        screen.blit(self.__titre, self.__titre_rect)
        screen.blit(self.__titrenbrPlayers, self.__titrenbrPlayers_rect)
        screen.blit(self.__nbrPlayers2, self.__nbrPlayers2_rect)
        screen.blit(self.__nbrPlayers4, self.__nbrPlayers4_rect)
        screen.blit(self.__titretaillePlateau, self.__titretaillePlateau_rect)
        screen.blit(self.__taillePlateau5, self.__taillePlateau5_rect)
        screen.blit(self.__taillePlateau7, self.__taillePlateau7_rect)
        screen.blit(self.__taillePlateau9, self.__taillePlateau9_rect)
        screen.blit(self.__taillePlateau11, self.__taillePlateau11_rect)
        screen.blit(self.__titrenbrbarriere, self.__titrenbrbarriere_rect)
        screen.blit(self.__nbrbarriere4, self.__nbrbarriere4_rect)
        screen.blit(self.__nbrbarriere8, self.__nbrbarriere8_rect)
        screen.blit(self.__nbrbarriere12, self.__nbrbarriere12_rect)
        screen.blit(self.__nbrbarriere16, self.__nbrbarriere16_rect)
        screen.blit(self.__nbrbarriere20, self.__nbrbarriere20_rect)
        screen.blit(self.__nbrbarriere24, self.__nbrbarriere24_rect)
        screen.blit(self.__nbrbarriere28, self.__nbrbarriere28_rect)
        screen.blit(self.__nbrbarriere32, self.__nbrbarriere32_rect)
        screen.blit(self.__nbrbarriere36, self.__nbrbarriere36_rect)
        screen.blit(self.__nbrbarriere40, self.__nbrbarriere40_rect)
        screen.blit(self.__jouerreseau, self.__jouerreseau_rect)
        screen.blit(self.__reset, self.__reset_rect)
        screen.blit(self.__Play, self.__Play_rect)