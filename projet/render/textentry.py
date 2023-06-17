from render.label import Label

class TextEntry(Label):
    def __init__(self, id, surface, x, y, scene, font, action):
        super().__init__(id, surface, x, y, scene, font)
        if callable(action):
            self.Action = action
        elif (isinstance(id, str) and hasattr(scene, id)) or hasattr(scene, action):
            if action == None:
                self.Action = getattr(scene, id)
            else:
                self.Action = getattr(scene,action)
        else:
            self.Action = getattr(scene,action)