# -*- coding:utf-8 -*-
from Settings import *
import pygame
from random import random,randint

class Block(pygame.sprite.Sprite):

    def __init__(self,n, x, y):
        super().__init__()
        self.n=n
        self.image = pygame.transform.scale(pygame.image.load(GamePath.tree) , (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        



class Decorate(pygame.sprite.Sprite):
    frame=0
    def __init__(self,n, x, y):
        super().__init__()
        self.n=n

        self.image = pygame.transform.scale(pygame.image.load(GamePath.tree) , (SceneSettings.tileWidth, SceneSettings.tileHeight))

        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (SceneSettings.tileWidth, SceneSettings.tileHeight*2)) for img in GamePath.fire]
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y


    def update(self):
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



def gen_map():
    images = [pygame.image.load(tile) for tile in GamePath.groundTiles]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    mapObj = []
    for i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)
    
    return mapObj

def build_obstacles():
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

