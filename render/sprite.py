from pygame.sprite import DirtySprite
from math import ceil

class DirtySprite(DirtySprite):
    def __init__(self, id, surface, x, y):
        super().__init__()
        self.id = id
        self.image = surface
        self.rect = surface.get_rect()
        self.__pos = (x,y)
        self.rect.x = x
        self.rect.y = y
        
    def GetPos(self):
        return self.__pos