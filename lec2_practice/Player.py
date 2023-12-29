# -*- coding:utf-8 -*-

from Settings import *
import pygame


class Player(pygame.sprite.Sprite):
    i=0
    def __init__(self, x, y):
        super().__init__()
        self.image = GamePath.player[0]
        self.speed = PlayerSettings.playerSpeed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def show(self):
        self.image=GamePath.player[Player.i]
        if Player.i==120:
            Player.i=0
        else:
            Player.i+=1
        return self.image
    def update(self, keys, scene):
        if keys[pygame.K_w] and self.rect.top > 0 :
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
            self.rect.x += self.speed

    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy
