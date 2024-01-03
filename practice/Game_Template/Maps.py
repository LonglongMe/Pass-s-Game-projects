# -*- coding:utf-8 -*-

import pygame

from Settings import *
from random import random, randint

class Block(pygame.sprite.Sprite):

    def __init__(self,n, x, y):
        super().__init__()
        self.n=n
        self.image = pygame.transform.scale(pygame.image.load(GamePath.tree) , (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, (SceneSettings.tileWidth, SceneSettings.tileHeight))

class Decorate(pygame.sprite.Sprite):
    frame=0
    def __init__(self,n, x, y):
        super().__init__()
        self.n=n
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (SceneSettings.tileWidth, SceneSettings.tileHeight*2)) for img in GamePath.fire]
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
    def draw(self,window):
        if self.n==1:
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
        if self.n==2:
            if Decorate.frame<60:
                self.image=self.images[Decorate.frame//10]
                Decorate.frame+=1
            else:
                Decorate.frame=0
            self.rect = self.image.get_rect()
            self.rect.height=50
            self.rect.topleft = (self.x, self.y-40)
        window.blit(self.image, (SceneSettings.tileWidth, SceneSettings.tileHeight))

def gen_wild_map():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####

def gen_home_map():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####

def gen_boss_map():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####

def gen_home_obstacle():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####

def gen_wild_obstacle():
    decorates=pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    datamatrix=[[1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,2,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
                [1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                [1,1,0,0,1,1,1,2,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1],
                [1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                ]
    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            # 防止在出生点生成obstacle
            if datamatrix[j][i]==1:
                obstacles.add(Block(datamatrix[j][i], SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
            if datamatrix[j][i]==2:
                decorates.add(Decorate(datamatrix[j][i], SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
    return obstacles ,decorates   

def gen_boss_obstacle():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####
