# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self):
        raise NotImplementedError

    def reset_talkCD(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

class DialogNPC(NPC):
    def __init__(self, x, y, name, dialog):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

class ShopNPC(NPC):
    def __init__(self, x, y, name, items, dialog):
        super().__init__(x, y, name)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Money = 15):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (BattleSettings.monsterWidth//3, BattleSettings.monsterHeight//3)) for img in GamePath.monster]
        self.image=self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.originrect_x=x
        self.originrect_y=y
        self.HP = HP
        self.attack = Attack
        self.money= Money
        
    def draw(self, window, dx=0, dy=0):

        self.rect.x=self.originrect_x-dx
        self.rect.y=self.originrect_y-dy
        window.blit(self.image,self.rect)

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
