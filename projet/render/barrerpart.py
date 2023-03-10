from pygame import Rect

class BarrerPart(Rect):
    def __init__(self, left, top, width, height):
        Rect.__init__(self, left, top, width, height)
        self.__id = None
        self.__vertical = False
        self.__posed = False
    
    def SetVertical(self, vertical):
        self.__vertical = vertical
        return self
    
    def IsVertical(self):
        return self.__vertical
    
    def GetId(self):
        return self.__id
    
    def SetId(self, id):
        self.__id = id
        
    def IsPosed(self):
        return self.__posed
    
    def SetPosed(self,val):
        self.__posed = val
        
    def SetPos(self,val):
        self.__pos = val
        return self
    
    def GetPos(self):
        return self.__pos