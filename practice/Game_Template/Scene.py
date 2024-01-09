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
        self.monsters=pygame.sprite.Group()
        self.map = None
        self.decorates=pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.breakobj=pygame.sprite.Group()

        self.window = window
        self.width = WindowSettings.width
        self.height = WindowSettings.height
        self.battlebox=None
        self.dialogbox=None
        self.shoppingbox=None
        self.cameraX =0
        self.cameraY=0      

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):

        self.dialogbox=None


    def trigger_battle(self, player):

        self.battlebox=BattleBox(self.window,player,player.collidingObject["monster"])
        pygame.event.post(pygame.event.Event(GameEvent.EVENT_BATTLE))
        print("init battle done,battle event done")


    def end_battle(self,player):
        self.battlebox=None
        player.collidingWith['monster']=False
        player.reset_pos()
        


    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):

        self.shoppingbox=None


    
    def get_width(self):
        return WindowSettings.width * WindowSettings.outdoorScale

    def get_height(self):
        return WindowSettings.height * WindowSettings.outdoorScale

    def update_camera(self, player):

            if player.rect.x > WindowSettings.width //2+ 10:
                self.cameraX += player.speed

                if self.cameraX < self.get_width() - WindowSettings.width:
                    player.fix_to_middle(player.speed, 0)
                else:
                    self.cameraX = self.get_width() - WindowSettings.width
                    
            elif player.rect.x < WindowSettings.width//2-10:
                self.cameraX -= player.speed
                if self.cameraX > 0:
                    player.fix_to_middle(-player.speed, 0)
                else:
                    self.cameraX = 0
            if player.rect.y > WindowSettings.height //2+10:
                self.cameraY += player.speed
                if self.cameraY < self.get_height() - WindowSettings.height:
                    player.fix_to_middle(0, player.speed)
                else:
                    self.cameraY = self.get_height() - WindowSettings.height
            elif player.rect.y < WindowSettings.height //2-10:
                self.cameraY -= player.speed
                if self.cameraY > 0:
                    player.fix_to_middle(0, -player.speed)
                else:
                    self.cameraY = 0



    def render(self, player:Player):
        self.update_camera(player)

        if self.type==SceneType.WILD:

            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    self.window.blit(self.map[i][j], 
                                    (SceneSettings.tileWidth * i- self.cameraX, SceneSettings.tileHeight * j- self.cameraY))
            for obs in self.obstacles.sprites():
                obs.draw(self.window,self.cameraX,self.cameraY)
            for dec in self.decorates.sprites():             
                dec.draw(self.window,self.cameraX,self.cameraY)
            for mon in self.monsters.sprites(): 
                mon.draw(self.window,self.cameraX,self.cameraY)
            for bra in self.breakobj.sprites(): 
                bra.draw(self.window,self.cameraX,self.cameraY)

            if player.is_colliding():
                player.draw(self.window,player.dx,player.dy)
            if self.battlebox!=None:
                self.battlebox.Update_card()
                #print("render in scene")
            else:
                player.draw(self.window,0,0)
            keys=pygame.key.get_pressed()
            if player.is_colliding_bra() and keys[pygame.K_0]:
                for bra in player.collidingObject["bra"]:
                    self.breakobj.remove(bra)

class StartMenu:
    def __init__(self, window):
        self.index=0
        self.type=SceneType.MENU
        self.images=[ pygame.transform.scale(pygame.image.load(img) ,
                     (WindowSettings.width,550)) for img in GamePath.menu]
        self.startimg=pygame.transform.scale(pygame.image.load(GamePath.dialog) ,(300,50)) 
        self.image=self.images[self.index]
        self.window=window
        self.start_rect=self.startimg.get_rect()
        self.wordcenter=(WindowSettings.width // 2 , (WindowSettings.height ) // 2+100)
        #self.start_rect.center=self.wordcenter

        self.textsize=40
        self.textsize2=30
        self.position3=(350,620)

        font0=pygame.font.SysFont("impact", self.textsize)
        self.text = font0.render("START",True,(20,0,0))
        self.text_rect=self.text.get_rect()
        #self.text_rect.center=self.wordcenter

        font1=pygame.font.SysFont("inkfree", self.textsize2)
        self.text2=font1.render("If you don't risk anything, you risk even more",True,(150,150,150))
    def selectanimate(self,size=1):
        self.text=pygame.font.SysFont("impact", int(self.textsize*size)).render("START",True,(20,0,0))
        self.startimg=pygame.transform.scale(pygame.image.load(GamePath.dialog) ,(300*size,50*size)) 
        self.start_rect=self.startimg.get_rect()
        self.text_rect=self.text.get_rect()
        self.start_rect.center=self.wordcenter
        self.text_rect.center=self.wordcenter
    def update_menu(self):
        if self.index<94*4:
            self.index+=1
        else:
            self.index=0
        self.image=self.images[self.index//4]
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] >= self.start_rect.x and mousepos[0]<self.start_rect.x+300 and mousepos[1] >self.start_rect.y  and mousepos[1]<self.start_rect.y+50  :
            self.selectanimate(1.3)
            if pygame.mouse.get_pressed()[0]:
                pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH))
                self.selectanimate(1)               
        else:
            self.selectanimate(1)


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
        self.obstacles,self.decorates,self.breakobj=Maps.gen_wild_obstacle()
        self.map=Maps.gen_wild_map()
        self.monsters.add(Monster(200, 80,1,100,2,10))

    def gen_WILD(self):
        pass
        #PortalSettings

    def gen_monsters(self, num = 10):
        self.monsters.add(Monster(600,600,100,5,10))

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

