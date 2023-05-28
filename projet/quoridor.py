import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, settings as settings
from render.scene.startscene import StartScene
from network.client import NetClientManager
from console import Console

class Quoridor():
    def __init__(self):
        self.__console = Console()  # Console de debug
        self.__console.RegisterCommand("exit", lambda args: pygame.event.post(pygame.event.Event(pygame.QUIT)), "Permet de quiter le processus en cour")
        self.__console.log("[green]Starting[/green]")
        self.__console.log("Init PyGame", style="#af00ff")
        pygame.init()  # Init pygame
        self.__display_surface = pygame.display.set_mode(settings.DISPLAY_SIZE)  # Init display
        pygame.display.set_caption(settings.CAPTION)  # Set caption
        pygame.display.set_icon(pygame.image.load(settings.ICON_PATH).convert_alpha())  # Set icon
        pygame.event.set_allowed(pygame.QUIT)  # Allow to quit event
        self.__clock = pygame.time.Clock()
        self.__active_scene = StartScene(self)  # Init active scene
        self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")
        self.__netclient = NetClientManager()
        
        self.Run()
        
    def GetNetClient(self):
        """Return the net client"""
        return self.__netclient
    
    def Run(self):
        """Run the game"""
        while 1:  # Main loop
            update_rects = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If quit event
                    pygame.quit()
                    self.__console.log("[red]EXIT[/red]")
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:  # If mouse down event
                    self.__active_scene.MouseDown()
                if event.type == pygame.MOUSEBUTTONUP:  # If mouse up event
                    self.__active_scene.MouseUp()
                if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                    display_settings = settings.DISPLAY_SIZE
                    rect = pygame.Rect(0, 0, display_settings[0], display_settings[1])
                    update_rects.append(rect)
                    self.__active_scene.GetMainGroup().repaint_rect(rect)
            self.__display_surface.blit(self.__active_scene.GetBackGroundSurface(), (0, 0))
            self.__active_scene.Update()
            self.__active_scene.Input(pygame.key.get_pressed())
            for rect in self.__active_scene.Render(self.__display_surface):
                update_rects.append(rect)
            pygame.display.update(update_rects)
            self.__clock.tick(settings.MAX_TICKS)
            if self.__active_scene.Next() != False:  # If next scene
                self.__active_scene = self.__active_scene.Next()
                self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")

    def GetConsole(self):
        """Return the console"""
        return self.__console
    
    def GetDisplaySurface(self):
        """Return the display surface"""
        return self.__display_surface

if __name__ == "__main__":
    """Main function"""
    QUORIDOR = Quoridor()
