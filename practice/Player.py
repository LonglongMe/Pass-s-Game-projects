# -*- coding:utf-8 -*-

from Settings import *
import pygame
import os

# 设置角色动画
class Player(pygame.sprite.Sprite):
    frame=0
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth+10, PlayerSettings.playerHeight+10)) for img in GamePath.player]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.width=25
        self.rect.height=50
        self.rect.topleft = (x,y)
        self.speed = PlayerSettings.playerSpeed
        self.talking = False

        self.OriginHP = PlayerSettings.playerHP
        self.Hp=self.OriginHP
        self.attack = PlayerSettings.playerAttack
        self.defence = PlayerSettings.playerDefence
        self.card_list=[]

    def move(self, dx, dy):
        self.rect = self.rect.move(dx,dy)

    def update(self, keys, scene):
        if self.talking:
            # 如果不移动，显示静态图像
            self.index = 0
            self.image = self.images[self.index]
        else:
            # Update Player Position
            dx = 0
            dy = 0
            if keys[pygame.K_w] and self.rect.top > 0 :
                dy -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
                dy += self.speed
            if keys[pygame.K_a] and self.rect.left > 0:
                dx -= self.speed
            if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
                dx += self.speed
                
            self.rect = self.rect.move(dx, dy)
            if pygame.sprite.spritecollide(self, scene.obstacles, False) or pygame.sprite.spritecollide(self, scene.decorates, False,pygame.sprite.collide_mask):
                # 遇到障碍物，取消移动
                self.rect = self.rect.move(-dx, -dy)

            # 更新角色动画


    def show(self):
        if Player.frame==119:
            Player.frame=0
        else:
            Player.frame+=1
        self.image=self.images[Player.frame]
    def draw(self, window):
        self.show()
        window.blit(self.image, (self.rect.x-15,self.rect.y-15,self.rect.width,self.rect.height))