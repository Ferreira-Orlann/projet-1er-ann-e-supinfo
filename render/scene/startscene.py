import pygame
from render.scene.basescene import BaseScene

class StartScene(BaseScene):
    def __init__(self, display_surface):
        super().__init__("./assets/page1/background1.jpg", display_surface)
        self.RegisterSprite(StartButton())
        self.Render()
        pass
    
class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/page1/play.PNG")
        self.rect = self.image.get_rect()
        self.rect.center = (594,600)
        pass
    
    def ProcessEvents(self, events):
        pass