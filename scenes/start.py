from scenes.scenebase import SceneBase
from scenes.config import SceneConfig
from math import ceil
import pygame

class SceneStart(SceneBase):
    def __init__(self, screen, quoridor):
        self.__quoridor = quoridor
        SceneBase.__init__(self,screen)
        self.__background = pygame.image.load('./images/page1/background1.jpg')
        
        self.__banner = pygame.transform.scale(pygame.image.load('./images/page1/game.PNG').convert_alpha(), (700, 150))
        self.__banner_rect = self.__banner.get_rect()
        self.__banner_rect.x = ceil(screen.get_width() / 4.7)
        self.__banner_rect.y = ceil(screen.get_width() / 4)

        self.__play_button = pygame.transform.scale(pygame.image.load('./images/page1/play.PNG').convert_alpha(), (235, 90))
        self.__play_button_rect = self.__play_button.get_rect()
        self.__play_button_rect.x = ceil(screen.get_width() / 2.43)
        self.__play_button_rect.y = ceil(screen.get_height() / 1.635)
        
    def ProcessInput(self, events, keys, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.__play_button_rect.collidepoint(event.pos):
                self.SwitchToScene(SceneConfig(screen, self.__quoridor))
        
    def Update(self):
        pass
    
    def FirstRender(self, screen):
        print("FirstRender")
        screen.blit(self.__background, (0,0))
        screen.blit(self.__play_button, self.__play_button_rect)
        screen.blit(self.__banner, self.__banner_rect)