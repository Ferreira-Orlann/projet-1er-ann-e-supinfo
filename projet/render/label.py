from render.sprite import DirtySprite

class Label(DirtySprite):
    def __init__(self, id, x, y, scene, font):
        self.__font = font
        self.__text = ""
        self.__antialias = True
        self.__color = (0,0,0)
        super().__init__(id, self.__font.render(self.__text, self.__antialias, self.__color), x, y, scene)
        
    def GetAntialias(self):
        return self.__antialias
    
    def SetAntialias(self, alias):
        self.__antialias = alias
        
    def GetColor(self):
        return self.__color
    
    def SetColor(self, color, update = True):
        self.__color = color
        if (update):
            self.UpdateSurface()
        
    def GetFont(self):
        return self.__font
    
    def SetFont(self, font):
        self.__font = font
    
    def SetText(self, text):
        self.__text = text
        self.UpdateSurface()
        
    def GetText(self):
        return self.__text
    
    def UpdateSurface(self):
        surface = self.__font.render(self.__text, self.__antialias, self.__color)
        self.ChangeSurface(surface)