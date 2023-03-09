import pygame, sys, settings
from render.scene.startscene import StartScene
from network.client import NetClientManager

class Quoridor():
    def __init__(self):
        pygame.init()
        self.__display_surface = pygame.display.set_mode(settings.DISPLAY_SIZE)
        pygame.display.set_caption(settings.CAPTION)
        pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())
        pygame.event.set_allowed(pygame.QUIT)
        self.__clock = pygame.time.Clock()
        self.__active_scene = StartScene(self.__display_surface)
        self.__netclient = NetClientManager()
        
        self.Run()
        pass
    
    def Run(self):
        while 1:
            update_rects = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__active_scene.MouseDown()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__active_scene.MouseUp()
                if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                    display_settings = settings.DISPLAY_SIZE
                    update_rects.append(pygame.Rect(0,0,display_settings[0],display_settings[1]))
            self.__active_scene.Update()
            self.__active_scene.Input(pygame.key.get_pressed())
            update_rects.extend(self.__active_scene.Render(self.__display_surface))
            pygame.display.update(update_rects)
            self.__clock.tick(settings.MAX_TICKS)
            if self.__active_scene.Next() != False:
                self.__active_scene = self.__active_scene.Next()

if __name__ == "__main__":
    Quoridor()