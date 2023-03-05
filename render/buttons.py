from render.sprite import DirtySprite

class Button(DirtySprite):
    def __init__(self, scene, id, surface, x, y, action=None):
        super().__init__(id, surface, x, y)
        if hasattr(scene, id) and action == None:
            self.Action = getattr(scene, id)
        else:
            self.Action = action
        self.dirty = 1
        pass
    
    def GetId(self):
        return

class ToggleButton(Button):
    def __init__(self, scene, id, surfaceone, surfacetwo, x, y, action=None):
        super().__init__(scene, id, surfaceone, x, y, self.Toggle)
        if action:
            self.ToggleAction = action
        else:
            self.ToggleAction = getattr(scene, id)
        self.__toggled = False
        
    def Toggle(self, this):
        self.__toggled = not self.__toggled
        self.ToggleAction(self, self.__toggled)
        pass