import pygame
from render.scene.basescene import BaseScene
from render.scene.configscene import ConfigScene

class StartScene(BaseScene):
    def __init__(self, display_surface):
        super().__init__("./assets/page1/background1.jpg", display_surface)
        self.RegisterSprite(StartButton())
        pass
    
    def MouseDown(self):
        if self.GetMainGroup().sprites()[0].rect.collidepoint(pygame.mouse.get_pos()):
            self.Next(ConfigScene(self.GetDisplaySurface()))
        pass
    
class StartButton(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/page1/play.PNG")
        self.rect = self.image.get_rect()
        self.rect.center = (594,600)
        self.dirty = 1
        pass