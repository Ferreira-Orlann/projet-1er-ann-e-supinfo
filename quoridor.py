import pygame

class Quoridor():
    MOVE_TYPE_UP = (-1,0)
    MOVE_TYPE_DOWN = (1,0)
    MOVE_TYPE_LEFT = (0,-1)
    MOVE_TYPE_RIGHT = (0,1)
    START_CONFIGS = [(0,4,True,8), (8,4,True,0), (4,0,False,8), (4,8,False,0)]
    
    def __init__(self):
        from scenes.start import SceneStart
        pygame.init()
        self.__active_scene = None
        self.__screen = pygame.display.set_mode(size=(1160, 920))
        self.__active_scene = SceneStart(self.__screen, self)
        self.__active_scene.FirstRender(self.__screen)
        pygame.display.flip()
        
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
            temp = self.__active_scene.Next()
            if temp != self.__active_scene:
                temp.FirstRender(self.__screen)
                pygame.display.flip()
            if self.__active_scene.ShouldRender():
                self.__active_scene.Render(self.__screen)
                self.__active_scene.StopFullRender()
                pygame.display.flip()
            else:
                pygame.display.update(None)
            self.__active_scene = temp
            clock.tick(60)

if __name__ == '__main__':
    QUORIDOR = Quoridor()