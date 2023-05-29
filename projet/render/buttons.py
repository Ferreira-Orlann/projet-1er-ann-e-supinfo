from render.sprite import DirtySprite

class Button(DirtySprite):
    def __init__(self, scene, id, surface, x, y, action=None):
        super().__init__(id, surface, x, y)
        if callable(action):
            self.Action = action
        elif (isinstance(id, str) and hasattr(scene, id)) or hasattr(scene, action):
            if action == None:
                self.Action = getattr(scene, id)
            else:
                self.Action = getattr(scene,action)
        else:
            self.Action = getattr(scene,action)
        self.dirty = 1
    
    def DefineData(self, data):
        self.__data = data
        
    def GetData(self):
        return self.__data

class ToggleButton(Button):
    def __init__(self, scene, id, surfaceone, surfacetwo, x, y, action=None):
        super().__init__(scene, id, surfaceone, x, y, action)
        self.__surfaceone = surfaceone
        self.__surfacetwo = surfacetwo
        self.__toggled = False
        
    def Toggle(self, this=None):
        """Toggle the button"""
        if self.__toggled:
            self.ChangeSurface(self.__surfaceone)
        else:
            self.ChangeSurface(self.__surfacetwo)
        self.__toggled = not self.__toggled
        
    def IsToggled(self):
        """Return if the button is toggled"""
        return self.__toggled
