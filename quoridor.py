import pygame, sys, settings
from render.scene.startscene import StartScene

class Quoridor():
    def __init__(self):
        pygame.init()
        self.__display_surface = pygame.display.set_mode(settings.DISPLAY_SIZE)
        pygame.display.set_caption(settings.CAPTION)
        pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())
        pygame.event.set_allowed(pygame.QUIT)
        self.__clock = pygame.time.Clock()
        self.__active_scene = StartScene(self.__display_surface)
        
        self.Run()
        pass
    
    def Run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__active_scene.MouseDown()
            self.__active_scene.Update()
            self.__active_scene.Input(pygame.key.get_pressed())
            pygame.display.flip()
            self.__clock.tick(settings.MAX_TICKS)
            
if __name__ == "__main__":
    Quoridor()