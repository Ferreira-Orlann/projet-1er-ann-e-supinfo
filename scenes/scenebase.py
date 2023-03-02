from pygame import display
from sys import exit

class SceneBase:
    def __init__(self, screen):
        self.__next = self
        self.__screen = screen
        self.__full_render = False
    
    def GetScreen(self):
        return self.__screen
    
    def ProcessInput(self, events, keys):
        pass
        
    def Update(self):
        pass

    def Render(self, screen):
        pass

    def SwitchToScene(self, next_scene):
        self.__next = next_scene
        
    def Quit(self):
        self.SwitchToScene(None)
        
    def Next(self):
        return self.__next
    
    def Terminate(self):
        print("Exit & Quit")
        exit()
    
    def FirstRender(self, scene):
        pass
    
    def NextFullRender(self):
        self.__full_render = True
        
    def StopFullRender(self):
        self.__full_render = False
        
    def ShouldRender(self):
        return self.__full_render