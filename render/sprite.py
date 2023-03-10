from pygame.sprite import DirtySprite

class DirtySprite(DirtySprite):
    def __init__(self, id, surface, x, y):
        super().__init__()
        self.__id = id
        self.ChangeSurface(surface, x, y)
        
    def GetPos(self):
        return self.__pos
    
    def ChangeSurface(self, surface, x=None, y=None):
        if x == None and y == None:
            x = self.rect.x
            y = self.rect.y
        self.image = surface
        self.rect = surface.get_rect()
        self.__pos = (x,y)
        self.rect.x = x
        self.rect.y = y
        self.dirty = 1
        self.rect.update(self.rect.left, self.rect.top, self.rect.width + 10, self.rect.height + 10)
        
    def GetId(self):
        return self.__id