import pygame

class BaseScene():
    def __init__(self, background,display_surface):
        self.__sprites = pygame.sprite.Group()
        self.__display_surface = display_surface
        self.__background = pygame.image.load(background).convert_alpha()
    
    def GetDisplaySurface(self):
        return self.__display_surface
    
    def RegisterSprite(self, sprite):
        self.__sprites.add(sprite)
    
    def Render(self):
        display_surface = self.__display_surface
        # temp_surface = pygame.surface.Surface()
        display_surface.blit(self.__background, (0,0))
        self.__sprites.draw(display_surface)
        
    def Update(self):
        self.__sprites.update()
        pass
    
    def ProcessEvents(self, events):
        pass
    
    def Input(self, keys):
        pass
    
    def Terminate(self):
        pass