from pygame.time import get_ticks
from pygame.image import load
from rich import print_json

class SurfaceManager():
    def __init__(self):
        self.__data = {}
        self.__last_tick = get_ticks()
        
    def RegisterSurface(self, path, surface, numberOfUse):
        self.__data[path] = [surface, 3, numberOfUse]
        
    def AddSurface(self, path):
        if path in self.__data.keys():
            data = self.__data[path]
            data[2] += 1
            data[1] = 3
            self.__data[path] = data
            
    def RemoveSurface(self, path):
        if path in self.__data.keys():
            nb = self.__data[path][2]
            nb -= 1
            if (nb <= 0):
                self.__data.pop(path)
                return
            self.__data[path][2] = nb
        
    def GetPath(self, surface):
        for path, data in self.__data.items():
            if (data[0] == surface):
                return path
        return None
            
    def GetSurface(self, path):
        if path in self.__data.keys():
            data = self.__data[path]
            data[2] += 1
            return data[0]
        surface = load(path).convert_alpha()
        self.RegisterSurface(path, surface, 1)
        return surface
        
    def Update(self):
        ticks = get_ticks()
        if (not (ticks - self.__last_tick) > 1000): return
        self.__last_tick = ticks
        for path, data in list(self.__data.items()):
            if (data[2] > 0): continue
            nb = data[1]
            nb -= 1
            if nb == 0:
                self.__data.pop(path)