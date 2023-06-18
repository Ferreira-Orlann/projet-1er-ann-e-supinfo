import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, settings as settings
from render.scene.startscene import StartScene
from render.surfacemanager import SurfaceManager
from console import Console
from utils import CheckJson
from render.fontsmanager import FontManager

class Quoridor():
    def __init__(self):
        self.__console = Console()
        self.__console.RegisterCommand("exit", self.__console.Quit, "Permet de quiter le processus en cour")
        self.__console.log("[green]Starting[/green]")
        self.__console.log("Init PyGame", style="#af00ff")
        self.__force_redraw_rects = []
        self.__json = CheckJson("configs/global.json")
        self.__netclient = None
        pygame.init()
        pygame.mixer.init()
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
        
        self.Run()
        
    def GetSurfaceManager(self):
        return self.__surface_manager
    
    def SetNetClient(self, net_client):
        self.__netclient = net_client
        
    def GetNetClient(self):
        return self.__netclient
    
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
                    continue
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__active_scene.MouseUp()
                    continue
                if event.type == pygame.VIDEOEXPOSE or event.type == pygame.VIDEORESIZE:
                    display_settings = settings.DISPLAY_SIZE
                    rect = pygame.Rect(0, 0, display_settings[0], display_settings[1])
                    update_rects.append(rect)
                    self.__active_scene.GetMainGroup().repaint_rect(rect)
                    continue
                if (event.type == pygame.KEYDOWN):
                    self.__active_scene.InputPressed(event)
                    self.__active_scene.InternalInputPressed(event)
                    continue
                if (event.type == pygame.KEYUP):
                    self.__active_scene.InputReleased(event)
                    continue
            self.__display_surface.blit(self.__active_scene.GetBackGroundSurface(), (0, 0))
            self.__active_scene.InternalUpdate()
            self.__active_scene.Update()
            self.__active_scene.Inputs(pygame.key.get_pressed())
            for rect in self.__active_scene.Render(self.__display_surface):
                update_rects.append(rect)
            if (self.__force_redraw_rects):
                update_rects.extend(self.__force_redraw_rects)
                pygame.display.update(update_rects)
                self.__force_redraw_rects.clear()
            else:
                pygame.display.update(update_rects)
            self.__clock.tick(settings.MAX_TICKS)
            if self.__active_scene.Next() != False:
                self.__active_scene = self.__active_scene.Next()
                self.__console.log("Changement de scène: " + str(self.__active_scene), style="#af00ff")

    def GetConsole(self):
        return self.__console
    
    def GetDisplaySurface(self):
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
    QUORIDOR = Quoridor()