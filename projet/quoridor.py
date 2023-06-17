import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, settings as settings
from render.scene.startscene import StartScene
from network.client import NetClientManager
from render.surfacemanager import SurfaceManager
from console import Console
from utils import CheckJson
from render.fontsmanager import FontManager

class Quoridor():
    def __init__(self):
        self.__console = Console()
        self.__console.RegisterCommand("exit", lambda args: pygame.event.post(pygame.event.Event(pygame.QUIT)), "Permet de quiter le processus en cour")
        self.__console.log("[green]Starting[/green]")
        self.__console.log("Init PyGame", style="#af00ff")
        self.__json = CheckJson("configs/global.json")
        pygame.init()  # Init pygame
        self.__display_surface = pygame.display.set_mode(settings.DISPLAY_SIZE)
        self.__surface_manager = SurfaceManager()
        self.__font_manager = FontManager(self.__json)
        pygame.display.set_caption(settings.CAPTION)
        pygame.display.set_icon(self.__surface_manager.GetSurface(settings.ICON_PATH))
        pygame.event.set_allowed(pygame.QUIT)
        self.__clock = pygame.time.Clock()
        self.__active_scene = None
        self.__active_scene = StartScene(self)
        self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")
        self.__netclient = NetClientManager()
        self.__force_redraw_rects = []
        
        self.Run()
        
    def GetSurfaceManager(self):
        return self.__surface_manager
        
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
                    continue
                if event.type == pygame.MOUSEBUTTONUP:  # If mouse up event
                    self.__active_scene.MouseUp()
                    continue
                if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                    display_settings = settings.DISPLAY_SIZE
                    rect = pygame.Rect(0, 0, display_settings[0], display_settings[1])
                    update_rects.append(rect)
                    self.__active_scene.GetMainGroup().repaint_rect(rect)
                    continue
                if (event.type == pygame.KEYDOWN):
                    self.__active_scene.InputPressed(event.key)
                    continue
                if (event.type == pygame.KEYUP):
                    self.__active_scene.InputReleased(event.key)
                    continue
            self.__display_surface.blit(self.__active_scene.GetBackGroundSurface(), (0, 0))
            self.__active_scene.Update()
            self.__active_scene.Input(pygame.key.get_pressed())
            for rect in self.__active_scene.Render(self.__display_surface):
                update_rects.append(rect)
            if (self.__force_redraw_rects):
                update_rects.extend(self.__force_redraw_rects)
                pygame.display.update(update_rects)
                self.__force_redraw_rects.clear()
            else:
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
    
    def AddRedrawRect(self, rect):
        self.__force_redraw_rects.append(rect)
        
    def GetActiveScene(self):
        return self.__active_scene
    
    def GetGlobalJson(self):
        return self.__json
    
    def GetFontManager(self):
        return self.__font_manager

if __name__ == "__main__":
    """Main function"""
    QUORIDOR = Quoridor()