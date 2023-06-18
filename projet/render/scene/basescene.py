import pygame
from render.buttons import Button, ToggleButton
from render.sprite import DirtySprite
from math import ceil
import settings
from utils import CheckJson
from render.textentry import TextEntry

class BaseScene():
    def __init__(self,quoridor, json=None, background=None):
        self.__quoridor = quoridor
        if (quoridor.GetActiveScene() is not None):
            quoridor.GetSurfaceManager().Clear()
        self.__sprites = pygame.sprite.LayeredDirty(layer=1)
        self.__display_surface = quoridor.GetDisplaySurface()
        self.__background = None
        self.__next = False
        self.__cached_surfaces = {}
        self.__custom_groups = {}
        self.__custom_groups["default"] = self.__sprites
        self.AddSpriteGroup("text_entries")
        
        self.LoadBackground(background)
        self.__sprites.clear(self.__display_surface,self.__background)
        
        json = CheckJson(json)
        self.LoadBaseJson(json)
        
    def GetSpriteById(self, id, group = "default"):
        g = self.GetSpriteGroup(group)
        for sprite in g:
            if (sprite.GetId() == id):
                return sprite
        return None

    def GetSpritesById(self, ids, group = "default"):
        returnList = []
        g = self.GetSpriteGroup(group)
        for sprite in g:
            if (sprite.GetId() in ids):
                returnList.append(sprite)
        return returnList

    def SetJson(self,json):
        self.__json = json

    def GetJson(self):
        return self.__json
    
    def GetNameByGroup(self,search_group):
        for name, group in self.__custom_groups.items():
            if (group == search_group):
                return name
        return None

    def AddSpriteGroup(self, name):
        self.__custom_groups[name] = pygame.sprite.LayeredDirty(layer=len(self.__custom_groups)+1)
        self.__custom_groups[name].clear(self.__display_surface,self.__background)
        return self.__custom_groups[name]
        
    def GetSpriteGroup(self, name):
        return self.__custom_groups.get(name)

    def GetQuoridor(self):
        return self.__quoridor
        
    def GetSurface(self, path):
        if path in self.__cached_surfaces:
            return self.__cached_surfaces[path]
        else:
            return self.RegisterSurface(path, pygame.image.load(path).convert_alpha())
        
    def RegisterSurface(self,id,surface):
        self.__cached_surfaces[id] = surface
        return surface
    
    def LoadBackground(self, background):
        if isinstance(background, str):
            self.__background = self.__quoridor.GetSurfaceManager().GetSurface(background)
        elif self.__background is None:
            self.__background = pygame.surface.Surface(settings.DISPLAY_SIZE)
            self.__background.fill(pygame.Color(0, 255, 255))
        self.__background = pygame.transform.scale(self.__background, settings.DISPLAY_SIZE)
        self.__display_surface.blit(self.__background, (0, 0))
        for group in self.__custom_groups.values():
            group.clear(self.__display_surface,self.__background)
        
    def LoadBaseJson(self, json):
        if json is None:
            return
        if "background" in json:
            self.LoadBackground(json["background"])
        if "toggle-buttons" in json:
            for name, data in json["toggle-buttons"].items():
                self.RegisterButton(ToggleButton, name, data)
        if "buttons" in json:
            for name, data in json["buttons"].items():
                self.RegisterButton(Button, name, data)
        if "sprites" in json:
            for name, data in json["sprites"].items():
                pos = data["pos"]
                size = data["size"]
                x = pos[0]
                y = pos[1]
                surface = pygame.transform.scale(self.GetSurface(data["path"]), (size[0], size[1]))
                sprite = DirtySprite(name, surface, x, y, self)
                self.RegisterSprite(sprite)
        if "textentries" in json:
            for name, data in json["textentries"].items():
                pos = data["pos"]
                tentry = TextEntry(name, pos[0], pos[1], self, self.__quoridor.GetFontManager().GetFont("default"))
                tentry.SetText(data["text"])
                tentry.SetMaxSize(data["maxchar"])
                self.RegisterSprite(tentry)
        self.SetJson(json)
    
    def GetBackGroundSurface(self):
        return self.__background
                
    def RegisterButton(self, clazz, id, data, group=None):
        action = None
        pos = data["pos"]
        size = data["size"]
        x = pos[0]
        y = pos[1]
        if "action" in data:
            action = data["action"]
        if clazz == Button:
            surface = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"]), (size[0], size[1]))
            button = Button(self, id, surface, x, y, action)
            self.RegisterSprite(button, group)
            return button
        elif clazz == ToggleButton:
            surface_untoggled = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"]), (size[0], size[1]))
            surface_toggled = pygame.transform.scale(self.__quoridor.GetSurfaceManager().GetSurface(data["path"].replace(".PNG", "ok.PNG")), (size[0], size[1]))
            button = ToggleButton(self, id, surface_untoggled, surface_toggled, x, y, action)
            self.RegisterSprite(button, group)
            if "toggled" in data and data["toggled"] == True:
                button.Action(button)
            return button
    
    def GetDisplaySurface(self):
        return self.__display_surface
    
    def RegisterSprite(self, sprite, group = None, bypass = False):
        if isinstance(sprite.GetPos()[0], float):
            sprite.rect.x = ceil(self.__display_surface.get_width() / sprite.GetPos()[0])
            sprite.rect.y = ceil(self.__display_surface.get_height() / sprite.GetPos()[1])
        if (isinstance(sprite, TextEntry)):
            self.GetSpriteGroup("text_entries").add(sprite)
        gr = self.GetSpriteGroup(group)
        if gr is not None:
            gr.add(sprite)
        if (not bypass):
            self.__sprites.add(sprite)
        return sprite
    
    def Render(self, display_surface):
        rects = []
        rects.extend(self.__sprites.draw(display_surface))
        return rects
        
    def SpriteHover(self, sprite):
        pass    
    
    def InternalUpdate(self):
        mouse_pos = pygame.mouse.get_pos ()
        for group in self.__custom_groups.values():
            group.update()
            for sprite in group:
                if sprite.rect.collidepoint(mouse_pos):
                    self.SpriteHover(sprite)
                    
    def Update(self): ...
    
    def ProcessEvents(self, events):
        pass
    
    def Inputs(self, keys):
        pass
    
    def InternalInputPressed(self, event):
        for textentry in self.GetSpriteGroup("text_entries"):
            if (textentry.IsSelected()):
                text = textentry.GetText()
                if (event.key == pygame.K_BACKSPACE):
                    text = text[:-1]
                elif (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN) :
                    textentry.SetSelected(False)
                    continue
                else:
                    text += event.unicode
                textentry.SetText(text)
                
    def InputPressed(self, event):
        pass
    
    def InputReleased(self, event):
        pass
    
    def MouseDown(self):
        pass
    
    def MouseUp(self):
        buttons = []
        mouse_pos = pygame.mouse.get_pos()
        for group in self.__custom_groups.values():
            for sprite in group:
                if (isinstance(sprite, Button)):
                    if sprite.rect.collidepoint(mouse_pos) and sprite.Action:
                        sprite.Action(sprite)
                if (isinstance(sprite, TextEntry)):
                    if sprite.rect.collidepoint(mouse_pos) and sprite.Action:
                        sprite.SetSelected(True)
                

    def GetMainGroup(self):
        return self.__sprites
    
    def Next(self, nextsene=None):
        if nextsene:
            self.__next = nextsene
        return self.__next
    
    def __str__(self):
        return type(self).__name__