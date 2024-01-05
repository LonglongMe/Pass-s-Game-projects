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
        self.rect.topleft = (30+(order)*130, 350)
        self.fontColor=(0,0,0)
        self.renderlevelcolor=None
        self.position=None
        self.rendermodcolor=None
        self.roundtimes=0
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
            a=random.randint(1,100)
            b=random.randint(1,10)
            sort=0
            level=0
            if a>=70 and a<98:#atk
                sort=0
            elif a>=20 and a<70:
                if a<50:#buff
                    sort=2
                if a>=50 and a<55:#sacrifice
                    sort=6
                if a>=55 and a<60:#rebound
                    sort=7
                if a>=60 and a<62:#laststand
                    sort=8
                if a>=62 :#spell
                    sort=4
            elif a>=98:#joker
                sort=9
            else:#cure
                sort=1

            if b>=6:
                level=1
            elif b>=2 and b<7:
                level=2
            else:
                level=3         
            return Card(sort,level,self.order)
    def random_card_enemy(self):
        if self.sort==5:
            a=random.randint(1,10)
            b=random.randint(1,10)
            sort=0
            level=0
            if a>=7 :#atk
                sort=0
            else:
                sort=2#buff


            if b>=6:
                level=1
            elif b>=2 and b<7:
                level=2
            else:
                level=3         
            return Card(sort,level,self.order)
    def display_card(self):
            self.position = ( self.rect.x+self.width-3, self.rect.y+self.width-2, 126, 184 )   
            #render cards
            #render image
            #self.window.blit(self.image,(self.rect.x+self.width,self.rect.y+self.width))
            #render margin and level color
            self.renderlevelcolor = pygame.Surface((120, 42), pygame.SRCALPHA)
            if self.sort in [0,1,2]:
                self.renderlevelcolor.fill(self.content_color)
            #self.window.blit(transparent_rect, (self.rect.x+5, self.rect.y+110))
            #pygame.draw.rect(self.window,self.margin_color, self.position,self.width,border_radius=9 )
            #render light mod
            self.rendermodcolor = pygame.Surface((124,182), pygame.SRCALPHA)
            self.rendermodcolor.fill((0, 0,0, 20))
            self.image=self.images[self.sort]
            #self.window.blit(transparent_rect, (self.rect.x,self.rect.y))
           

