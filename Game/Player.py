# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *
import random
from NPCs import Animal

class Player(pygame.sprite.Sprite, Collidable):
    
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth+10, PlayerSettings.playerHeight+10)) for img in GamePath.player]
        self.index = 0
        self.hadbattle=1
        self.animal=pygame.sprite.Group()
        self.image = self.images[self.index]
        self.battle=False
        self.dialog=False
        self.shopping=False
        self.rect = self.image.get_rect()
        self.rect.width=13
        self.rect.height=13
        self.rect.topleft = (x,y)
        self.next_rect=self.rect
        self.speed = PlayerSettings.playerSpeed
        self.talking = False
        self.dx=0
        self.dy=0
        self.OriginHP = PlayerSettings.playerHP
        self.HP=self.OriginHP
        self.egg=0
        self.ATK = PlayerSettings.playerAttack
        self.defence = PlayerSettings.playerDefence
        self.readytoplay=0
        self.cameraX=0
        self.cameraY=0
        self.money=1000
        self.price1=50
        self.price2=50
        self.price3=30


    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self):
        if self.collidingWith["monster"]==True:
            postionlist=[[-140,80],[0,-80],[-40,-80],[-120,80],[120,0],[10,-180],[0,-80]]
            self.rect.x=self.collidingObject["monster"].rect.x+postionlist[self.collidingObject["monster"].order-1][0]
            self.rect.y=self.collidingObject["monster"].rect.y+postionlist[self.collidingObject["monster"].order-1][1]
        if self.collidingWith["dialog_npc"]==True:
            self.rect.x=self.collidingObject["dialog_npc"].rect.x-60
            self.rect.y=self.collidingObject["dialog_npc"].rect.y

        if self.collidingWith["animalgame_npc"]==True or self.readytoplay==2:
            if self.readytoplay==1:#play
                self.rect.x=self.collidingObject["animalgame_npc"].rect.x
                self.rect.y=self.collidingObject["animalgame_npc"].rect.y+150
            if self.readytoplay==0 :#quit
                self.rect.x=self.collidingObject["animalgame_npc"].rect.x
                self.rect.y=self.collidingObject["animalgame_npc"].rect.y-70
            if self.readytoplay==2:#reset
                self.rect.topleft=(200-self.cameraX,430-self.cameraY)
                


        return self.rect

    def try_move(self):
        keys=pygame.key.get_pressed()


            # Update Player Position
        dx=0
        dy=0
        if keys[pygame.K_w] and self.rect.top > 0 :
            dy -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
            dy += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            dx -= self.speed
        if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
            dx += self.speed
            
        self.rect.x+=dx
        self.rect.y+=dy
        self.dx=dx
        self.dy=dy


        return self.rect ,self.dy,self.dx

    def update(self, width,height):
        if self.index==119:
            self.index=0
        else:
            self.index+=1
        self.image=self.images[self.index]

    def draw(self, window, dx=0, dy=0):
        
        self.update(PlayerSettings.playerWidth,PlayerSettings.playerHeight)
        self.rect.x-=dx
        self.rect.y-=dy
        window.blit(self.image, (self.rect.x-25,self.rect.y-28,self.rect.width,self.rect.height))

        
    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy

    def eggborn(self):
        if self.hadbattle and self.egg!=0:
            for i in range(self.egg):
                a=len(self.animal)
                b=random.randint(0,100)
                if b<95:
                    typ=b%8
                else:
                    typ=8
                self.animal.add(Animal(typ,600+(a%6)*100,100+((a//6)%6)*100))
        self.egg=0
        return self.animal