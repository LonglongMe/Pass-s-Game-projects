# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group
import random
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
    def __init__(self, x, y,order, HP = 100, Atk = 3, Money = 15):
        super().__init__()
        self.index=0
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (BattleSettings.monsterWidth//3, BattleSettings.monsterHeight//3)) for img in GamePath.monster]
        self.image=self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.originrect_x=x
        self.originrect_y=y
        self.HP = HP
        self.ATK = Atk
        self.money= Money
        self.order=order
        
        
    def draw(self, window, dx=0, dy=0):
        if self.index==39:
            self.index=0
        else:
            self.index+=1
        self.image=self.images[self.index//10]
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

class Animal(pygame.sprite.Sprite):
    def __init__(self,index,x,y) -> None:
        super().__init__()
        self.index=index
        speed=[1,1,1,1,1,1,1,2,2,1,2,2]
        self.speed=speed[self.index]
        self.step=30
        self.directionx=1
        self.directiony=0
        self.flame=0
        self.moving=1
        self.imagelist=[[pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.cat1],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.cat2],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.cat3],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.cat4],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.fish],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.elf],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.chicken1],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.chicken2],
                        [pygame.transform.scale(pygame.image.load(img), (70,70)) for img in GamePath.goldenbird],
                        [pygame.transform.scale(pygame.image.load(img), (40,40)) for img in GamePath.cat1]
                        ]
        self.images=self.imagelist[self.index]
        if self.index==0:
            self.images = [pygame.transform.scale(pygame.image.load(img), 
                                (40,40)) for img in GamePath.cat1]
        if self.index==0:
            self.images = [pygame.transform.scale(pygame.image.load(img), 
                                (40,40)) for img in GamePath.cat1]  
                  
        self.image=self.images[self.flame]
        self.rect = self.image.get_rect()
        self.definiterectx=x
        self.definiterecty=y

    def walk(self,player,animals,obstacles):
        self.definiterectx+=self.directionx*self.speed
        self.definiterecty+=self.directiony*self.speed
#pygame.sprite.spritecollide(self, animals, False) player.is_colliding_animal
        if pygame.sprite.spritecollide(self, obstacles, False):
            self.definiterectx-=2*self.directionx*self.speed
            self.definiterecty-=2*self.directiony*self.speed
            if self.directionx!=0:
                self.directiony=-1*self.directionx
                self.directionx=0
            elif self.directionx==0:
                self.directionx=self.directiony
                self.directiony=0

        for animal in animals:
            if self != animal and self.rect.colliderect(animal.rect):
                self.definiterectx-=2*self.directionx*self.speed
                self.definiterecty-=2*self.directiony*self.speed
                self.directionx=self.directionx*random.choice([-1,1])
                self.directiony=self.directiony*random.choice([-1,1])


        if pygame.sprite.spritecollide(self, player,False):

            self.definiterectx-=self.directionx*self.speed
            self.definiterecty-=self.directiony*self.speed
            self.moving=0
        else:
            if self.moving==0:
                self.directionx=self.directionx*-1
                self.directiony=self.directiony*-1
            self.moving=1
        #print(pygame.sprite.spritecollide(self, player, False)==True)
        #print(player.is_colliding_animal==True)
    def draw(self, window, dx=0, dy=0):
        if self.flame<12:
            self.flame+=1
        else:
            self.flame=0
        if self.moving==1:
            if self.directiony==-1:
                self.image=self.images[4*(self.flame//4)+3]
            elif self.directiony==1:
                self.image=self.images[4*(self.flame//4)]
            elif self.directionx==-1:
                self.image=self.images[4*(self.flame//4)+1]
            elif self.directionx==1:
                self.image=self.images[4*(self.flame//4)+2]
        else:
            if self.directiony==-1:
                self.image=self.images[3]
            elif self.directiony==1:
                self.image=self.images[0]
            elif self.directionx==-1:
                self.image=self.images[1]
            elif self.directionx==1:
                self.image=self.images[2]

        self.rect.x=self.definiterectx-dx
        self.rect.y=self.definiterecty-dy
        window.blit(self.image,self.rect)


        """
        if pygame.sprite.spritecollide(self, animals, False) or pygame.sprite.spritecollide(self, player, False) or pygame.sprite.spritecollide(self, obstacles, False):
            self.definiterectx-=self.directionx*self.speed
            self.definiterecty-=self.directiony*self.speed
            if self.directionx!=0:
                self.directiony=-1*self.directionx
                self.directionx=0
            elif self.directionx==0:
                self.directionx=-1*self.directiony
                self.directiony=0
"""