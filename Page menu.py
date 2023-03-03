from math import ceil
import pygame

class Case():
    def __init__(self,state=0):
        self.__state=state

    def getState(self):
        return self.__state
    def setState(self,state):
        self.__state=state

class MainPage:
    def __init__(self):
        self.__Page2=False
        self.__Page3=False
        self.__nbrPlayers = 0
        self.__taillePlateau = 0
        self.__nbrBarriere = 0
        self.__PlayInReseau = False
        # Espacement entre les cases
        self.__espacement = 80
        # Position de départ de la grille
        self.__pos_x = 40
        self.__pos_y = 40

        pygame.init()
        # Générer la fenêtre du jeu
        pygame.display.set_caption("Jeu du QUORIDOR")
        self.__image = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(self.__image)
        self.__screen = pygame.display.set_mode(size=(1160, 920))

        self.__background = pygame.image.load('./images/page1/background1.jpg')

        #Générer les images de la page de jeu
        self.__banner = pygame.transform.scale(pygame.image.load('./images/page1/game.PNG'), (700, 150))
        self.__banner_rect = self.__banner.get_rect()
        self.__banner_rect.x = ceil(self.__screen.get_width() / 4.7)
        self.__banner_rect.y = ceil(self.__screen.get_width() / 4)

        self.__play_button = pygame.transform.scale(pygame.image.load('./images/page1/play.PNG'), (235, 90))
        self.__play_button_rect = self.__play_button.get_rect()
        self.__play_button_rect.x = ceil(self.__screen.get_width() / 2.43)
        self.__play_button_rect.y = ceil(self.__screen.get_height() / 1.635)

        self.__Play = pygame.transform.scale(pygame.image.load('./images/page2/play.PNG'), (350, 100))
        self.__Play_rect = self.__Play.get_rect()
        self.__Play_rect.x = ceil(self.__screen.get_width() / 4)
        self.__Play_rect.y = ceil(self.__screen.get_width() / 1.55)


        self.__game_is_running = True
        # Boucle tant que le jeu est en cours
        while self.__game_is_running:
            # Application des images 
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.__play_button, self.__play_button_rect)
            self.__screen.blit(self.__banner, self.__banner_rect)
            if self.__Page2:
                self.__screen.blit(self.__titre, self.__titre_rect)
                self.__screen.blit(self.__titrenbrPlayers, self.__titrenbrPlayers_rect)
                self.__screen.blit(self.__nbrPlayers2, self.__nbrPlayers2_rect)
                self.__screen.blit(self.__nbrPlayers4, self.__nbrPlayers4_rect)
                self.__screen.blit(self.__titretaillePlateau, self.__titretaillePlateau_rect)
                self.__screen.blit(self.__taillePlateau5, self.__taillePlateau5_rect)
                self.__screen.blit(self.__taillePlateau7, self.__taillePlateau7_rect)
                self.__screen.blit(self.__taillePlateau9, self.__taillePlateau9_rect)
                self.__screen.blit(self.__taillePlateau11, self.__taillePlateau11_rect)
                self.__screen.blit(self.__titrenbrbarriere, self.__titrenbrbarriere_rect)
                self.__screen.blit(self.__nbrbarriere4, self.__nbrbarriere4_rect)
                self.__screen.blit(self.__nbrbarriere8, self.__nbrbarriere8_rect)
                self.__screen.blit(self.__nbrbarriere12, self.__nbrbarriere12_rect)
                self.__screen.blit(self.__nbrbarriere16, self.__nbrbarriere16_rect)
                self.__screen.blit(self.__nbrbarriere20, self.__nbrbarriere20_rect)
                self.__screen.blit(self.__nbrbarriere24, self.__nbrbarriere24_rect)
                self.__screen.blit(self.__nbrbarriere28, self.__nbrbarriere28_rect)
                self.__screen.blit(self.__nbrbarriere32, self.__nbrbarriere32_rect)
                self.__screen.blit(self.__nbrbarriere36, self.__nbrbarriere36_rect)
                self.__screen.blit(self.__nbrbarriere40, self.__nbrbarriere40_rect)
                self.__screen.blit(self.__jouerreseau, self.__jouerreseau_rect)
                self.__screen.blit(self.__reset, self.__reset_rect)
                self.__screen.blit(self.__Play, self.__Play_rect)

            # mise à jour de l'écran
            pygame.display.flip()

            # Boucle sur les événements
            for event in pygame.event.get():
                # événement de fermeture de fenêtre
                if event.type == pygame.QUIT:
                    self.__game_is_running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__play_button_rect.collidepoint(event.pos):
                        self.SecondPage()
                    if self.__Play_rect.collidepoint(event.pos) and self.__nbrPlayers != 0 and self.__taillePlateau != 0 and self.__nbrBarriere != 0:
                        self.GamePage()
                    if self.__nbrPlayers2_rect.collidepoint(event.pos) and self.__nbrPlayers ==0:
                        self.__nbrPlayers = 2
                        self.__nbrPlayers2 = pygame.transform.scale(pygame.image.load('./images/page2/choix1ok.PNG'), (120, 120))
                    if self.__nbrPlayers4_rect.collidepoint(event.pos) and self.__nbrPlayers ==0:
                        self.__nbrPlayers = 4
                        self.__nbrPlayers4 = pygame.transform.scale(pygame.image.load('./images/page2/choix2ok.PNG'), (120, 120))
                    if self.__taillePlateau5_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                        self.__taillePlateau = 5 
                        self.__taillePlateau5 = pygame.transform.scale(pygame.image.load('./images/page2/5x5ok.PNG'), (280, 70))
                    if self.__taillePlateau7_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                        self.__taillePlateau = 7
                        self.__taillePlateau7 = pygame.transform.scale(pygame.image.load('./images/page2/7x7ok.PNG'), (280, 70))
                    if self.__taillePlateau9_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                        self.__taillePlateau = 9
                        self.__taillePlateau9 = pygame.transform.scale(pygame.image.load('./images/page2/9x9ok.PNG'), (280, 70))
                    if self.__taillePlateau11_rect.collidepoint(event.pos) and self.__taillePlateau == 0:
                        self.__taillePlateau = 11 
                        self.__taillePlateau11 = pygame.transform.scale(pygame.image.load('./images/page2/11x11ok.PNG'), (280, 70))
                    if self.__nbrbarriere4_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 4
                        self.__nbrbarriere4 = pygame.transform.scale(pygame.image.load('./images/page2/barriere4ok.PNG'), (120, 120))
                    if self.__nbrbarriere8_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 8
                        self.__nbrbarriere8 = pygame.transform.scale(pygame.image.load('./images/page2/barriere8ok.PNG'), (120, 120))
                    if self.__nbrbarriere12_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 12
                        self.__nbrbarriere12 = pygame.transform.scale(pygame.image.load('./images/page2/barriere12ok.PNG'), (120, 120))
                    if self.__nbrbarriere16_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 16
                        self.__nbrbarriere16 = pygame.transform.scale(pygame.image.load('./images/page2/barriere16ok.PNG'), (120, 120))
                    if self.__nbrbarriere20_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 20
                        self.__nbrbarriere20 = pygame.transform.scale(pygame.image.load('./images/page2/barriere20ok.PNG'), (120, 120))
                    if self.__nbrbarriere24_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 24
                        self.__nbrbarriere24 = pygame.transform.scale(pygame.image.load('./images/page2/barriere24ok.PNG'), (120, 120))
                    if self.__nbrbarriere28_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 28
                        self.__nbrbarriere28 = pygame.transform.scale(pygame.image.load('./images/page2/barriere28ok.PNG'), (120, 120))
                    if self.__nbrbarriere32_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 32
                        self.__nbrbarriere32 = pygame.transform.scale(pygame.image.load('./images/page2/barriere32ok.PNG'), (120, 120))
                    if self.__nbrbarriere36_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 36
                        self.__nbrbarriere36 = pygame.transform.scale(pygame.image.load('./images/page2/barriere36ok.PNG'), (120, 120))
                    if self.__nbrbarriere40_rect.collidepoint(event.pos) and self.__nbrBarriere == 0:
                        self.__nbrBarriere= 40
                        self.__nbrbarriere40 = pygame.transform.scale(pygame.image.load('./images/page2/barriere40ok.PNG'), (120, 120))
                    if self.__jouerreseau_rect.collidepoint(event.pos):
                        self.__PlayInReseau = True
                        self.__jouerreseau = pygame.transform.scale(pygame.image.load('./images/page2/reseauok.PNG'), (350, 100))
                    if self.__reset_rect.collidepoint(event.pos):
                        self.__nbrBarriere= 0
                        self.__taillePlateau = 0
                        self.__nbrPlayers = 0
                        self.SecondPage()


    def SecondPage(self):
        self.__Page2=True
        self.__background = pygame.image.load('./images/page2/background3.jpg')
        self.__banner_rect.x,self.__banner_rect.y = 2000,1000
        self.__play_button_rect.x,self.__play_button_rect.y = 2000,1000

        self.__titre = pygame.transform.scale(pygame.image.load('./images/page2/titre.PNG'), (700, 150))
        self.__titre_rect = self.__titre.get_rect()
        self.__titre_rect.x = ceil(self.__screen.get_width() / 4.7)
        self.__titre_rect.y = ceil(self.__screen.get_width() / 65)

        self.__titrenbrPlayers = pygame.transform.scale(pygame.image.load('./images/page2/nbrplayers.PNG'), (320, 50))
        self.__titrenbrPlayers_rect = self.__titrenbrPlayers.get_rect()
        self.__titrenbrPlayers_rect.x = ceil(self.__screen.get_width() / 2.7)
        self.__titrenbrPlayers_rect.y = ceil(self.__screen.get_width() / 6)

        self.__nbrPlayers2 = pygame.transform.scale(pygame.image.load('./images/page2/choix1.PNG'), (120, 120))
        self.__nbrPlayers2_rect = self.__nbrPlayers2.get_rect()
        self.__nbrPlayers2_rect.x = ceil(self.__screen.get_width() / 3.1)
        self.__nbrPlayers2_rect.y = ceil(self.__screen.get_width() / 4.6)

        self.__nbrPlayers4 = pygame.transform.scale(pygame.image.load('./images/page2/choix2.PNG'), (120, 120))
        self.__nbrPlayers4_rect = self.__nbrPlayers4.get_rect()
        self.__nbrPlayers4_rect.x = ceil(self.__screen.get_width() / 1.7)
        self.__nbrPlayers4_rect.y = ceil(self.__screen.get_width() / 4.6)

        self.__titretaillePlateau = pygame.transform.scale(pygame.image.load('./images/page2/tailleplateau.PNG'), (320, 50))
        self.__titretaillePlateau_rect = self.__titretaillePlateau.get_rect()
        self.__titretaillePlateau_rect.x = ceil(self.__screen.get_width() / 2.7)
        self.__titretaillePlateau_rect.y = ceil(self.__screen.get_width() / 3.2)

        self.__taillePlateau5 = pygame.transform.scale(pygame.image.load('./images/page2/5x5.PNG'), (280, 70))
        self.__taillePlateau5_rect = self.__taillePlateau5.get_rect()
        self.__taillePlateau5_rect.x = ceil(self.__screen.get_width() / 22)
        self.__taillePlateau5_rect.y = ceil(self.__screen.get_width() / 2.5)

        self.__taillePlateau7 = pygame.transform.scale(pygame.image.load('./images/page2/7x7.PNG'), (280, 70))
        self.__taillePlateau7_rect = self.__taillePlateau7.get_rect()
        self.__taillePlateau7_rect.x = ceil(self.__screen.get_width() / 3.7)
        self.__taillePlateau7_rect.y = ceil(self.__screen.get_width() / 2.5)

        self.__taillePlateau9 = pygame.transform.scale(pygame.image.load('./images/page2/9x9.PNG'), (280, 70))
        self.__taillePlateau9_rect = self.__taillePlateau9.get_rect()
        self.__taillePlateau9_rect.x = ceil(self.__screen.get_width() / 2)
        self.__taillePlateau9_rect.y = ceil(self.__screen.get_width() / 2.5)

        self.__taillePlateau11 = pygame.transform.scale(pygame.image.load('./images/page2/11x11.PNG'), (280, 70))
        self.__taillePlateau11_rect = self.__taillePlateau11.get_rect()
        self.__taillePlateau11_rect.x = ceil(self.__screen.get_width() / 1.37)
        self.__taillePlateau11_rect.y = ceil(self.__screen.get_width() / 2.5)

        self.__titrenbrbarriere = pygame.transform.scale(pygame.image.load('./images/page2/nbrBarriere.PNG'), (320, 50))
        self.__titrenbrbarriere_rect = self.__titrenbrbarriere.get_rect()
        self.__titrenbrbarriere_rect.x = ceil(self.__screen.get_width() / 2.5)
        self.__titrenbrbarriere_rect.y = ceil(self.__screen.get_width() / 2.5)

        self.__nbrbarriere4 = pygame.transform.scale(pygame.image.load('./images/page2/barriere4.PNG'), (120, 120))
        self.__nbrbarriere4_rect = self.__nbrbarriere4.get_rect()
        self.__nbrbarriere4_rect.x = ceil(self.__screen.get_width() / 30)
        self.__nbrbarriere4_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere8 = pygame.transform.scale(pygame.image.load('./images/page2/barriere8.PNG'), (120, 120))
        self.__nbrbarriere8_rect = self.__nbrbarriere8.get_rect()
        self.__nbrbarriere8_rect.x = ceil(self.__screen.get_width() / 8)
        self.__nbrbarriere8_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere12 = pygame.transform.scale(pygame.image.load('./images/page2/barriere12.PNG'), (120, 120))
        self.__nbrbarriere12_rect = self.__nbrbarriere12.get_rect()
        self.__nbrbarriere12_rect.x = ceil(self.__screen.get_width() / 4.6)
        self.__nbrbarriere12_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere16 = pygame.transform.scale(pygame.image.load('./images/page2/barriere16.PNG'), (120, 120))
        self.__nbrbarriere16_rect = self.__nbrbarriere16.get_rect()
        self.__nbrbarriere16_rect.x = ceil(self.__screen.get_width() / 3.25)
        self.__nbrbarriere16_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere20 = pygame.transform.scale(pygame.image.load('./images/page2/barriere20.PNG'), (120, 120))
        self.__nbrbarriere20_rect = self.__nbrbarriere20.get_rect()
        self.__nbrbarriere20_rect.x = ceil(self.__screen.get_width() / 2.5)
        self.__nbrbarriere20_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere24 = pygame.transform.scale(pygame.image.load('./images/page2/barriere24.PNG'), (120, 120))
        self.__nbrbarriere24_rect = self.__nbrbarriere24.get_rect()
        self.__nbrbarriere24_rect.x = ceil(self.__screen.get_width() / 2.05)
        self.__nbrbarriere24_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere28 = pygame.transform.scale(pygame.image.load('./images/page2/barriere28.PNG'), (120, 120))
        self.__nbrbarriere28_rect = self.__nbrbarriere28.get_rect()
        self.__nbrbarriere28_rect.x = ceil(self.__screen.get_width() / 1.73)
        self.__nbrbarriere28_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere32 = pygame.transform.scale(pygame.image.load('./images/page2/barriere32.PNG'), (120, 120))
        self.__nbrbarriere32_rect = self.__nbrbarriere32.get_rect()
        self.__nbrbarriere32_rect.x = ceil(self.__screen.get_width() / 1.48)
        self.__nbrbarriere32_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere36 = pygame.transform.scale(pygame.image.load('./images/page2/barriere36.PNG'), (120, 120))
        self.__nbrbarriere36_rect = self.__nbrbarriere36.get_rect()
        self.__nbrbarriere36_rect.x = ceil(self.__screen.get_width() / 1.3)
        self.__nbrbarriere36_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__nbrbarriere40 = pygame.transform.scale(pygame.image.load('./images/page2/barriere40.PNG'), (120, 120))
        self.__nbrbarriere40_rect = self.__nbrbarriere40.get_rect()
        self.__nbrbarriere40_rect.x = ceil(self.__screen.get_width() / 1.17)
        self.__nbrbarriere40_rect.y = ceil(self.__screen.get_width() / 1.8)

        self.__jouerreseau = pygame.transform.scale(pygame.image.load('./images/page2/reseau.PNG'), (350, 100))
        self.__jouerreseau_rect = self.__jouerreseau.get_rect()
        self.__jouerreseau_rect.x = ceil(self.__screen.get_width() / 2.1)
        self.__jouerreseau_rect.y = ceil(self.__screen.get_width() / 1.55)
        
        self.__reset = pygame.transform.scale(pygame.image.load('./images/page2/reset.PNG'), (350, 100))
        self.__reset_rect = self.__reset.get_rect()
        self.__reset_rect.x = ceil(self.__screen.get_width() / 1.475)
        self.__reset_rect.y = ceil(self.__screen.get_width() / 17.5)

    def draw(self):
        self.__grid = []
        for x in range(self.__taillePlateau):
            self.__grid.append([])
            for y in range(self.__taillePlateau):
                self.__grid[x].append(Case(0))
        self.__index=self.__taillePlateau//2
        self.__grid[0][self.__index].setState(1)
        self.__grid[self.__taillePlateau-1][self.__index].setState(2)

        # Boucle pour dessiner les cases
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid)):
                rect = pygame.Rect(self.__pos_x, self.__pos_y, 40, 40)
                pygame.draw.rect(self.__screen, (0, 0, 255), rect,5)
                if i <self.__taillePlateau-1:
                    # Dessiner un rectangle en dessous
                    rect_down = pygame.Rect(self.__pos_x, self.__pos_y+50, 40, 8)
                    pygame.draw.rect(self.__screen, (0, 0, 0), rect_down)
                if i<0:
                    # Dessiner un rectangle au dessus
                    rect_up = pygame.Rect(self.__pos_x, self.__pos_y-20, 40, 8)
                    pygame.draw.rect(self.__screen, (0, 0, 0), rect_up)
                if j<0:
                    # Dessiner un rectangle à gauche
                    rect_left = pygame.Rect(self.__pos_x-20, self.__pos_y, 8, 40)
                    pygame.draw.rect(self.__screen, (0, 0, 0), rect_left)
                if j<self.__taillePlateau-1:
                    # Dessiner un rectangle à droite
                    rect_right = pygame.Rect(self.__pos_x+55, self.__pos_y, 8, 40)
                    pygame.draw.rect(self.__screen, (0, 0, 0), rect_right)
                if self.__grid[i][j].getState() == 1:
                    pygame.draw.circle(self.__screen, (255,0,0), (self.__pos_x + 20, self.__pos_y + 20), 15)
                if self.__grid[i][j].getState() == 2:
                    pygame.draw.circle(self.__screen, (0,255,0), (self.__pos_x + 20, self.__pos_y + 20), 15)
                self.__pos_x += self.__espacement
            self.__pos_x = 40
            self.__pos_y += self.__espacement

    def GamePage(self):
        self.__Page3=True 
        self.__background = pygame.image.load('./images/page3/tr.PNG')
        self.__screen.fill((255,255,255))
        self.__titre_rect.x,self.__titre_rect.y =3000,1500
        self.__titrenbrPlayers_rect.x,self.__titrenbrPlayers_rect.y = 3000,1500
        self.__nbrPlayers2_rect.x,self.__nbrPlayers2_rect.y = 3000,1500
        self.__nbrPlayers4_rect.x,self.__nbrPlayers4_rect.y = 3000,1500
        self.__titretaillePlateau_rect.x,self.__titretaillePlateau_rect.y = 3000,1500
        self.__taillePlateau5_rect.x,self.__taillePlateau5_rect.y = 3000,1500
        self.__taillePlateau7_rect.x,self.__taillePlateau7_rect.y = 3000,1500
        self.__taillePlateau9_rect.x,self.__taillePlateau9_rect.y = 3000,1500
        self.__taillePlateau11_rect.x,self.__taillePlateau11_rect.y = 3000,1500
        self.__titrenbrbarriere_rect.x,self.__titrenbrbarriere_rect.y = 3000,1500
        self.__nbrbarriere4_rect.x,self.__nbrbarriere4_rect.y = 3000,1500
        self.__nbrbarriere8_rect.x,self.__nbrbarriere8_rect.y = 3000,1500
        self.__nbrbarriere12_rect.x,self.__nbrbarriere12_rect.y = 3000,1500
        self.__nbrbarriere16_rect.x,self.__nbrbarriere16_rect.y = 3000,1500
        self.__nbrbarriere20_rect.x,self.__nbrbarriere20_rect.y = 3000,1500
        self.__nbrbarriere24_rect.x,self.__nbrbarriere24_rect.y = 3000,1500
        self.__nbrbarriere28_rect.x,self.__nbrbarriere28_rect.y = 3000,1500
        self.__nbrbarriere32_rect.x,self.__nbrbarriere32_rect.y = 3000,1500
        self.__nbrbarriere36_rect.x,self.__nbrbarriere36_rect.y = 3000,1500
        self.__nbrbarriere40_rect.x,self.__nbrbarriere40_rect.y = 3000,1500
        self.__jouerreseau_rect.x,self.__jouerreseau_rect.y = 3000,1500
        self.__reset_rect.x,self.__jouerreseau_rect.y = 3000,1500
        self.__Play_rect.x,self.__Play_rect.y = 3000,1500
        self.draw()

        print("le nombre de joueur est",self.__nbrPlayers,"\n La largueur du plateau est",self.__taillePlateau,"\n Le nombre de barrière est",self.__nbrBarriere,"\n La partie est jouer en reseau",self.__PlayInReseau,"\n la couleur des joueurs est ",self.CouleurPlayers())

    def CouleurPlayers(self):
        if self.__nbrPlayers==2:
            print("ok")
            return ["red","green"]
        elif self.__nbrPlayers == 4:
            return ["red","green","purple","orange"]

'''Les murs sernt en noir et les cases de couleur bleu *
Les 4 couluers des joueurs sont rouge, vert, violet et orange '''

if __name__ == '__main__':
    MainPage()