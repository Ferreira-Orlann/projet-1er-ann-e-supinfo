import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, settings
from render.scene.startscene import StartScene
from network.client import NetClientManager
from console import Console
from time import sleep

class Quoridor():
    def __init__(self):
        self.__console = Console()
        self.__console.RegisterCommand("exit", lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)))
        self.__console.log("[green]Starting[/green]")
        self.__console.log("Init PyGame", style="#af00ff")
        pygame.init()
        self.__display_surface = pygame.display.set_mode(settings.DISPLAY_SIZE)
        pygame.display.set_caption(settings.CAPTION)
        pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())
        pygame.event.set_allowed(pygame.QUIT)
        self.__clock = pygame.time.Clock()
        self.__active_scene = StartScene(self.__display_surface)
        self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")
        self.__netclient = NetClientManager()
        self.Run()
        pass
    
    def GetCmdsManager(self):
        return self.__cmdsmanager
    
    def Run(self):
        while 1:
            update_rects = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.__console.log("[red]EXIT[/red]")
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__active_scene.MouseDown()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__active_scene.MouseUp()
                if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                    display_settings = settings.DISPLAY_SIZE
                    rect = pygame.Rect(0,0,display_settings[0],display_settings[1])
                    update_rects.append(rect)
                    self.__active_scene.GetMainGroup().repaint_rect(rect)
            self.__display_surface.blit(self.__active_scene.GetBackGroundSurface(), (0,0))
            self.__active_scene.Update()
            self.__active_scene.Input(pygame.key.get_pressed())
            for rect in self.__active_scene.Render(self.__display_surface):
                update_rects.append(rect)
            pygame.display.update(update_rects)
            self.__clock.tick(settings.MAX_TICKS)
            if self.__active_scene.Next() != False:
                self.__active_scene = self.__active_scene.Next()
                self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")

    def GetConsole(self):
        return self.__console

if __name__ == "__main__":
    QUORIDOR = Quoridor()