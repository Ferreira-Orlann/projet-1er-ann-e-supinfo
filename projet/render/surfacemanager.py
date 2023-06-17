from pygame.time import get_ticks
from pygame.image import load

class SurfaceManager():
    def __init__(self):
        self.__data = {}
        self.__last_tick = get_ticks()
        
    def RegisterSurface(self, path, surface):
        self.__data[path] = surface
        
    def GetPath(self, surface):
        for path, data in self.__data.items():
            if (data == surface):
                return path
        return None
    
    def GetPaths(self, surfaces):
        paths = []
        for path, data in self.__data.items():
            if (data in surfaces):
                paths.append(path)
        return paths
    
    def Clear(self):
        self.__data = {}
        
    def GetSurface(self, path):
        if path in self.__data.keys():
            return self.__data[path]
        surface = load(path).convert_alpha()
        self.RegisterSurface(path, surface)
        return surface