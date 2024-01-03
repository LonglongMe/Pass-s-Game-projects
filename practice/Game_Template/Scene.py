# -*- coding:utf-8 -*-

import pygame
import Maps
from random import randint

from enum import Enum
from Settings import *
from NPCs import *
from PopUpBox import *
from Portal import *
from BgmPlayer import *

class Scene():
    def __init__(self, window):
        self.type = None

        self.map = None
        self.decorates=pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()

        self.window = window
        self.width = WindowSettings.width
        self.height = WindowSettings.height

        

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_battle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_camera(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render(self, player):
      
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], 
                                 (SceneSettings.tileWidth * i, 
                                SceneSettings.tileHeight * j))
                
        self.obstacles.draw(self.window)
        self.decorat
        self.npcs.draw(self.window)
        self.portals.draw(self.window)


class StartMenu():
    def __init__(self, window):
        self.type=SceneType.MENU
        self.image=self.image = pygame.transform.scale(pygame.image.load(GamePath.menu) , (WindowSettings.width,WindowSettings.height))
        self.window=window
        self.font = pygame.font.Font(None, 40)
        self.botton = pygame.Surface((300, 50), pygame.SRCALPHA)
        self.botton.fill(self.content_color)
        button_width = 300
        button_height = 50
        self.button_x = (WindowSettings.width - button_width) // 2
        self.button_y = (WindowSettings.height - button_height) // 2
        self.position=(self.button_x,self.button_y,button_width,button_height)


    def render(self, time):
        pygame.draw.rect(self.window,(255,255,255), self.position,0,border_radius=9 )
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] >= self.button_x and mousepos[0]<self.button_x+300 and mousepos[1] >self.button_y  and mousepos[1]<self.button_y+50  and pygame.mouse.get_pressed()[0] :
            pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH))


class HomeScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_Home(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_WILD(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_monsters(self, num = 10):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Overwrite Scene's function
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_BOSS(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
