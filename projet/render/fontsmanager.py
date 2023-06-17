from pygame.font import Font

class FontManager():
    def __init__(self, json):
        self.__data = {}
        for name, data in json["fonts"].items():
            self.__data[name] = Font(data[0], data[1])
            
    def GetFont(self, name):
        return self.__data.get(name)