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
        self.originrect_x=x
        self.originrect_y=y
        self.rect.x=x
        self.rect.y=y
        
    def draw(self, window, dx=0, dy=0):
        self.rect.x=self.originrect_x-dx
        self.rect.y=self.originrect_y-dy
        window.blit(self.image, (self.rect))
        self.lastdx=dx
        self.lastdy=dy

class Decorate(pygame.sprite.Sprite):
    frame=0
    def __init__(self,n, x, y):
        super().__init__()
        self.n=n
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (SceneSettings.tileWidth, SceneSettings.tileHeight*2)) for img in GamePath.fire]
        self.image=self.images[Decorate.frame//15]
        self.rect = self.image.get_rect()
        self.originrect_x=x
        self.originrect_y=y
        self.rect.x=x
        self.rect.y=y

    def update(self):

        if Decorate.frame<90:
            self.image=self.images[Decorate.frame//15]
            Decorate.frame+=1
        else:
            Decorate.frame=0
        self.rect = self.image.get_rect()
        self.rect.height=50
        self.rect.topleft = (self.rect.x, self.rect.y-40)
    def draw(self, window, dx=0, dy=0):
        self.rect.x=self.originrect_x-dx
        self.rect.y=self.originrect_y-dy
        window.blit(self.image, (self.rect))




def gen_wild_map():
    images = [pygame.image.load(tile) for tile in GamePath.groundTiles]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    mapObj = []
    for i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)
    
    return mapObj

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
    datamatrix=[[1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [2,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,2,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
                [1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                [1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1],
                [1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                ]
    for i in range(36):  #SceneSettings.tileXnum
        for j in range(19): #SceneSettings.tileYnum
            if datamatrix[j][i]==1:
                obstacles.add(Block(datamatrix[j][i], SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
            if datamatrix[j][i]==2:
                decorates.add(Decorate(datamatrix[j][i], SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))

    return obstacles ,decorates   

def gen_boss_obstacle():
    ##### Your Code Here ↓ #####
    pass
    ##### Your Code Here ↑ #####
