import pygame
from render.buttons import Button, ToggleButton
from render.sprite import DirtySprite
from math import ceil
import settings
from utils import CheckJson

class BaseScene():
    def __init__(self,quoridor, json=None, background=None):
            
        self.__sprites = pygame.sprite.LayeredDirty()
        self.__quoridor = quoridor
        self.__display_surface = quoridor.GetDisplaySurface()
        self.__background = None
        self.__sprites.clear(self.__display_surface,self.__background)
        self.__next = False
        self.__cached_surfaces = {}

        self.LoadBackground(background)
        self.LoadBaseJson(json)

    def GetQuoridor(self):
        return self.__quoridor
        
    # Path can also be an id
    def GetSurface(self, path):
        if path in self.__cached_surfaces:
            return self.__cached_surfaces[path]
        else:
            return self.RegisterSurface(path, pygame.image.load(path).convert_alpha())
        
    def RegisterSurface(self,id,surface):
        self.__cached_surfaces[id] = surface
        return surface
    
    def LoadBackground(self,background):
        if isinstance(background,str):
            self.__background = pygame.image.load(background).convert()
        elif self.__background is None:
            self.__background = pygame.surface.Surface(settings.DISPLAY_SIZE)
            self.__background.fill(pygame.Color(255,255,255))
        self.__display_surface.blit(self.__background, (0,0))
        
    def LoadBaseJson(self, json):
        json = CheckJson(json)
        
        if json is None:
            return

        if "background" in json:
            self.LoadBackground(json["background"])
        
        if "toggle-buttons" in json:
            for name, data in json["toggle-buttons"].items():
                self.RegisterButton(ToggleButton, name, data)
        if "buttons" in json:
            for name, data in json["buttons"].items():
                self.RegisterButton(Button, name, data)
        if "sprites" in json:
            for name, data in json["sprites"].items():
                pos = data["pos"]
                size = data["size"]
                x = pos[0]
                y = pos[1]
                surface = pygame.transform.scale(self.GetSurface(data["path"]), (size[0], size[1]))
                sprite = DirtySprite(name, surface, x, y)
                self.RegisterSprite(sprite)
    
    def GetBackGroundSurface(self):
        return self.__background
                
    def RegisterButton(self, clazz, id, data):
        action = None
        pos = data["pos"]
        size = data["size"]
        x = pos[0]
        y = pos[1]
        if "action" in data:
            action = data["action"]
        if clazz == Button:
            surface = pygame.transform.scale(pygame.image.load(data["path"]).convert_alpha(), (size[0], size[1]))
            self.RegisterSprite(Button(self, id, surface, x, y, action))
        elif clazz == ToggleButton:
            surface_untoggled = pygame.transform.scale(pygame.image.load(data["path"]).convert_alpha(), (size[0], size[1]))
            surface_toggled = pygame.transform.scale(pygame.image.load(data["path"].replace(".PNG", "ok.PNG")).convert_alpha(), (size[0], size[1]))
            button = ToggleButton(self, id, surface_untoggled, surface_toggled, x, y, action)
            self.RegisterSprite(button)
            if "toggled" in data and data["toggled"] == True:
                button.Action(button)
    
    def GetDisplaySurface(self):
        return self.__display_surface
    
    def RegisterSprite(self, sprite):
        if isinstance(sprite.GetPos()[0], float):
            sprite.rect.x = ceil(self.__display_surface.get_width() / sprite.GetPos()[0])
            sprite.rect.y = ceil(self.__display_surface.get_height() / sprite.GetPos()[1])
        self.__sprites.add(sprite)
    
    def Render(self, display_surface):
        return self.__sprites.draw(display_surface)
        
    def Update(self):
        self.__sprites.update()
        pass
    
    def ProcessEvents(self, events):
        pass
    
    def Input(self, keys):
        pass
    
    def Terminate(self):
        pass
    
    def MouseDown(self):
        pass
    
    def MouseUp(self):
        buttons = filter(lambda sprite: isinstance(sprite, Button), self.__sprites)
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(mouse_pos) and button.Action:
                button.Action(button)

    def GetMainGroup(self):
        return self.__sprites
    
    def Next(self, nextsene=None):
        if nextsene:
            self.__next = nextsene
        return self.__next
    
    def __str__(self):
        return type(self).__name__