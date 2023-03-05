from pygame.sprite import DirtySprite

class Button(DirtySprite):
    def __init__(self, scene, id, surface, action=None):
        super().__init__()
        self.id = id
        if hasattr(scene, id) and action == None:
            self.Action = getattr(scene, id)
        else:
            self.Action = action
        self.image = surface
        self.rect = surface.get_rect()
        self.rect.center = (0,0)
        self.dirty = 1
        pass
    
    def GetId(self):
        return

class ToggleButton(Button):
    def __init__(self, scene, id, surfaceone, surfacetwo, action=None):
        super().__init__(scene, id, surfaceone, self.Toggle)
        if action:
            self.ToggleAction = action
        else:
            self.ToggleAction = getattr(scene, id)
        self.__toggled = False
        
    def Toggle(self):
        self.__toggled = not self.__toggled
        self.ToggleAction(self.__toggled)
        pass