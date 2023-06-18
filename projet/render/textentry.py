from render.label import Label

class TextEntry(Label):
    def __init__(self, id, surface, x, y, scene, font):
        super().__init__(id, surface, x, y, scene, font)
        self.__is_selected
    
    def SetSelected(self, val):
        self.__is_selected = val
        
    def IsSelected(self):
        return self.__is_selected