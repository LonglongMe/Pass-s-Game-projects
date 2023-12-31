import pygame
import sys
from Settings import *
import random
#fontlist=pygame.font.get_fonts()

 
game_background_list=[]
effect_animate=[]

class cardnum:
    "ATK"==0
    "CURE"==1
    "BUFF"==2
    "PURE"==3
    "DEBUFF"==4
    "EMPTY"==5

#game_backround=pygame.image.load(card_backround_list[i])
#game_backround = pygame.transform.scale(card_backround, (120, 180))
class Card(pygame.sprite.Sprite):
    selected=[]
    pressed=0

    def __init__(self,sort,level,window,order):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (CardSettings.cardWidth, CardSettings.cardHeight)) for img in GamePath.card_backround_list]
        self.sort=sort
        self.level=level
        self.width=5 # marginwidth
        self.window=window
        self.order=order
        self.Accumulated_atk=1
        self.Hp_change=0
        self.ATK_change=1
        self.image=self.images[self.sort]
        self.rect = self.image.get_rect()
        self.rect.topleft = (30+(order)*130, 350)
                #LEVEL REPRESENTING COLOR 
        if self.level==1:
            self.content_color = (50,130, 250,140)
        if self.level==2:
            self.content_color=(150,15,160,180)
        if self.level==3:
            self.content_color=(180,15,10,210)
        #APPEND MARGIN
        self.margin_color=(45,70,130)
    def Update_card(self):       
        #CHOSE FONT
       # d=pygame.font.SysFont(fontlist[6], 15)
        #check selected card
        Card.Seclect_Card(self)

        position = ( self.rect.x+self.width-2, self.rect.y+self.width-1, 124, 182 )   
        #render cards
        self.window.blit(self.image,(self.rect.x+self.width,self.rect.y+self.width))
        transparent_rect = pygame.Surface((120, 73), pygame.SRCALPHA)
        transparent_rect.fill(self.content_color)
        self.window.blit(transparent_rect, (self.rect.x+5, self.rect.y+110))
        pygame.draw.rect( self.window, self.margin_color, position,self.width,border_radius=9 )

    def Seclect_Card(self):
        #get key events
        
        mousepos=pygame.mouse.get_pos()
        #for trail: show mouse
        pygame.draw.rect( self.window, (100,0,0), (mousepos[0],mousepos[1],10,10), 0)
        #select card by mouse
        if pygame.mouse.get_pressed()[0]==False:
            Card.pressed=1           
        if mousepos[0] >= self.rect.x and mousepos[0]<self.rect.x+120 and mousepos[1] >self.rect.y  and mousepos[1]<self.rect.y+180  and pygame.mouse.get_pressed()[0] and Card.pressed==1:
            if len(Card.selected)<3 and (self.order,self.sort,self.level) not in Card.selected:
                Card.selected.append((self.order,self.sort,self.level))
                self.rect.y-=40
                print("choose")
            elif (self.order,self.sort,self.level) in Card.selected:
                Card.selected.remove((self.order,self.sort,self.level))
                self.rect.y+=40
                print("dechoose")
            Card.pressed=0
            
            print(Card.selected)
        #Play card


            
       
        #print(Card.selected)
    def act_changes(self):
        Hp_change=0
        real_ATK=0
        Accumulate_ATK=self.Accumulated_atk
        for card in Card.selected:
            #card=atk
            if card[1]==0:
                if card[2]==1:
                    real_ATK+=1.1
                if card[2]==2:
                    real_ATK+=1.2                
                if card[2]==1:
                    real_ATK+=1.5
            #card=cure
            if card[1]==1:
                if card[2]==1:
                    Hp_change+=0.1
                if card[2]==2:
                    Hp_change+=0.2                
                if card[2]==1:
                    Hp_change+=0.3
            #card=buff-accumulate atk
            if card[1]==2:
                if card[2]==1:
                    Accumulate_ATK+=1
                if card[2]==2:
                    Accumulate_ATK+=2                
                if card[2]==1:
                    Accumulate_ATK+=3


        if real_ATK!=0:
            real_ATK=real_ATK*Accumulate_ATK
            self.Accumulate_ATK=1
        self.Hp_change=Hp_change
        self.ATK_change=real_ATK
        Card.selected=[]
class Background:
    def __init__(self,window) -> None:
        self.window=window
    def showbg(self):
        transparent_rect = pygame.Surface((960, 250), pygame.SRCALPHA)
        transparent_rect.fill((0, 0,0, 140))
        self.window.blit(transparent_rect, (0, 350))

        
def run_game():
    pygame.init()
    window = pygame.display.set_mode((960,540))
    bg=Background(window)
    cards=[Card(random.randint(1,4),1,window,i) for i in range(6)]
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.showbg()
        for card in cards:
            card.Update_card()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and len(Card.selected)==3:
            Card.act_changes(card)
            for card in cards:
                for x in Card.selected:
                    if card.order==x[0]:
                        card.sort=5
                        card.rect.y+=40
                        Card.selected.remove(card)


        pygame.display.flip()

if __name__ == "__main__":
    run_game()
"""
        for x in Card.selected:
            if (self.order,self.sort,self.level)==x:
                if self.rect.y>320:
                    self.rect.y-=30    
                    print("moved") 
            else:
                if self.rect.y<=320:
                    self.rect.y+=30  
                    print("drawback")"""