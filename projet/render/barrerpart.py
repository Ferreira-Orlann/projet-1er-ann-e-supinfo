from pygame import Rect

class BarrerPart(Rect):
    def __init__(self, left, top, width, height):
        Rect.__init__(self, left, top, width, height)
        self.__id = None
        self.__vertical = False
        self.__posed = False
    
    def SetVertical(self, vertical):
        """Set if the barrer part is vertical or not"""
        self.__vertical = vertical
        return self
    
    def IsVertical(self):
        """Return if the barrer part is vertical or not"""
        return self.__vertical
    
    def GetId(self):
        """Return the id of the barrer part"""
        return self.__id
    
    def SetId(self, id):
        """Set the id of the barrer part"""
        self.__id = id
        
    def IsPosed(self):
        """Return if the barrer part is posed or not"""
        return self.__posed
    
    def SetPosed(self, val):
        """Set if the barrer part is posed or not"""
        self.__posed = val
        
    def SetPos(self, val):
        """Set the position of the barrer part"""
        self.__pos = val
        return self
    
    def GetPos(self):
        """Return the position of the barrer part"""
        return self.__pos
