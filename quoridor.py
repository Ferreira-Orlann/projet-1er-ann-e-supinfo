import pygame

class Quoridor():
    MOVE_TYPE_UP = (1,0)
    MOVE_TYPE_DOWN = (-1,0)
    MOVE_TYPE_LEFT = (0,-1)
    MOVE_TYPE_RIGHT = (0,1)
    
    def __init__(self):
        from scenes.start import SceneStart
        pygame.init()
        self.__active_scene = None
        self.__screen = pygame.display.set_mode(size=(1160, 920))
        self.__active_scene = SceneStart(self.__screen, self)
        
        self.Run()
        pass
    
    def Run(self):
        clock = pygame.time.Clock()  
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
            clock.tick(60)

if __name__ == '__main__':
    QUORIDOR = Quoridor()