from pygame import quit
from sys import exit

class SceneBase:
    def __init__(self):
        self.__next = self
    
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
        quit()
        exit()