import pygame

class Quoridor():
    def __init__(self):
        from scenes.start import SceneStart
        pygame.init()
        self.__active_scene = None
        self.__screen = pygame.display.set_mode(size=(1160, 920))
        self.__active_scene = SceneStart(self.__screen, self)
        
        conf = list()
        conf.append(2)
        conf.append(5)
        conf.append(4)
        self.__config = conf
        
        self.Run()
        pass
    
    def Run(self):
        while self.__active_scene != None:
            pressed_keys = pygame.key.get_pressed()
            filtered_events = []
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__active_scene.Terminate()
                filtered_events.append(event)
                pass
            
            self.__active_scene.ProcessInput(filtered_events, pressed_keys, self.__screen)
            self.__active_scene.Update()
            self.__active_scene.Render(self.__screen)
            self.__active_scene = self.__active_scene.Next()
            pygame.display.flip()
            
    def GetConfig(self):
        # 0 : Nombre de joueurs
        # 1: Taille du plateau
        # 2: Nombre de barrières
        return self.__config

if __name__ == '__main__':
    QUORIDOR = Quoridor()