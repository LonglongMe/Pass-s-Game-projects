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
from Player import *
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
        self.battlebox=None
        self.dialogbox=None
        self.shoppingbox=None

        

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):

        self.dialogbox=None


    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_battle(self):
        self.battlebox=None


    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):

        self.shoppingbox=None

    def update_camera(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render(self, player:Player):
        if self.type==SceneType.WILD:
            #self.WildScene.gen_WILD()
            #WildScene.gen_WILD(self)
            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    self.window.blit(self.map[i][j], 
                                    (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
            self.obstacles.draw(self.window)         
            self.decorates.draw(self.window)
            if player.is_colliding():
                player.draw(self.window,player.dx,player.dy)
            else:
                player.draw(self.window,0,0)
             
        #print("rendering in scene")



class StartMenu:
    def __init__(self, window):
        self.index=0
        self.type=SceneType.MENU
        self.images=[ pygame.transform.scale(pygame.image.load(img) ,
                     (WindowSettings.width,550)) for img in GamePath.menu]
        self.image=self.images[self.index]
        self.window=window
        self.button_width = 300
        self.button_height = 50
        self.button_x =0
        self.button_y =0
        self.position1=None
        self.text_x=0
        self.text_y=0
        self.position2=None
        self.textsize=40
        self.textsize2=30
        self.position3=(350,620)
        self.text = None
        self.text2=None
        c=pygame.font.SysFont("inkfree", self.textsize2)
        self.text2=c.render("If you don't risk anything, you risk even more",True,(150,150,150))
    def selectanimate(self,size=1):
        self.button_width = 300*size
        self.button_height = 50*size
        self.button_x = (WindowSettings.width - self.button_width) // 2 -15
        self.button_y = (WindowSettings.height - self.button_height) // 2+100
        self.position1=(self.button_x,self.button_y,self.button_width,self.button_height)
        self.text_x=(self.button_x+93*size)    
        if size==1:
            self.text_y=(self.button_y+1)
        else:
            self.text_y=(self.button_y-3)
        self.position2=(self.text_x,self.text_y)

        self.textsize=int(40*size**2)
        b=pygame.font.SysFont("impact", self.textsize)

        self.text = b.render("START",True,(20,0,0))
    def update_menu(self):
        if self.scene.index<94*4:
            self.scene.index+=1
        else:
            self.scene.index=0
        self.scene.image=self.scene.images[self.scene.index//4]
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] >= self.scene.button_x and mousepos[0]<self.scene.button_x+300 and mousepos[1] >self.scene.button_y  and mousepos[1]<self.scene.button_y+50  :
            self.scene.selectanimate(1.1)
            if pygame.mouse.get_pressed()[0]:
                pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH))
                self.scene.selectanimate(1)               
        else:
            self.scene.selectanimate(1)
        return self.scene.position1,self.scene.position2

    def gen_menu(self, time):
        pygame.draw.rect(self.window,(255,255,255), self.position,0,border_radius=9 )
        if self.index<94:
            self.index+=1
        else:
            self.index=0
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
        self.type=SceneType.WILD
        self.obstacles,self.decorates=Maps.gen_wild_obstacle()
        self.map=Maps.gen_wild_map()

    def gen_WILD(self):
        pass
        #PortalSettings

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

