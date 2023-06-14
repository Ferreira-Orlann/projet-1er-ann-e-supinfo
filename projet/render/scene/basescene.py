import pygame
from render.buttons import Button, ToggleButton
from render.sprite import DirtySprite
from math import ceil
import settings
from utils import CheckJson

class BaseScene():
    def __init__(self,quoridor, json=None, background=None):
        self.__sprites = pygame.sprite.LayeredDirty()
        self.__quoridor = quoridor
        self.__display_surface = quoridor.GetDisplaySurface()
        self.__background = None
        self.__next = False
        self.__cached_surfaces = {}
        self.__custom_groups = {}
        self.__custom_groups["default"] = self.__sprites
        
        self.LoadBackground(background)
        self.__sprites.clear(self.__display_surface,self.__background)
        
        json = CheckJson(json)
        self.LoadBaseJson(json)

    def SetJson(self,json):
        self.__json = json

    def GetJson(self):
        return self.__json

    def AddSpriteGroup(self, name):
        print(name)
        self.__custom_groups[name] = pygame.sprite.LayeredDirty()
        self.__custom_groups[name].clear(self.__display_surface,self.__background)
        
    def GetSpriteGroup(self, name):
        if name not in self.__custom_groups.keys(): return False
        return self.__custom_groups[name]

    def GetQuoridor(self):
        """Return the quoridor instance"""
        return self.__quoridor
        
    # Path can also be an id
    def GetSurface(self, path):
        """Return the surface from the path"""
        if path in self.__cached_surfaces:
            return self.__cached_surfaces[path]
        else:
            return self.RegisterSurface(path, pygame.image.load(path).convert_alpha())
        
    def RegisterSurface(self,id,surface):
        """Register a surface"""
        self.__cached_surfaces[id] = surface
        return surface
    
    def LoadBackground(self, background):
        """Load the background"""
        if isinstance(background, str):
            self.__background = self.__quoridor.GetSurfaceManager().GetSurface(background)
        elif self.__background is None:
            self.__background = pygame.surface.Surface(settings.DISPLAY_SIZE)
            self.__background.fill(pygame.Color(0, 255, 255))
        self.__display_surface.blit(self.__background, (0, 0))
        for group in self.__custom_groups.values():
            group.clear(self.__display_surface,self.__background)
        
    def LoadBaseJson(self, json):
        """Load the base json"""
        if json is None:
            return
        if "background" in json:  # Load the background
            self.LoadBackground(json["background"])
        if "toggle-buttons" in json:  # Load the toggle buttons
            for name, data in json["toggle-buttons"].items():
                self.RegisterButton(ToggleButton, name, data)
        if "buttons" in json:   # Load the buttons
            for name, data in json["buttons"].items():
                self.RegisterButton(Button, name, data)
        if "sprites" in json:  # Load the sprites
            for name, data in json["sprites"].items():
                pos = data["pos"]  # Get the position
                size = data["size"]  # Get the size
                x = pos[0]
                y = pos[1]
                surface = pygame.transform.scale(self.GetSurface(data["path"]), (size[0], size[1]))
                sprite = DirtySprite(name, surface, x, y)
                self.RegisterSprite(sprite)  # Register the sprite
        self.SetJson(json)
    
    def GetBackGroundSurface(self):
        """Return the background surface"""
        return self.__background
                
    def RegisterButton(self, clazz, id, data, group=None):
        """Register a button"""
        action = None  # The action of the button
        pos = data["pos"]  # Get the position
        size = data["size"]  # Get the size
        x = pos[0]
        y = pos[1]
        if "action" in data:  # Get the action
            action = data["action"]
        if clazz == Button:
            surface = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"]).convert_alpha(), (size[0], size[1]))
            button = Button(self, id, surface, x, y, action)
            self.RegisterSprite(button, group)
            return button
        elif clazz == ToggleButton:
            surface_untoggled = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"]).convert_alpha(), (size[0], size[1]))
            surface_toggled = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"].replace(".PNG", "ok.PNG")).convert_alpha(), (size[0], size[1]))
            button = ToggleButton(self, id, surface_untoggled, surface_toggled, x, y, action)
            self.RegisterSprite(button,group)
            if "toggled" in data and data["toggled"] == True:
                button.Action(button)
            return button
    
    def GetDisplaySurface(self):
        """Return the display surface"""
        return self.__display_surface
    
    def RegisterSprite(self, sprite, group = None):
        """Register a sprite"""
        if isinstance(sprite.GetPos()[0], float):
            sprite.rect.x = ceil(self.__display_surface.get_width() / sprite.GetPos()[0])
            sprite.rect.y = ceil(self.__display_surface.get_height() / sprite.GetPos()[1])
        if sprite is not None:
            gr = self.GetSpriteGroup(group)
            if gr:
                gr.add(sprite)
                return sprite
        self.__sprites.add(sprite)
        return sprite
    
    def Render(self, display_surface):
        """Render the scene"""
        rects = []
        for group in self.__custom_groups.values():
            rects.extend(group.draw(display_surface))
        return rects
        
    def SpriteHover(self, sprite):
        pass    
    
    def Update(self):
        """Update the scene"""
        groups = self.__custom_groups.values()
        mouse_pos = pygame.mouse.get_pos()
        for group in groups:
            group.update()
            for sprite in group:
                if sprite.rect.collidepoint(mouse_pos):
                    self.SpriteHover(sprite)
    
    def ProcessEvents(self, events):
        pass
    
    def Input(self, keys):
        pass
    
    def InputPressed(self, key):
        pass
    
    def InputReleased(self, key):
        pass
    
    def Terminate(self):
        pass
    
    def MouseDown(self):
        pass
    
    def MouseUp(self):
        """Called when the mouse is up"""
        buttons = filter(lambda sprite: isinstance(sprite, Button), self.__sprites)
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(mouse_pos) and button.Action:
                button.Action(button)

    def GetMainGroup(self):
        """Return the main group"""
        return self.__sprites
    
    def Next(self, nextsene=None):
        """Return the next scene"""
        if nextsene:
            self.__next = nextsene
        return self.__next
    
    def __str__(self):
        """Return the name of the scene"""
        return type(self).__name__