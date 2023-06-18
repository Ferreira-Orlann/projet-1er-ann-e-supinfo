from render.label import Label

class TextEntry(Label):
    def __init__(self, id, x, y, scene, font):
        super().__init__(id, x, y, scene, font)
        self.__is_selected
        self.__max_size = None
        
    def SetText(self, text):
        if (len(self.GetText()) >= self.__max_size): return
        super().SetText(text)
    
    def SetMaxSize(self, val)
        self.__max_size = val
    
    def GetMaxSize(self):
        return self.__max_size
    
    def SetSelected(self, val):
        self.__is_selected = val
        
    def IsSelected(self):
        return self.__is_selected