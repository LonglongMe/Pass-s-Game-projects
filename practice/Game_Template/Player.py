import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth+10, PlayerSettings.playerHeight+10)) for img in GamePath.player]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.width=10
        self.rect.height=10
        self.rect.topleft = (x,y)
        self.next_rect=self.rect
        self.speed = PlayerSettings.playerSpeed
        self.talking = False
        self.dx=0
        self.dy=0
        self.OriginHP = PlayerSettings.playerHP
        self.Hp=self.OriginHP
        self.attack = PlayerSettings.playerAttack
        self.defence = PlayerSettings.playerDefence
        self.card_list=[]

    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


    def try_move(self):
        keys=pygame.key.get_pressed()
        if self.talking:
            # 如果不移动，显示静态图像
            self.index = 0
            self.image = self.images[0]
        else:
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
        window.blit(self.image, (self.rect.x-15,self.rect.y-15,self.rect.width,self.rect.height))

        
    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy