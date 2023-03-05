import pygame
from render.buttons import Button, ToggleButton

class BaseScene():
    def __init__(self, background, display_surface, json=None):
        self.__sprites = pygame.sprite.LayeredDirty()
        self.__display_surface = display_surface
        self.__background = pygame.image.load(background).convert()
        self.__sprites.clear(display_surface,self.__background)
        display_surface.blit(self.__background, (0,0))
        self.__next = False
    
        if json: 
            for name, data in json["toggle-buttons"].items():
                self.RegisterButton(ToggleButton, name, data)
            for name, data in json["buttons"].items():
                self.RegisterButton(Button, name, data)
            for name, data in json["sprites"].items():
                sprite = pygame.sprite.Sprite()
                sprite.image = pygame.transform.scale(pygame.image.load(data[0]).convert_alpha(), (data[1], data[2]))
                sprite.rect = sprite
                self.RegisterSprite(Button, name, da)
                
    def RegisterButton(self, clazz, id, data):
        action = None
        if data[3]:
            action = data[3]
        if clazz == Button:
            surface = pygame.transform.scale(pygame.image.load(data[0]).convert_alpha(), (data[1], data[2]))
            self.RegisterSprite(Button(self, id, surface, action))
            pass
        elif clazz == ToggleButton:
            surface_untoggled = pygame.transform.scale(pygame.image.load(data[0]).convert_alpha(), (data[1], data[2]))
            surface_toggled = pygame.transform.scale(pygame.image.load(data[0].replace(".PNG", "ok.PNG")).convert_alpha(), (data[1], data[2]))
            self.RegisterSprite(ToggleButton(self, id, surface_untoggled, surface_toggled, action))
    
    def GetDisplaySurface(self):
        return self.__display_surface
    
    def RegisterSprite(self, sprite):
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
                button.Action()

    def GetMainGroup(self):
        return self.__sprites
    
    def Next(self, nextsene=None):
        if nextsene:
            self.__next = nextsene
        return self.__next