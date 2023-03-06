import pygame
from render.buttons import Button, ToggleButton
from render.sprite import DirtySprite
from math import ceil
from json import load as json_load
import settings

class BaseScene():
    def __init__(self, background, display_surface, json=None):
        self.__sprites = pygame.sprite.LayeredDirty()
        self.__display_surface = display_surface
        self.__background = pygame.image.load(background).convert()
        self.__sprites.clear(display_surface,self.__background)
        display_surface.blit(self.__background, (0,0))
        self.__next = False
    
        if json: 
            file = open(json, "r")
            json = json_load(file)
            file.close()
            
            for name, data in json["toggle-buttons"].items():
                self.RegisterButton(ToggleButton, name, data)
            for name, data in json["buttons"].items():
                self.RegisterButton(Button, name, data)
            for name, data in json["sprites"].items():
                pos = data["pos"]
                size = data["size"]
                x = pos[0]
                y = pos[1]
                surface = pygame.transform.scale(pygame.image.load(data["path"]).convert_alpha(), (size[0], size[1]))
                sprite = DirtySprite(name, surface, x, y)
                self.RegisterSprite(sprite)
                
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
                button.Toggle(button)
    
    def GetDisplaySurface(self):
        return self.__display_surface
    
    def RegisterSprite(self, sprite):
        print(sprite.rect.x)
        if isinstance(sprite.GetPos()[0], float):
            sprite.rect.x = ceil(self.__display_surface.get_width() / sprite.GetPos()[0])
            sprite.rect.y = ceil(self.__display_surface.get_height() / sprite.GetPos()[1])
            print("Registering sprite")
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