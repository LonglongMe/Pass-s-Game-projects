import pygame
import sys
from Settings import *
import random
import copy
from typing import List
import pygame.gfxdraw
from pygame.locals import *
from Player import Player
from time import sleep
fontlist=pygame.font.get_fonts()
 
game_background_list=[]
effect_animate=[]

#game_backround=pygame.image.load(card_backround_list[i])
#game_backround = pygame.transform.scale(card_backround, (120, 180))
    
class Card:  #basic information of differernt cards
    def __init__(self,sort,level,order):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (CardSettings.cardWidth, CardSettings.cardHeight)) for img in GamePath.card_backround_list]
        self.sort=sort
        self.level=level
        self.width=5 # marginwidth
        self.order=order
        self.Accumulated_atk=1
        self.Hp_change=0
        self.ATK_change=1
        self.image=self.images[self.sort]
        self.rect = self.image.get_rect()
        self.rect.topleft = (BattleSettings.boxStartX+30+(order)*130, BattleSettings.boxStartY+350)
        self.fontColor=(0,0,0)
        self.font = pygame.font.SysFont("impact", 15)
        self.font2=pygame.font.SysFont("impact", 22)
        self.renderlevelcolor=None
        self.position=(self.rect.x+2,self.rect.y+2,self.rect.width+5,self.rect.height+5)
        self.rendermodcolor=None
        self.roundtimes=0
        self.colorlist= [(50,130, 250,140),(150,15,160,180),(180,15,10,210)]
        self.colorindex=0
        self.level4atk=random.randint(1,7)
        self.level4cure=random.randint(1,4)
        self.level4buff=random.randint(1,7)
    

        self.text = None
        self.textdata=None

        self.textdatarect=None
        #LEVEL REPRESENTING COLOR 
          #APPEND MARGIN
        self.margin_color=(45,70,130)
    def random_card(self,type):
        if self.sort==5:
            a=random.randint(1,100)
            b=random.randint(1,10)
            sort=0
            level=0
            if type==0:
                if a<=50:#atk
                    sort=0
                elif a>=40 and a<90:#buff
                    sort=2
                else:#cure
                    sort=1
                if b>=2:
                    level=1
                else:
                    level=2
            if type==1:
                if a<=50:#atk
                    sort=0
                elif a>=40 and a<90:#buff
                    sort=2
                else:#cure
                    sort=1
                if b>=5:
                    level=1
                elif b>=2 and b<5:
                    level=2
                else:
                    level=3
            if type==2:
                if a<=40:#atk
                    sort=0
                elif a>=40 and a<75:#buff
                    sort=2
                else:#cure
                    sort=1   
                if b>=6:
                    level=1
                elif b>=2 and b<6:
                    level=2
                else:
                    level=3      
            if type==3:
                if a<=40:#atk
                    sort=0
                elif a>=40 and a<70:#buff
                    sort=2
                elif a>=70 and a<74:
                    sort=6
                else:#cure
                    sort=1
                if b>=6:
                    level=1
                elif b>=2 and b<6:
                    level=2
                else:
                    level=3     
            if type==4:
                if a<=40:#atk
                    sort=0
                elif a>=40 and a<70:#buff
                    sort=2
                elif a>=70 and a<74:
                    sort=6
                else:#cure
                    sort=1
                if b>=6:
                    level=1
                elif b>4 and b<6:
                    level=2
                elif b>=2 and b<=4:
                    level=3  
                else:
                    level=4      
            return Card(sort,level,self.order)
    def random_card_enemy(self,type):
        if self.sort==5:
            a=random.randint(1,100)
            b=random.randint(1,10)
            sort=0
            level=0
            if type==0:
                if a<=50:#atk
                    sort=0
                elif a>=40 and a<90:#buff
                    sort=2
                else:#cure
                    sort=1
                if b>=2:
                    level=1
                else:
                    level=2
            if type==1:
                if a<=50:#atk
                    sort=0
                elif a>=40 and a<90:#buff
                    sort=2
                else:#cure
                    sort=1
                if b>=5:
                    level=1
                elif b>2 and b<5:
                    level=2
                else:
                    level=3
            if type==2:
                if a<=40:#atk
                    sort=0
                elif a>=40 and a<75:#buff
                    sort=2
                else:#cure
                    sort=1 
                if b>=5:
                    level=1
                elif b>2 and b<5:
                    level=2
                else:
                    level=3     
            if type==3:
                if a<=40:#atk
                    sort=0
                else:
                    sort=2
                if b>=6:
                    level=1
                elif b>2 and b<6:
                    level=2
                else:
                    level=3     
            if type==4:
                if a<=40:#atk
                    sort=0
                else:#buff
                    sort=2

                if b>=6:
                    level=1
                elif b>4 and b<6:
                    level=2
                elif b>2 and b<=4:
                    level=3  
                else:
                    level=4      
            return Card(sort,level,self.order)
    def update_card(self):
            #color 
            if self.level<4:
                content_color =self.colorlist[self.level-1]
            if self.level==4:#mistry color of level4 card
                if self.colorindex<1510:
                    self.colorindex+=3
                else:
                    self.colorindex=0
                i=self.colorindex
                if i<255:
                    a=i
                    b=255
                    c=0
                elif 255<=i<510:
                    a=255
                    b=510-i
                    c=0
                elif 510<=i<765:
                    a=255
                    b=0
                    c=i-510
                elif 765<=i<1010:
                    a=1010-i
                    b=0
                    c=255
                elif 1010<=i<1265:
                    a=0
                    b=i-1010
                    c=255
                elif 1265<=i<1520:
                    a=0
                    b=255
                    c=1520-i
                content_color=[a,b,c]

            self.renderlevelcolor = pygame.Surface((120, 42), pygame.SRCALPHA)
            if self.sort in [0,1,2]:
                self.renderlevelcolor.fill(content_color)

            #information 
                self.text = "Level"+str(self.level)
                if self.sort==0:#atk
                    a=[1.1,1.2,1.5,"???"]
                    self.textdata = self.font2.render(str(a[self.level-1]),True,(220,220,220))
                if self.sort==1:#cure
                    a=["5%","8%","10%","???"]
                    self.textdata = self.font2.render("+"+str(a[self.level-1]),True,(220,220,220))
                if self.sort==2:#buff
                    a=["120%","150%","200%","???"]
                    self.textdata = self.font2.render("x"+str(a[self.level-1]),True,(220,220,220))
                self.textdatarect=self.textdata.get_rect()
                self.textdatarect.x=self.rect.x+(CardSettings.cardWidth-self.textdatarect.width)//2+5
                self.textdatarect.y=self.rect.y+138
        
            
            #light mod
            self.rendermodcolor = pygame.Surface((124,182), pygame.SRCALPHA)
            self.rendermodcolor.fill((0, 0,0, 20))
            self.image=self.images[self.sort]

            #position
            self.position=(self.rect.x+2,self.rect.y+2,self.rect.width+6,self.rect.height+5)

    def rendermycard(self,window,x,y):
        self.update_card()#update card's imformation
        #and then display them 

        window.blit(self.image,(x+self.width,y+self.width))
        window.blit(self.renderlevelcolor, (x+5,y+140))
        pygame.draw.rect(window,self.margin_color,(x+2,y+2,self.rect.width+6,self.rect.height+5),self.width,border_radius=9 )
        window.blit(self.rendermodcolor, (x,y)) 
        if self.sort in[0,1,2]:
            self.textdatarect.x=x+(CardSettings.cardWidth-self.textdatarect.width)//2+5
            self.textdatarect.y=y+138
            window.blit(self.font.render(self.text, True, (210,210,210)),(x+44,y+162,60,20))
            window.blit(self.textdata,self.textdatarect)
    def renderenemycard(self,window):
        self.update_card()#update card's imformation
        #and then display them 
        self.rect.x=BattleSettings.boxStartX+400+110*self.order
        self.rect.y=BattleSettings.boxStartY+140
        window.blit(self.image,(self.rect.x+self.width,self.rect.y+self.width))
        window.blit(self.renderlevelcolor, (self.rect.x+5,self.rect.y+140))
        pygame.draw.rect(window,self.margin_color, self.position,self.width,border_radius=9 )
        window.blit(self.rendermodcolor, (self.rect.x,self.rect.y)) 
        if self.sort in[0,1,2]:
            window.blit(self.font.render(self.text, True, (210,210,210)),(self.rect.x+44,self.rect.y+162,60,20))
            window.blit(self.textdata,self.textdatarect)

