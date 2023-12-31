import pygame
import sys
from Settings import *
import random
import copy
from typing import Tuple, List

fontlist=pygame.font.get_fonts()

 
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
        self.rect.topleft = (30+(order)*130, 350)
        self.fontColor=(0,0,0)
        #LEVEL REPRESENTING COLOR 
    
        if self.level==1:
            self.content_color = (50,130, 250,140)
        if self.level==2:
            self.content_color=(150,15,160,180)
        if self.level==3:
            self.content_color=(180,15,10,210)
        #APPEND MARGIN
        self.margin_color=(45,70,130)
    def random_card(self):
        if self.sort==5:
            a=random.randint(1,10)
            b=random.randint(1,10)
            sort=0
            level=0
            if a>=7:
                sort=0
            elif a>=3 and a<7:
                sort=2
            else:
                sort=1
            if b>=6:
                level=1
            elif b>=2 and b<7:
                level=2
            else:
                level=3         
            return Card(sort,level,self.order)

class CardSet:
    cards=[]
    selected=[]
    pressed=0
    Accumulated_atk=1
    Hp_change=0
    ATK_change=1
    enemy_hp=300
    playerhp=50
    leftround=10
    def __init__(self, cards: List[Card],window) -> None:
        CardSet.cards=copy.copy(cards)
        self.window=window
        self.font = pygame.font.Font(None, 40)
        self.fontColor=(0,0,0)
        pass
    def Seclect_Card(self):
        #get key events        
        mousepos=pygame.mouse.get_pos()
        #for trail: show mouse
        number=0
        for cards in CardSet.cards:
        #select card by mouse
            if pygame.mouse.get_pressed()[0]==False:
                CardSet.pressed=1           
            if mousepos[0] >= cards.rect.x and mousepos[0]<cards.rect.x+120 and mousepos[1] >cards.rect.y  and mousepos[1]<cards.rect.y+180  and pygame.mouse.get_pressed()[0] and CardSet.pressed==1:
                if len(CardSet.selected)<3 and cards not in CardSet.selected:
                    CardSet.selected.append(cards)
                    cards.rect.y-=40
                    number+=1
                    print("choose")
                elif cards in CardSet.selected:
                    CardSet.selected.remove(cards)
                    number-=1
                    cards.rect.y+=40
                    print("dechoose")
                CardSet.pressed=0

                print(CardSet.selected)
        #Play card
    def detect_end_of_the_round(self):
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] >= 15 and mousepos[0]<45 and mousepos[1] >20  and mousepos[1]<50  and pygame.mouse.get_pressed()[0] :
            CardSet.Hp_change=0
            CardSet.ATK_change=1

    def Update_card(self):       
        CardSet.DrawNewCard(self)
        CardSet.Seclect_Card(self)
        CardSet.Playcards(self)
        CardSet.detect_end_of_the_round(self)
        for cards in CardSet.cards:
            position = ( cards.rect.x+cards.width-2, cards.rect.y+cards.width-1, 124, 182 )   
            #render cards
            self.window.blit(cards.image,(cards.rect.x+cards.width,cards.rect.y+cards.width))
            transparent_rect = pygame.Surface((120, 73), pygame.SRCALPHA)
            transparent_rect.fill(cards.content_color)
            self.window.blit(transparent_rect, (cards.rect.x+5, cards.rect.y+110))
            pygame.draw.rect(self.window,cards.margin_color, position,cards.width,border_radius=9 )
        pygame.draw.rect(self.window,cards.margin_color,(15,20,30,30),0,border_radius=9)
        text = "real attak: " + str(CardSet.ATK_change)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY-80))

        text = "cure hp: " + str(CardSet.Hp_change)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY-40))

        text = "my hp: " + str((CardSet.Hp_change+1)*CardSet.playerhp)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY-120))

        text = "accumulated atk: " + str(CardSet.Accumulated_atk)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY)) 

        text = "enemy hp: " + str(CardSet.enemy_hp)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX, BattleSettings.textStartY)) 

        text = "left round: " + str(CardSet.leftround)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX, BattleSettings.textStartY-40)) 
        self.Win()
        mousepos=pygame.mouse.get_pos()
        pygame.draw.circle(self.window, (100,0,0), (mousepos[0],mousepos[1]),5, width=0)

    def Playcards(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and len(CardSet.selected)==3:
            self.act_changes()

            for card in CardSet.cards:
                for playedcards in CardSet.selected:
                    if card.order==playedcards.order:
                        card.sort=5
                        card.image=card.images[card.sort]
                        card.rect.y+=40
                        CardSet.selected.remove(card)    
       
        #print(Card.selected)
    def act_changes(self):#data adjust
        Hp_change=0
        real_ATK=0
        Accumulate_ATK=self.Accumulated_atk
        for card in CardSet.selected:
            #card=atk
            if card.sort==0:
                enhancement=[1.1,1.2,1.5]
                real_ATK+=enhancement[card.level-1]

            #card=cure
            if card.sort==1:
                enhancement=[0.1,0.2,0.3]
                Hp_change+=enhancement[card.level-1]

            #card=buff-accumulate atk
            if card.sort==2:
                enhancement=[1,2,3]
                Accumulate_ATK+=enhancement[card.level-1]
            print(card.sort,Hp_change,real_ATK)

        if real_ATK!=0:
            real_ATK=real_ATK*Accumulate_ATK
            CardSet.Accumulated_atk=1
        else:
            CardSet.Accumulated_atk=Accumulate_ATK
        CardSet.Hp_change=int(Hp_change)
        CardSet.ATK_change=int(real_ATK)
        if CardSet.enemy_hp-real_ATK>0:
            CardSet.enemy_hp-=real_ATK
        else:
            CardSet.enemy_hp=0
        CardSet.leftround-=1
    def DrawNewCard(self):
        for cards in CardSet.cards:
            if cards.sort==5:
                CardSet.cards=[cards.random_card() if i==cards else i for i in CardSet.cards]
    def Win(self):
        if CardSet.enemy_hp==0 and CardSet.leftround>=0:
            pygame.draw.rect(self.window,(200,200,200), (0,160,1000,200),0)
            b=pygame.font.SysFont(fontlist[17], 50)
            text = b.render("You win! by" + str(10-CardSet.leftround)+"rounds",True,(20,0,0))
            self.window.blit(text,(150,220))
        elif CardSet.enemy_hp>0 and CardSet.leftround<=0:
            pygame.draw.rect(self.window,(200,200,200), (135,160,500,200),0,border_radius=9 )
            b=pygame.font.SysFont(fontlist[17], 50)
            text = b.render("You Lose! ",True,(20,0,0))
            self.window.blit(text,(150,210))







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
    cards=[Card(5,1,i) for i in range(6)]
    Handset=CardSet(cards,window)
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.showbg()
        Handset.Update_card()




        pygame.display.flip()

if __name__ == "__main__":
    run_game()
