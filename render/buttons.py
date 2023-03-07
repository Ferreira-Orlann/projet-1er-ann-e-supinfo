from render.sprite import DirtySprite

class Button(DirtySprite):
    def __init__(self, scene, id, surface, x, y, action=None):
        super().__init__(id, surface, x, y)
        if callable(action):
            self.Action = action
        elif hasattr(scene, id):
            if action == None:
                self.Action = getattr(scene, id)
            else:
                self.Action = getattr(scene,action)
        else:
            self.Action = getattr(scene,action)
        self.dirty = 1
        pass

class ToggleButton(Button):
    def __init__(self, scene, id, surfaceone, surfacetwo, x, y, action=None):
        super().__init__(scene, id, surfaceone, x, y, self.Toggle)
        self.__surfaceone = surfaceone
        self.__surfacetwo = surfacetwo
        if action:
            self.ToggleAction = getattr(scene, action)
        else:
            self.ToggleAction = getattr(scene, id)
        self.__toggled = False
        
    def Toggle(self, this=None):
        self.ToggleAction(self, self.__toggled)
        if self.__toggled:
            self.ChangeSurface(self.__surfaceone)
        else:
            self.ChangeSurface(self.__surfacetwo)
            print("Changed surface")
        self.__toggled = not self.__toggled
        
    def IsToggled(self):
        return self.__toggled