class CardSet:
    begin=1
    ismyround=1
    atkgif=0
    atktimes=0
    enemyatktimes=0
    win=0
    actanimategif=0
    actcuregif=0
    enemyactlightninggif=0
    actlightninggif=0
    cards=[]
    selected=[]
    enemycards=[Card(5,1,i) for i in range(3)]
    pressed=0
    enemy_Accumulated_atk=1
    Accumulated_atk=1
    enemy_ATK_change=1
    Hp_change=0
    ATK_change=1
    enemyinitialhp=100
    enemy_hp=100
    playerinitialhp=50
    playerinitialatk=5
    enemyinitialatk=3
    playerhp=50
    leftround=20
    accumulateatkgifindex=0
    enemy_round_count=0
    def __init__(self, cards: List[Card],window) -> None:
        CardSet.cards=copy.copy(cards)
        self.window=window
        self.font = pygame.font.Font(None, 40)
        self.hpfont = pygame.font.Font(None, 15)
        self.hpfontcolor=(255,255,255)
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

        #self.gradient_fill_rect(self.window, (0,350,960,250), (0,0,0,140), (0,0,0,255))
    def curegif(self):

        
        if CardSet.actcuregif>0 :
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth-50, PlayerSettings.playerHeight)) for img in GamePath.cure]
            image = images[CardSet.actcuregif%3]
            if CardSet.actcuregif>20:
                CardSet.actcuregif=0
            else:
                CardSet.actcuregif+=1
            #render blood volume change
            text4 = "+ "+str(int(CardSet.Hp_change))
            self.window.blit(self.hpfont.render(text4, True, self.hpfontcolor),(70+CardSet.actcuregif//2,10)) 
            self.window.blit(image, (100,200)) 
    def accumulategif(self):
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightshield]
        for i in range(int(CardSet.Accumulated_atk//2)):
            imagee = images[(CardSet.accumulateatkgifindex//2+1+i)%9]
            self.window.blit(imagee, (100,200))
        if CardSet.accumulateatkgifindex==16:
            CardSet.accumulateatkgifindex=1
        else:
            CardSet.accumulateatkgifindex+=1      
    def lightninggif(self):
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightning]
        
        imagee = images[CardSet.actlightninggif//2]
        
        self.window.blit(imagee, (500,200))
        if CardSet.actlightninggif==8:
            CardSet.actlightninggif=0
        else:
            CardSet.actlightninggif+=1
    def atk_gif(self):
        for i in range(CardSet.atktimes):
            text3 = "- "+str(int(CardSet.ATK_change//(CardSet.atktimes)))
            self.window.blit(self.font.render(text3, True, (255,255,255)),(470+CardSet.atkgif+2*i,250+40*i)) 
        if CardSet.atkgif>40:
            CardSet.atkgif=0
            CardSet.atktimes=0
        else:
            CardSet.atkgif+=1
    def enemy_atk_gif(self):
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightning]     
        imagee = images[CardSet.enemyactlightninggif%5]
        if CardSet.enemyactlightninggif>0:
            self.window.blit(imagee, (100,200))
        if CardSet.enemyactlightninggif==10:
            CardSet.enemyactlightninggif=0
        if CardSet.enemyactlightninggif>0:
            CardSet.enemyactlightninggif+=1

        for i in range(CardSet.enemyatktimes):
            text3 = "- "+str(int(CardSet.ATK_change//(CardSet.enemyatktimes)))
            if CardSet.atkgif>0:
                 self.window.blit(self.font.render(text3, True, (255,255,255)),(170+CardSet.atkgif+2*i,250+40*i)) 
        if CardSet.atkgif>40:
            CardSet.atkgif=0
            CardSet.enemyatktimes=0
        if CardSet.atkgif>0:
            CardSet.atkgif+=1
  
    def animategif(self):
        
        if CardSet.actanimategif>0 and CardSet.actanimategif<81:
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (426,240)) for img in GamePath.animate]
            image = images[CardSet.actanimategif]
            CardSet.actanimategif+=1
            x=CardSet.actanimategif
            pygame.draw.rect(self.window,(30,30,30),(0,150,960,240),0)
            self.window.blit(image, (100,150))



        if CardSet.actanimategif==81:
            CardSet.actanimategif=0
            CardSet.actlightninggif=1
    def Playcards(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and len(CardSet.selected)==3:
            self.act_my_changes()

            for card in CardSet.cards:
                for playedcards in CardSet.selected:
                    if card.order==playedcards.order:
                        card.sort=5
                        card.image=card.images[card.sort]
                        card.rect.y+=40
                        CardSet.selected.remove(card)    
       
        #print(Card.selected)
    def act_my_changes(self):#data adjust
        Hp_change=0
        real_ATK=0
        Accumulate_ATK=CardSet.Accumulated_atk
        for card in CardSet.selected:
            #card=atk
            if card.sort==0:
                enhancement=[1.1,1.2,1.5]
                real_ATK+=enhancement[card.level-1]
                CardSet.atktimes+=1

            #card=cure
            if card.sort==1:
                enhancement=[0.1,0.2,0.3]
                Hp_change+=enhancement[card.level-1]

            #card=buff-accumulate atk
            if card.sort==2:
                enhancement=[1,2.3,3.4]
                Accumulate_ATK+=enhancement[card.level-1]
            print(card.sort,Hp_change,real_ATK)
        #plaer atk number adjust and activate animate        
        if real_ATK!=0:
            real_ATK=real_ATK*Accumulate_ATK*CardSet.playerinitialatk          
            if Accumulate_ATK>10:
                CardSet.actlightninggif=1

            CardSet.Accumulated_atk=1
        else:
            CardSet.Accumulated_atk+=Accumulate_ATK
        #plaer hp number adjust and activate animate
        if Hp_change>0:
            CardSet.Hp_change=int(Hp_change)
            CardSet.actcuregif=1
        CardSet.ATK_change=int(real_ATK)
        #enemy hp number adjust
        if CardSet.enemy_hp-real_ATK>0:
            CardSet.enemy_hp-=int(real_ATK)
        else:
            CardSet.enemy_hp=0
 
        CardSet.ismyround=0
    def act_enemy_change(self):
        real_ATK=0
        Accumulate_ATK=CardSet.enemy_Accumulated_atk
        for cards in CardSet.enemycards:
            if cards.sort==5:
                CardSet.enemycards=[cards.random_card_enemy() if i==cards else i for i in CardSet.enemycards]
        for card in CardSet.enemycards:
                       #card=atk
            if card.sort==0:
                enhancement=[1.1,1.2,1.5]
                real_ATK+=enhancement[card.level-1]
                CardSet.enemyatktimes+=1
            #card=buff-accumulate atk
            if card.sort==2:
                enhancement=[1,2.3,3.4]
                Accumulate_ATK+=enhancement[card.level-1]
            print(card.sort,real_ATK)
        #plaer atk number adjust and activate animate        
        if real_ATK!=0:
            real_ATK=real_ATK*Accumulate_ATK*CardSet.enemyinitialatk       
            if Accumulate_ATK>10:
                CardSet.enemyactlightninggif=1
            CardSet.atkgif=1
            CardSet.enemy_Accumulated_atk=1
        else:
            CardSet.enemy_Accumulated_atk=Accumulate_ATK
        #plaer hp number adjust and activate animate

        CardSet.enemy_ATK_change=int(real_ATK)
        #player hp number adjust
        if CardSet.playerhp-real_ATK>0:
            CardSet.playerhp-=int(real_ATK)
            CardSet.leftround-=1
        else:
            CardSet.playerhp=0



        print("enemyacted")



    def DrawNewCard(self):
        for cards in CardSet.cards:
            if cards.sort==5:
                CardSet.cards=[cards.random_card() if i==cards else i for i in CardSet.cards]
    def Win(self):
        bg=pygame.transform.scale(pygame.image.load(GamePath.dialog), (900, 200))
        
        if CardSet.enemy_hp==0 and CardSet.leftround>=0:
            CardSet.win=1
            b=pygame.font.SysFont(fontlist[17], 50)
            text = b.render("You win! in " + str(20-CardSet.leftround)+"rounds",True,(20,0,0))
            self.window.blit(bg, (30, 170))
            self.window.blit(text,(250,240))
        elif CardSet.enemy_hp>0 and CardSet.leftround<=0:

            b=pygame.font.SysFont(fontlist[17], 50)
            text = b.render("You Lose by "+ str(20-CardSet.leftround)+"rounds",True,(20,0,0))
            self.window.blit(bg, (30, 170))
            self.window.blit(text,(250,240))
    def Update_card(self):

        for cards in CardSet.cards:
            cards.display_card()
            self.window.blit(cards.image,(cards.rect.x+cards.width,cards.rect.y+cards.width))
            self.window.blit(cards.renderlevelcolor, (cards.rect.x+5,cards.rect.y+140))
            pygame.draw.rect(self.window,cards.margin_color, cards.position,cards.width,border_radius=9 )
            self.window.blit(cards.rendermodcolor, (cards.rect.x,cards.rect.y))


        #CardSet.actanimategif==0 and 
        if CardSet.win==0 :
            #print(CardSet.enemyactlightninggif)
            if CardSet.ismyround==1 and CardSet.enemyactlightninggif==0 and CardSet.atkgif==0:#if the game is in player's round:and CardSet.begin==0
                CardSet.DrawNewCard(self)#draw new card
                CardSet.Seclect_Card(self)# 1 select card in list by mouse
                CardSet.Playcards(self)# 2 play 3 cards selceted by "space"
                if CardSet.enemy_hp==0 or CardSet.leftround==0:
                    self.Win()

            #act gif of player's action
            if CardSet.actlightninggif>0:
                self.lightninggif()
            if CardSet.actcuregif>0:
                self.curegif()           
            if CardSet.Accumulated_atk>1:
                self.accumulategif()
            if CardSet.atktimes>0:
                self.atk_gif()

                #determin whether win                         

            if CardSet.ismyround==0  and CardSet.actlightninggif==0 and CardSet.actcuregif==0 and CardSet.atkgif==0:
                if CardSet.enemy_round_count==0:
                    print("enmy acted") 
                    self.act_enemy_change()
                    CardSet.enemy_round_count=1
                else:
                    if CardSet.enemyatktimes>0:
                        self.enemy_atk_gif()
                    for cards in CardSet.enemycards:
                        cards.display_card()
                        cards.rect.x=400+110*cards.order
                        cards.rect.y=130+5*cards.order
                        self.window.blit(cards.image,(cards.rect.x+cards.width,cards.rect.y+cards.width))
                        self.window.blit(cards.renderlevelcolor, (cards.rect.x+5,cards.rect.y+140))
                        pygame.draw.rect(self.window,cards.margin_color, cards.position,cards.width,border_radius=9 )
                        self.window.blit(cards.rendermodcolor, (cards.rect.x,cards.rect.y))
                        

                mousepress=pygame.mouse.get_pressed()
                if mousepress[0]:
                    print("detected")
                    CardSet.enemy_round_count=0
                    CardSet.enemycards=[Card(5,1,i) for i in range(3)]
                    CardSet.ismyround=1
        else:
            self.Win()


        #render general information:
        #1 render player hp
        pygame.draw.rect(self.window,(240,60,60), (20,10,CardSet.playerhp/CardSet.playerinitialhp*300,10),0,border_radius=30 )
        #2 render enmey hp
        pygame.draw.rect(self.window,(240,60,60), (500,10,CardSet.enemy_hp/CardSet.enemyinitialhp*400,10),0,border_radius=30)
        text1 = str(int(CardSet.enemy_hp))
        self.window.blit(self.hpfont.render(text1, True, self.hpfontcolor),(530,10)) 
        text2 = str(int(CardSet.playerhp))
        self.window.blit(self.hpfont.render(text2, True, self.hpfontcolor),(50,10))
        #3 render left rounds and atk accumulation:


        text = "Accumulated ATK: " + str(int(CardSet.Accumulated_atk))
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY-175)) 

        text = "Left round: " + str(CardSet.leftround)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX-300, BattleSettings.textStartY-210))

        text = "Accumulated ATK: " + str(int(CardSet.enemy_Accumulated_atk))
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX+150, BattleSettings.textStartY-175)) 
        #3 display mouse in game

        mousepos=pygame.mouse.get_pos()
        pygame.draw.circle(self.window, (100,0,0), (mousepos[0],mousepos[1]),5, width=0)



class Background:
    def __init__(self,window) -> None:
        self.window=window
    def showbg(self):
        bg=pygame.transform.scale(pygame.image.load(GamePath.background), (960, 540))
        self.window.blit(bg, (0, 0))
        #self.gradient_fill_rect(self.window, (0,350,960,250), (0,0,0,140), (0,0,0,255))
        transparent_rect = pygame.Surface((960, 250), pygame.SRCALPHA)
        transparent_rect.fill((0, 0,0, 140))
        self.window.blit(transparent_rect, (0, 350))
        databg = pygame.Surface((960,100), pygame.SRCALPHA)
        databg.fill((200,200,200,100))
        self.window.blit(databg,(0,0))


      
def run_game():

    pygame.init()
    window = pygame.display.set_mode((960,540))
    bg=Background(window)
    cards=[Card(5,1,i) for i in range(6)]

    Handset=CardSet(cards,window)

    clock = pygame.time.Clock()
   # player=Player(100,150)
    
    while True:
        clock.tick(30)
        window.fill((10,30,20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.showbg()
        Handset.Update_card()

        
  

            
        
        #player.draw(window)
        pygame.display.flip()

if __name__ == "__main__":
    run_game()