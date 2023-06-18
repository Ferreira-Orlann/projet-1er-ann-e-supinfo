from pygame.sprite import DirtySprite

class DirtySprite(DirtySprite):
    def __init__(self, id, surface, x, y, scene):
        super().__init__()
        self.__id = id
        self.__scene = scene
        self.rect = None
        self.ChangeSurface(surface, x, y)
        
    def GetPos(self):
        return self.__pos
    
    def SetPos(self, pos):
        self.__pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dirty = 1
        self.rect.update(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        self.__scene.GetQuoridor().AddRedrawRect(self.rect.copy())
        
    def ChangeSurface(self, surface, x=None, y=None):
        if x == None and y == None:
            x = self.rect.x
            y = self.rect.y
        if (self.rect is not None):
            self.__scene.GetQuoridor().AddRedrawRect(self.rect.copy())
        self.image = surface
        self.rect = surface.get_rect()
        self.SetPos((x,y))
        
    def GetId(self):
        return self.__id
