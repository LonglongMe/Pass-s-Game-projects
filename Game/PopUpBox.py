# -*- coding:utf-8 -*-

import pygame
from Card import Card
from typing import *
from Settings import *
from time import sleep

class DialogBox:
    def __init__(self, window, npc,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (20,20,20,200)):
        self.image=pygame.transform.scale(pygame.image.load(GamePath.npc), 
                            (BattleSettings.playerWidth+10, BattleSettings.playerHeight+10))#needs to be fixed
        self.window = window
        self.index=0
        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY-70
        # 最基础的字体和背景图片设置
        self.font = pygame.font.Font(None, 50)
        self.font2= pygame.font.Font(None, 40)
        self.font3=pygame.font.Font(None,33)
        self.hpfont = pygame.font.Font(None, 15)
        self.hpfontcolor=(255,255,255)
        self.fontColor=(255,255,255)
        self.selectedfontcolor=(255,100,100)
        self.donedialog=0
        self.bg = pygame.Surface((BattleSettings.boxWidth,
            BattleSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        self.firstchoice=0
        self.secondchoice=0
        self.contentx=BattleSettings.boxStartX+300
        self.contenty=BattleSettings.boxStartY+100
        self.selection=0
        self.hintindex=0
        self.pressing=0
        self.pressingw=0
        self.texts=None
        self.selectable=True
        self.title=None
        self.chosing=0
        self.hint=None

    def dialogboxdistribute(self):
        if self.firstchoice==0 and self.chosing==1:
            self.firstchoice=self.selection+1
            if self.firstchoice in [1,2,3]:
                self.selectable=False
                self.chosing=0
                self.secondchoice=0
            
        if self.firstchoice==1 and self.chosing==1:
            self.secondchoice=1
            self.selectable=False
            self.choing=0
        if self.firstchoice==3 and self.chosing==1:
            self.secondchoice=1
            self.selectable=False
            self.choing=0
            
    def Information(self):
        if self.firstchoice==1:
            if self.secondchoice==0:
                self.title=""
                self.texts=[
                            "Animals can improve your battle income.",
                            "More rare more gain.The only way to aquire animals",
                            "is buying eggs from merchants,and then you will find one ",
                            "animal of random type appears in your farm after one battle",
                          "                                                            press SPACE to go on"]
            if self.secondchoice==1:
                self.title="ANIMALS' INFORMATION:"
                self.texts=["",
                            "Chicks and fishes are the most common: 10 coin per battle",
                            "Cats are more rare: 20 coin per battle",
                            "Goldenbirds are the most rare: 100 coin per battle",]
        if self.firstchoice==2:
                self.title=None
                self.texts=["AS THE TILTLE SAYS, the game is a simulation of ",
                            "the last days of high school,where your enemies are",
                            "quizs and exams,the further you wander inside the maze,",
                            "the stronger enemy you will meet.If you win the battle,",
                            "coins will be rewarded so that you can improve",
                            "your inital attribute from shopping Npc",
                            "there are 4 easy enemies,2 strong enemies and 1 boss",
                            "When the boss is defeated, the game ends"
                ]
        if self.firstchoice==3:
            if self.secondchoice==0:
                self.title=None
                self.texts=["Collide with monster and your battle begins." ,
                            "SPACE and CLICK are your major input during the game.",
                            "You can select a card by a click.",
                            "Press SPACE and then:",
                            "Check information if you selected just one card;",
                            "Merge two cards into higher level card if you select two same card;",
                            "Play card if you selected three cards",
                            "                                                        press SPACE to go on"
                                ]
            if self.secondchoice==1:
                self.title=None
                self.texts=["Regular cards are cards with level written on it,",
                            "with LEVEL4 as the highest level",
                            "Special cards have no level and can't be merged",
                            "A GOOD STRATEGY is merge cards as MUCH you can,",
                            "so you will have MORE new cards next round,",
                            "Anthor one is to ACCUMULATE abundant buff cards",
                            "with the purpose to make your best shoot in the end"]

    def Selection(self):
        if self.firstchoice==0:
            self.title= "WHAT INFORMATION DO YOU NEED?"
            self.texts=[ "About Animals",
                    "About Enemys",
                    "About Battle",
                    ]
            self.hint="                                      press space to choose"
    
    def update_dialog(self):
        self.showbg()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_s]==False:
            self.pressing=0
        if keys[pygame.K_s] and self.pressing==0:
            if self.selection>=2:
                self.selection=0
            else:
                self.selection+=1
            self.pressing=1
        if keys[pygame.K_w]==False:
            self.pressingw=0
        if keys[pygame.K_w] and self.pressingw==0:
            if self.selection==0:
                self.selection=2
            else:
                self.selection-=1
            self.pressingw=1
        if keys[pygame.K_SPACE]==False:
            self.pressings=0
        if keys[pygame.K_SPACE] and self.pressings==0:
            self.chosing=1
            self.pressings=1
            self.dialogboxdistribute()



        #render texts
        if self.selectable:
            self.Selection()
            textbegin=self.contenty+60
            self.window.blit(self.font.render(self.title, True, self.fontColor),(self.contentx, textbegin))
            textbegin+=60
            for i in range(len(self.texts)):
                if i==self.selection:
                    self.window.blit(self.font.render(self.texts[i], True, self.selectedfontcolor),(self.contentx, textbegin)) 
                else:
                    self.window.blit(self.font2.render(self.texts[i], True, self.fontColor),(self.contentx, textbegin)) 
                textbegin+=50
            self.window.blit(self.font3.render(self.hint, True, self.fontColor),(self.contentx+40, textbegin))
        else:
            self.Information()
            textbegin=self.contenty
            if self.title!=None:
                self.window.blit(self.font.render(self.title, True, self.fontColor),(self.contentx, textbegin))
                textbegin+=40
            for text in self.texts:
                self.window.blit(self.font3.render(text, True, self.fontColor),(self.contentx-80, textbegin))
                textbegin+=50 

        #leave dialog
        if pygame.mouse.get_pressed()[0]:
            self.donedialog=1
        #hint
        hint="Click to back home "
        self.hintindex+=1
        if self.hintindex%25<16:
            self.window.blit(self.font3.render(hint, True, self.fontColor),(self.contentx+150, self.contenty+400)) 

    def showbg(self):

        #self.npcImg=self.npcimages[4*int((self.index//12)%4)]
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        transparent_rect = pygame.Surface((960, 250), pygame.SRCALPHA)
        transparent_rect.fill((0, 0,0, 140))
        self.window.blit(self.image, (self.playerX,
                                          self.playerY+100))

class AniamlgameBox:
    def __init__(self, window, npc,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (20,20,20,200)):
        self.image=pygame.transform.scale(pygame.image.load(GamePath.npc), 
                            (BattleSettings.playerWidth+10, BattleSettings.playerHeight+10))#needs to be fixed
        self.window = window
        self.index=0
        # 最基础的字体和背景图片设置
        self.npc=npc
        self.pressing=0
        self.selectable=1
        self.font2= pygame.font.Font(None, 38)
        self.font3=pygame.font.Font(None,27)
        self.hpfont = pygame.font.Font(None, 15)
        self.fontColor=(255,255,255)
        self.selectedfontcolor=(255,100,100)
        self.donedialog=0
        self.contentx=self.npc.rect.x+50
        self.contenty=self.npc.rect.y
        self.bg = pygame.Surface((BattleSettings.boxWidth//2,
            int(BattleSettings.boxHeight//3)), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        self.firstchoice=0
        self.secondchoice=0
        self.selection=2
        self.chosing=0
        self.title=None
        self.texts=None
        self.hardlevel=0
        self.pressings=0
        self.pressingw=0

    def dialogboxdistribute(self):
        if self.firstchoice==0 and self.chosing==1:
            if self.selection==0:
                self.firstchoice=1
                self.selectable=1
                self.chosing=0
            if self.selection==1:
                self.firstchoice=2
                self.selectable=0
                self.chosing=0
            if self.selection==2:
                self.donedialog=1
        if self.firstchoice==2 and self.chosing==1:
            self.firstchoice=0
            self.selection=0
            self.selectable=1
            self.chosing=0
        if self.firstchoice==1 and self.chosing==1:
            if self.selection==0:
                self.hardlevel=1
            elif self.selection==1:
                self.hardlevel=2
            elif self.selection==2:
                self.hardlevel=3
            self.donedialog=2
    def Information(self):
        if self.firstchoice==2:
            self.title=None
            self.texts=[
                        "CRAZY WILD ANIMALS IN YOUR GARDEN!",
                        "To get abundant coins as rewards",
                        "Please rush through and COLLIDE WITH THE TORCH ",
                        "WITHOUT being touched by wild animals",
                        "Select difficulty to get even more rewards!",
                        "                                        press SPACE to back"]

    def Selection(self):
        if self.firstchoice==0:
            self.title= "HOW  CAN  I  HELP?"
            self.texts=[ 
                        "Start game!",
                      "About this game",
                      "Leave"]
        if self.firstchoice==1:
            self.title="SELECT DIFFICULTY"
            self.texts=[ 
                    "WARM UP   REWARD:10 COINS",
                    "HARD      REWARD:20 COINS",
                    "IMPOSSIBLE REWARD:300 COINS!"]

    def update_animalgame(self):
        self.showbg()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_s]==False:
            self.pressing=0
        if keys[pygame.K_s] and self.pressing==0:
            if self.selection>=2:
                self.selection=0
            else:
                self.selection+=1
            self.pressing=1
        if keys[pygame.K_w]==False:
            self.pressingw=0
        if keys[pygame.K_w] and self.pressingw==0:
            if self.selection==0:
                self.selection=2
            else:
                self.selection-=1
            self.pressingw=1
        if keys[pygame.K_SPACE]==False:
            self.pressings=0
        if keys[pygame.K_SPACE] and self.pressings==0:
            self.chosing=1
            self.pressings=1
            self.dialogboxdistribute()


        if self.selectable:
            self.Selection()
            textbegin=self.contenty+20
            self.window.blit(self.font2.render(self.title, True, self.fontColor),(self.contentx+40, textbegin))
            textbegin+=40
            for i in range(len(self.texts)):
                if i==self.selection:
                    self.window.blit(self.font2.render(self.texts[i], True, self.selectedfontcolor),(self.contentx+40, textbegin)) 
                else:
                    self.window.blit(self.font3.render(self.texts[i], True, self.fontColor),(self.contentx+40, textbegin)) 
                textbegin+=30

            
        else:
            self.Information()
            textbegin=self.contenty+20
            if self.title!=None:
                self.window.blit(self.font2.render(self.title, True, self.fontColor),(self.contentx+40, textbegin))
                textbegin+=25
            for text in self.texts:
                self.window.blit(self.font3.render(text, True, self.fontColor),(self.contentx+40, textbegin))
                textbegin+=25

    def showbg(self):
        self.window.blit(self.bg, (self.contentx,
                                   self.contenty))
class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)) :
        self.window = window
        # 最基础的字体和背景图片设置
        self.font = pygame.font.Font(None, 40)
        self.font2= pygame.font.Font(None, 30)
        self.font3=pygame.font.Font(None,25)
        self.hpfont = pygame.font.Font(None, 15)
        self.hpfontcolor=(255,255,255)
        self.fontColor=(230,230,230)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.background), (BattleSettings.boxWidth, BattleSettings.boxHeight))


        # 初始化相关角色的参数，没有实际操作的权力
        self.player = player
        self.playeratk=player.ATK
        self.playerHP = player.HP
        self.playerinitialhp=player.HP

        
        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY
        
        self.monster = monster
        self.monsteratk=monster.ATK
        self.monsterHP = monster.HP
        self.monsterinitialhp=monster.HP

        
        self.monsterX = BattleSettings.monsterCoordX
        self.monsterY = BattleSettings.monsterCoordY

        #初始化玩家卡牌列表
        self.player_card_list=[Card(5,1,i) for i in range(6)]
        self.selected=[]
        self.monster_card_list=[Card(5,1,i) for i in range(3)]


        #动画，点击等图象变化的帧变量
        self.index=0
        self.images = [pygame.transform.scale(pygame.image.load(img), (BattleSettings.playerWidth, BattleSettings.playerHeight)) for img in GamePath.player]
        self.playerImg=self.images[self.index]
        self.playerImgrect=self.playerImg.get_rect()
        self.monsterimages = [pygame.transform.scale(pygame.image.load(img), (BattleSettings.monsterWidth, BattleSettings.monsterHeight)) for img in GamePath.monster]
        self.monsterImg=self.monsterimages[self.index]
        self.monsterImgrect=self.monsterImg.get_rect()
        self.pressed=0#mouse press detect
        self.leftround=15
        self.win=0
        self.ismyround=1
        self.atkgif=0
        self.actcuregif=0
        self.actlightninggif=0
        self.accumulateatkgifindex=0
        self.enemyactlightninggif=0
        self.roundchangeindex=0
        self.readytoleave=0
        self.retoreenergyindex=0
        self.enemyretoreenergyindex=0
        self.actrainatkindex=0
        self.gettinginfo=False
        self.hintindex=0
        #战斗过程数据变量
        self.atktimes=0
        self.Accumulated_atk=1
        self.Hp_change=0
        self.real_ATK=0
        self.level4atk=0
        self.mergetimes=0
        self.bestshot=0
        self.sacrificethistime=0
        self.enemyatktimes=0
        self.enemy_Accumulated_atk=1
        self.enemy_realatk=0
        self.enemy_round_count=1
        self.sacrificeatkthistime=0


    def DrawNewCard(self):
        for cards in self.player_card_list:
            if cards.sort==5:
                self.player_card_list=[cards.random_card(self.monster.type) if i==cards else i for i in self.player_card_list]
 
    def Seclect_Card(self):#detect mouse and append pointed cards into a list
        #get key events        
        mousepos=pygame.mouse.get_pos()
        #for trail: show mouse
        for cards in self.player_card_list:
        #select card by mouse
            if cards.sort!=5:
                if pygame.mouse.get_pressed()[0]==False:
                    self.pressed=1           
                if mousepos[0] >= cards.rect.x and mousepos[0]<cards.rect.x+120 and mousepos[1] >cards.rect.y  and mousepos[1]<620  :
                    if pygame.mouse.get_pressed()[0] and self.pressed==1:
                        if len(self.selected)<3 and cards not in self.selected:
                            self.selected.append(cards)
                            cards.rect.y=400

                            print("choose")
                        elif cards in self.selected:
                            self.selected.remove(cards)

                            cards.rect.y=420
                            print("dechoose")
                        self.pressed=0
                    else:
                        if len(self.selected)<3 and cards not in self.selected:
                            cards.rect.y=420
                elif cards not in self.selected:
                    cards.rect.y=440
                #cards.rendermycard(self.window)#second render for beauty

    def Mergecards(self):
        if self.mergetimes<3:
            keys=pygame.key.get_pressed()
            if len(self.selected)==2:
                if self.selected[0].sort==self.selected[1].sort and self.selected[0].level==self.selected[1].level and self.selected[0].level<4 and keys[pygame.K_SPACE]:
                    for cards in self.player_card_list:
                        print(cards.sort,cards.level,cards.order)
                    for cards in self.player_card_list:
                        if cards.order==self.selected[0].order:
                            cards.sort=5
                            cards.rect.y=440
                        elif cards.order==self.selected[1].order:
                            cards.level+=1
                            cards.rect.y=440
                    self.mergetimes+=1
                    del self.selected[1]
                    del self.selected[0]
                    for cards in self.player_card_list:
                        print(cards.sort,cards.level,cards.order)

    def curegif(self):#gif after player play cure cards
        if self.actcuregif>0 :
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (BattleSettings.playerWidth, BattleSettings.playerHeight)) for img in GamePath.cure]
            image = images[int((self.actcuregif//2)%3)]

            if self.actcuregif>40:
                self.actcuregif=0
            else:
                self.actcuregif+=1
            #render blood volume change
            text4 = "+ "+str(int((self.Hp_change)))
            self.window.blit(self.hpfont.render(text4, True, self.hpfontcolor),(BattleSettings.boxStartX+70+self.actcuregif//2,BattleSettings.boxStartY+10)) 
            self.window.blit(image, (BattleSettings.playerCoordX+10,BattleSettings.playerCoordY+10)) 
    def accumulategif(self):#gif of player's accumulate atk
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightshield]
        dizzy=30
        rotate=pygame.transform.rotate
        for i in range(int(self.Accumulated_atk//3)):
            imagee = images[(self.accumulateatkgifindex//2+1+i)%13]
            imagee=rotate(imagee,dizzy*i+10)
            self.window.blit(imagee, (BattleSettings.playerCoordX-30,BattleSettings.playerCoordY-30))
        if self.accumulateatkgifindex==16:
            self.accumulateatkgifindex=1
        else:
            self.accumulateatkgifindex+=1   

        if self.retoreenergyindex>0:
            text = "energy restored: "+str(int(self.Accumulated_atk))
            self.window.blit(self.font.render(text, True, (255,255,255)),(BattleSettings.boxStartX+30,BattleSettings.boxStartY+300)) 
            if self.retoreenergyindex>30:
                self.retoreenergyindex=0
            else:
                self.retoreenergyindex+=1
    def enemyaccumulategif(self):
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightshield]
        dizzy=30
        rotate=pygame.transform.rotate
        for i in range(int(self.enemy_Accumulated_atk//3.2)):
            imagee = images[(self.accumulateatkgifindex//2+1+i)%13]
            imagee=rotate(imagee,dizzy*i+10)
            self.window.blit(imagee,(BattleSettings.monsterCoordX-25,BattleSettings.monsterCoordY-25))
        if self.accumulateatkgifindex==16:
            self.accumulateatkgifindex=1
        else:
            self.accumulateatkgifindex+=1   

        if self.enemyretoreenergyindex>0:
            text = "energy restored: "+str(int(self.enemy_Accumulated_atk))
            self.window.blit(self.font.render(text, True, (255,255,255)),(BattleSettings.boxStartX+30,BattleSettings.boxStartY+70)) 
            if self.enemyretoreenergyindex>30:
                self.enemyretoreenergyindex=0
            else:
                self.enemyretoreenergyindex+=1

    def atk_gif(self):#gif after player's atk
        #lightning gif
        if self.actlightninggif>0:
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (200,184)) for img in GamePath.lightning]
            
            imagee = images[self.actlightninggif//4]
            
            self.window.blit(imagee, (BattleSettings.boxStartX+470,200))
            if self.actlightninggif==16:
                self.actlightninggif=0
            else:
                self.actlightninggif+=1
        # level4 unique: atk rain
        if self.level4atk>1:
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (170,340)) for img in GamePath.rainatk]
            
            imagee = images[self.atkgif%14]
            self.window.blit(imagee, (BattleSettings.boxStartX+730,150))

        if self.sacrificethistime==1:
            text = "SACRIFICE effect -10% hp"
            self.window.blit(self.font.render(text, True, (255,50,50)),(BattleSettings.boxStartX+170-self.atkgif,250)) 
        
        if self.sacrificeatkthistime==1:
            text3 = "SACRIFICE ATK -20% "
            print(self.atkgif)
            self.window.blit(self.font.render(text3, True, (255,25,55)),(BattleSettings.boxStartX+540+self.atkgif//2,BattleSettings.boxStartY+150)) 
            #atk effect: enemy hp reduce gif
        
        if self.real_ATK>0:
            for i in range(self.atktimes):
                text3 = "- "+str(int(self.real_ATK/(self.atktimes)))
                #print(self.real_ATK)
                self.window.blit(self.font.render(text3, True, (255,255,255)),(BattleSettings.boxStartX+640+self.atkgif+2*i,BattleSettings.boxStartY+250+40*i)) 
            if self.level4atk>1 :
                if self.atkgif<30:
                    text3 = "LEVEL4 ATK : "+str(int(self.level4atk))
                    self.window.blit(self.font.render(text3, True, (255,50,50)),(BattleSettings.boxStartX+220+self.atkgif+2*i,BattleSettings.boxStartY+100+40*i)) 
                else:
                    self.level4atk=0
        if self.level4atk>1:
            if self.atkgif>80:
                self.atkgif=0
                self.atktimes=0
            else:
                self.atkgif+=1
        else:
            if self.atkgif>40:
                self.atkgif=0
                self.atktimes=0
            else:
                self.atkgif+=1
        print(self.atkgif)
    def enemy_atk_gif(self):#gif after enemy's atk
        #lightning gif
        if self.actlightninggif>0:
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (200,184)) for img in GamePath.lightning]     
            imagee = images[self.actlightninggif%5]
            if self.actlightninggif>0:
                self.window.blit(imagee, (100,200))
            if self.actlightninggif==10:
                self.actlightninggif=0
            if self.actlightninggif>0:
                self.actlightninggif+=1
        #player hp reduce gif
        for i in range(self.enemyatktimes):
            text3 = "- "+str(int(self.enemy_realatk//(self.enemyatktimes)))
            if self.atkgif>0:
                self.window.blit(self.font.render(text3, True, (255,255,255)),(BattleSettings.boxStartX+170+self.atkgif+2*i,250+40*i)) 
        if self.enemy_Accumulated_atk>1:
            #print("built enemy accumlate data change in enemyatkgif")
            text = "energy restored "+str(int(self.enemy_Accumulated_atk))
            self.window.blit(self.font.render(text, True, (255,255,255)),(BattleSettings.boxStartX+430,BattleSettings.boxStartY+370)) 
        if self.atkgif>40:
            self.atkgif=0
            self.enemyatktimes=0
        if self.atkgif>0:
            self.atkgif+=1
    def Playcards(self):#trigger actchange fuction ,clean selected card list
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and len(self.selected)==3:
            self.act_my_changes()

            for card in self.player_card_list:
                for playedcards in self.selected:
                    if card.order==playedcards.order:
                        card.sort=5
                        card.image=card.images[card.sort]
                        card.rect.y+=40
                        self.selected.remove(card)    
       
    def act_my_changes(self):#change into stage 2        data adjust and trigger animate accordingly
        Hp_change=0
        real_ATK=0
        Accumulate_ATK=1
        #1 player data adjust

        for card in self.selected:
            if card.sort==0:#card=atk
                enhancement=[1.1,1.2,1.5,card.level4atk]
                real_ATK+=enhancement[card.level-1]
                self.atktimes+=1
                if card.level==4:
                    self.level4atk=card.level4atk
            if card.sort==1:#card=cure
                enhancement=[0.05,0.08,0.1,card.level4cure]
                Hp_change+=enhancement[card.level-1]
            if card.sort==2:#card=buff-accumulate atk
                enhancement=[1,1.5,2,card.level4buff]
                Accumulate_ATK+=enhancement[card.level-1]
            if card.sort==6:
                self.sacrificethistime+=4
                self.sacrificeatkthistime=1
                
        print(f"hpchange:{Hp_change}  realatk:{int(real_ATK)}  accumulated:{Accumulate_ATK}  player informationcheck")    
        if real_ATK!=0:#player atk number adjust and activate animate
            real_ATK=real_ATK*Accumulate_ATK*self.playeratk          
            if Accumulate_ATK>13:
                self.actlightninggif=1
            self.Accumulated_atk=1
        else:
            self.Accumulated_atk+=Accumulate_ATK
            self.retoreenergyindex=1
        if Hp_change>0:#player hp number adjust and activate animate
            self.Hp_change=self.playerinitialhp*Hp_change
            self.actcuregif=1
            if self.playerHP+self.Hp_change<self.playerinitialhp:
                self.playerHP+=self.Hp_change
            else:
                self.Hp_change=self.playerinitialhp-self.playerHP
                self.playerHP=self.playerinitialhp
        if self.sacrificethistime>0:
            if self.sacrificethistime==1:
                if self.playerHP-self.playerHP*0.2>0:
                    self.playerHP-=self.playerHP*0.2
                    self.atkgif=1
                    
                else:
                    self.playerHP=0


        #print(f"sacrifice contdown{self.sacrificenextime}")
        if self.sacrificeatkthistime==1:   
            if self.monsterHP-self.monsterHP*0.3>0:    
                self.monsterHP-=self.monsterHP*0.3
                self.atkgif=1
                print("atk thie time")
            else:
                self.monsterHP=0
        
    
        self.real_ATK=int(real_ATK)

        #2 enemy hp number adjust

        if self.monsterHP-real_ATK>0:
            self.monsterHP-=int(real_ATK)
        else:
            self.monsterHP=0
        if self.bestshot<int(real_ATK):
            self.bestshot=int(real_ATK)
        self.mergetimes=0
        self.ismyround=0 #change into stage 2
    def act_enemy_change(self):#change into stage 4
        real_atk=0
        Accumulate_ATK=1

        #1 enemy data adjust

        for card in self.monster_card_list:
            if card.sort==5:#initial enemy card list
                self.monster_card_list=[card.random_card_enemy(self.monster.type) if i==card else i for i in self.monster_card_list]
                                #cauculate card effect accordingly
        for card in self.monster_card_list:        
            if card.sort==0:#atk
                enhancement=[1.1,1.2,1.5]
                real_atk+=enhancement[card.level-1]
                self.enemyatktimes+=1
            elif card.sort==2:#buff
                enhancement=[1,2.3,3.4]
                Accumulate_ATK+=enhancement[card.level-1] 
        print(f"realatk:{real_atk}  accumulatedatk:{Accumulate_ATK}  in act enemy change")    
        if real_atk!=0:
            real_atk=real_atk*Accumulate_ATK*self.monsteratk       
            if Accumulate_ATK>10:
                self.actlightninggif=1#trigger lightning gif
            self.atkgif=1#trigger atk gif
            self.enemy_Accumulated_atk=1#reset accumulate atk
        else:
            self.enemy_Accumulated_atk+=Accumulate_ATK#restore accumulated atk

        
        #2player hp number adjust and activate animate
            
        self.enemy_realatk=int(real_atk)
        #print(self.enemy_realatk)
        if self.playerHP-real_atk>0:#player hp number adjust
            self.playerHP-=int(real_atk)
            self.leftround-=1
        else:
            self.playerHP=0

        self.ismyround=1#change into stage 4

    def animatedonechecker(self):
        if self.actcuregif==0 and self.actlightninggif==0 and self.enemyactlightninggif==0 and self.atkgif==0:
            return True
        else:
            return False
    def gifrender(self):#render stage2 and stage4

        if self.actcuregif>0:
            self.curegif()           
        if self.atkgif>0 or self.atktimes>0:
            self.atk_gif()
        if self.enemy_realatk>0:
            self.enemy_atk_gif()

        if self.ismyround==0 and self.enemy_round_count==0:

            #print(self.actcuregif,self.actlightninggif,self.atkgif,self.roundchangeindex)
            #trigger round change animate
            if self.actcuregif==0 and self.actlightninggif==0 and self.atkgif==0 and self.roundchangeindex==0:
                self.atktimes=0
                print("changeround")
                self.roundchangeindex=1

            #animating round change
            if self.roundchangeindex>0:
                #print(self.real_ATK,self.roundchangeindex)
                self.roundchange()
                if self.roundchangeindex==0:
                    self.enemy_round_count=1#change into stage 3

        if self.ismyround==1 and self.enemy_round_count==1:
            #trigger round change animate
            if self.actcuregif==0 and self.actlightninggif==0 and self.atkgif==0 and self.roundchangeindex==-1:
                self.roundchangeindex=1
            #animating round change
            if self.roundchangeindex>0:
                self.enemy_realatk=0
                self.enemyatktimes=0
                self.roundchange()
                if self.roundchangeindex==0:
                    self.enemy_round_count=0#change back into stage 1

    def roundchange(self):#change round animate
        bg=pygame.transform.scale(pygame.image.load(GamePath.dialog), (900, 200))
        b=pygame.font.SysFont("impact", 50)
        if self.ismyround==0:
            text = b.render("      Enemy round!",True,(20,0,0))
        if self.ismyround==1:
            text = b.render("      Your round!",True,(20,0,0))
        self.window.blit(bg, (BattleSettings.boxStartX+30,BattleSettings.boxStartY+170))
        self.window.blit(text,(BattleSettings.boxStartX+250,BattleSettings.boxStartY+240))
        if self.roundchangeindex<35:
            self.roundchangeindex+=1
        else:
            self.roundchangeindex=0

    def Win(self):
        self.player.hadbattle=1
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        bg=pygame.transform.scale(pygame.image.load(GamePath.winbg), (800, 390))
        b=pygame.font.SysFont("impact", 50)
        c=pygame.font.SysFont("impact", 30)
        self.window.blit(bg, (BattleSettings.boxStartX+30, BattleSettings.boxStartY+20))
        if self.monsterHP==0 and self.leftround>=0:
            text = b.render("You win! by " + str(10-self.leftround)+"rounds",True,(20,0,0))
            self.window.blit(text,(BattleSettings.boxStartX+300,BattleSettings.boxStartY+200))
            text2 = c.render(f"Your strongest shot : {self.bestshot}" ,False,(20,0,0))
            self.window.blit(text2,(BattleSettings.boxStartX+440,BattleSettings.boxStartY+290))

        elif self.monsterHP>0 and self.leftround<=0:
            text = b.render("You Lose by "+ str(10-self.leftround)+"rounds",True,(20,0,0))
            self.window.blit(text,(BattleSettings.boxStartX+250,BattleSettings.boxStartY+240))
            text2 = c.render(f"Your strongest shot : {self.bestshot}" ,False,(20,0,0))
            self.window.blit(text2,(BattleSettings.boxStartX+440,BattleSettings.boxStartY+290))

    def Getinfo(self):

        keys=pygame.key.get_pressed()


        if keys[pygame.K_SPACE] and len(self.selected)==1 :
            self.gettinginfo=True

        if self.gettinginfo==True and pygame.mouse.get_pressed()[0] :
            self.hintindex=0
            self.gettinginfo=False


        if self.gettinginfo==True:
            boxbeginx=BattleSettings.boxStartX
            boxbeginy= BattleSettings.boxStartY+150
            databg = pygame.Surface((960,300), pygame.SRCALPHA)
            databg.fill((100,100,100,250))
            self.window.blit(databg,(boxbeginx, boxbeginy))
            self.selected[0].rendermycard(self.window,boxbeginx+50, boxbeginy+50)
            if self.selected[0].sort==0:
                enhancement=[1.1,1.2,1.5,self.selected[0].level4atk]
                enhancement2=[1.1,1.2,1.5,"1~7"]
                realatk=self.playeratk*enhancement[self.selected[0].level-1]        
                titles=[ "Card Level:",
                        "Enhancement:" ,
                        "Initial ATK:" ,
                        "Brief:" ,
                        "Special:" ]
                contents=[str(self.selected[0].level),
                          str(enhancement2[self.selected[0].level-1]),
                          str(int(realatk)),
                          str("Reduce EnemyHp "),
                          str("None")]
            if self.selected[0].sort==1:
                enhancement=[0.5,0.8,1,self.selected[0].level4atk]
                enhancement2=["5%","8%","10%","10%~40%"]
                titles=[ "Card Level:",
                        "Brief:" ,
                        "Special:" ]
                contents=[str(self.selected[0].level),
                          str(f"Recover {enhancement2[self.selected[0].level-1]} Hp"),
                          str("None")]

            if self.selected[0].sort==2:
                enhancement=[1.2,1.5,2,self.selected[0].level4atk]
                enhancement2=["120%","150%","200%","100%~700%"]
                titles=[ "Card Level:",
                        "Buff Effect:" ,
                        "Brief:" ,
                        "Special:" ]
                contents=[str(self.selected[0].level),
                          str(enhancement2[self.selected[0].level-1]),
                          str("Store energy and can greatly improve next Atk "),
                          str("You can kept adding buff cards to accumulate"),
                          str("a huge shot")]
            if self.selected[0].sort==6:

                titles=["Brief:" ,
                        "",
                        "Special:" ]
                contents=[str("Immediately reduce '30%' of enemy's hp"),
                        str("With a cost of losing 20% hp 3rounds later"),
                        str("Sacrifice is one of the rarest card ,"),
                        str("its attack is strong and regardless of" ),
                        str("player's initial atk, if you are lucky enough to "),
                        str("have more than one sacrifice card, you can play"),
                        str("them in constant rounds to postpone sacrifice")]
 
 
            textbegin=boxbeginy+60
            for text in titles:
                self.window.blit(self.font2.render(text, True, self.fontColor),(boxbeginx+200, textbegin)) 
                textbegin+=30
            textbegin=boxbeginy+60
            for text in contents:
                self.window.blit(self.font2.render(text, True, self.fontColor),(boxbeginx+400, textbegin)) 
                textbegin+=30
            hint="Click to back battle"
            self.hintindex+=1
            if self.hintindex%25<16:
                self.window.blit(self.font3.render(hint, True, self.fontColor),(boxbeginx+750, boxbeginy+270)) 
    def Update_card(self):
        self.showbg()
        
        #render player's card
        for cards in self.player_card_list:
            cards.rendermycard(self.window,cards.rect.x,cards.rect.y)
        #render enemy's card
        if self.enemy_round_count==1:
            for cards in self.monster_card_list: #display cards
                cards.renderenemycard(self.window)
        #render accumulate gif
        if self.Accumulated_atk>1:
            self.accumulategif()
        if self.enemy_Accumulated_atk>1:
            self.enemyaccumulategif()

        if self.win==0 :#as long as no winner:

            #STAGE1 player selection and act effect
            if self.ismyround==1 and self.enemy_round_count==0 :
                #draw new card
                if self.gettinginfo==False:
                    self.Seclect_Card() # 1 select card in list by mouse
                    self.Getinfo()      # 2 get card information by "space"
                    self.Mergecards()   # 3 merge 2 cards by "space"
                    self.Playcards()    # 4 play 3 cards selceted by "space"
                else:
                    self.Getinfo()

            #STAGE2 player's animations
            if self.ismyround==0 and self.enemy_round_count==0:
                self.gifrender()

            #STAGE3 enemy's selection and act effect
            if self.ismyround==0 and self.enemy_round_count==1:
                self.act_enemy_change()
                self.Hp_change=0
                self.real_ATK=0
                self.sacrificeatkthistime=0
                if self.sacrificethistime==1:
                    self.sacrificethistime=0


            #STAGE4 enemy's animations
            if self.ismyround==1 and self.enemy_round_count==1 :
                self.gifrender()
                #two ways to enter next round
                mousepress=pygame.mouse.get_pressed()#detect change from enemy round to my round
                keys=pygame.key.get_pressed()
                if self.animatedonechecker():
                    if mousepress[0] or keys[pygame.K_SPACE]:
                        print("detected stage4-stage1 in updatecard")                           
                        self.monster_card_list=[Card(5,1,i) for i in range(3)]
                        self.roundchangeindex=-1
                        self.DrawNewCard()

                        if self.sacrificethistime>0:
                            self.sacrificethistime-=1

            #STAGE: one round finished

        if self.monsterHP==0 or self.playerHP==0 or self.leftround==0:#determin whether win
            self.win=1
            self.Win()
            mousepress=pygame.mouse.get_pressed()#detect change from enemy round to my round
            if mousepress[0]:
                self.readytoleave=1

        if self.index==119:
            self.index=0
        else:
            self.index+=1


        #display mouse to see whether the program working correctly

        mousepos=pygame.mouse.get_pos()
        pygame.draw.circle(self.window, (100,0,0), (mousepos[0],mousepos[1]),5, width=0)

    def showbg(self):

        self.playerImg=self.images[self.index]
        self.monsterImg=self.monsterimages[4*int((self.index//12)%4)]
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        transparent_rect = pygame.Surface((960, 250), pygame.SRCALPHA)
        transparent_rect.fill((0, 0,0, 140))

        databg = pygame.Surface((960,100), pygame.SRCALPHA)
        databg.fill((200,200,200,100))
        self.window.blit(databg,(BattleSettings.boxStartX, BattleSettings.boxStartY))
        self.window.blit(self.playerImg, (self.playerX,
                                          self.playerY))
        self.window.blit(self.monsterImg, (self.monsterX,
                                           self.monsterY))
        #render general information:
        #1 render player hp
        pygame.draw.rect(self.window,(120,20,20), (BattleSettings.boxStartX+20,BattleSettings.boxStartY+10,300,10),0,border_radius=3 )
        pygame.draw.rect(self.window,(240,60,60), (BattleSettings.boxStartX+20,BattleSettings.boxStartY+10,self.playerHP/self.playerinitialhp*300,10),0,border_radius=3 )
        #2 render enmey hp
        pygame.draw.rect(self.window,(120,20,20), (BattleSettings.boxStartX+500,BattleSettings.boxStartY+10,400,10),0,border_radius=3)
        pygame.draw.rect(self.window,(240,60,60), (BattleSettings.boxStartX+500,BattleSettings.boxStartY+10,self.monsterHP/self.monsterinitialhp*400,10),0,border_radius=3)
        text1 = str(int(self.monsterHP))
        self.window.blit(self.hpfont.render(text1, True, self.hpfontcolor),(BattleSettings.boxStartX+530,BattleSettings.boxStartY+10)) 
        text2 = str(int(self.playerHP))
        self.window.blit(self.hpfont.render(text2, True, self.hpfontcolor),(BattleSettings.boxStartX+50,BattleSettings.boxStartY+10))
        #3 render left rounds and atk accumulation:


        text = "Accumulated ATK: " + str(int(self.Accumulated_atk))+"00%"
        self.window.blit(self.font2.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+20, BattleSettings.boxStartY+30)) 

        text = "Left round: " + str(self.leftround)
        if self.leftround>3:
            self.window.blit(self.font2.render(text, True, self.fontColor),
            (BattleSettings.boxStartX+250, BattleSettings.boxStartY+60))
        else:
            self.window.blit(self.font2.render(text, True, (255,20,20)),
            (BattleSettings.boxStartX+250, BattleSettings.boxStartY+60))

        text = "My Origin ATK: " + str(int(self.playeratk))
        self.window.blit(self.font2.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+20, BattleSettings.boxStartY+60)) 
        if self.sacrificethistime>0:
            text = "SACRIFICE effect in " + str(self.sacrificethistime-1)+"rounds"
            self.window.blit(self.font2.render(text, True, (230,40,40)),(BattleSettings.boxStartX+20, BattleSettings.boxStartY+110)) 

        text = "Accumulated ATK: " + str(int(self.enemy_Accumulated_atk))+"00%"
        self.window.blit(self.font2.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+520, BattleSettings.boxStartY+30)) 

        text = "Enemy Origin ATK: " + str(int(self.monsteratk))
        self.window.blit(self.font2.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+520, BattleSettings.boxStartY+60)) 
class ShoppingBox:
    def __init__(self, window,player,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (20,20,20,200)):
        self.image=[pygame.transform.scale(pygame.image.load(img), (220,220)) for img in GamePath.npcgif]
        self.index3=0
        pygame.transform.flip(self.image[self.index3], True, False)#needs to be fixed
        self.window = window
        self.transparent_rect = pygame.Surface((960, 80), pygame.SRCALPHA)
        self.transparent_rect.fill((200, 200,200, 140))
        self.images=[pygame.transform.scale(pygame.image.load(img), (80,100)) for img in GamePath.store]
        self.eggimg=[pygame.transform.scale(pygame.image.load(img), (100,100)) for img in GamePath.egg]
        self.index=0
        self.player=player
        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY-70
        # 最基础的字体和背景图片设置
        self.font = pygame.font.Font(None, 50)
        self.font2= pygame.font.Font(None, 40)
        self.font3=pygame.font.Font(None,33)
        self.hpfont = pygame.font.Font(None, 15)
        self.hpfontcolor=(255,255,255)
        self.fontColor=(255,255,255)
        self.selectedfontcolor=(255,100,100)
        self.doneshopping=0
        self.bg = pygame.Surface((BattleSettings.boxWidth,
            BattleSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        self.selection=0
        self.hintindex=0
        self.pressing=0
        self.pressingw=0
        self.index2=-20
        self.title= "WHAT DO YOU NEED?"
        self.texts=[ f"Initial ATK + 0.5:  {self.player.price1}$",
        f"Iinitial HP + 5:      {self.player.price2}$",
        f"Animal egg + 1:       {self.player.price3}$",
        ]
        self.imgx=BattleSettings.boxStartX+250
        self.imgy=BattleSettings.boxStartY+150
        self.selectionrect = pygame.Surface((600,100), pygame.SRCALPHA)
        self.selectionrect.fill((160,160,160,200))
        self.start=[BattleSettings.boxStartY+150,BattleSettings.boxStartY+270,BattleSettings.boxStartY+390]

    def buy(self):
        if self.selection==0:
            if self.player.money-self.player.price1>0:
                self.player.money-=self.player.price1
                self.player.price1+=30
                self.player.ATK+=0.5
        if self.selection==1:
            if self.player.money-self.player.price2>0:
                self.player.money-=self.player.price2
                self.player.price2+=30
                self.player.HP+=5
        if self.selection==2:
            if self.player.money-self.player.price3>0:
                self.player.money-=self.player.price3
                self.player.egg+=1


        self.texts=[ f"Initial ATK + 0.5:  {self.player.price1}$",
        f"Iinitial HP + 5:      {self.player.price2}$",
        f"Animal egg + 1:       {self.player.price3}$",
        ]

    def update_dialog(self):
        self.showbg()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_s]==False:
            self.pressing=0
        if keys[pygame.K_s] and self.pressing==0:
            if self.selection>=2:
                self.selection=0
            else:
                self.selection+=1
            self.pressing=1
        if keys[pygame.K_w]==False:
            self.pressingw=0
        if keys[pygame.K_w] and self.pressingw==0:
            if self.selection==0:
                self.selection=2
            else:
                self.selection-=1
            self.pressingw=1
        if keys[pygame.K_SPACE]==False:
            self.pressings=0
        if keys[pygame.K_SPACE] and self.pressings==0:
            self.chosing=1
            self.pressings=1
            self.buy()

        #leave dialog
        if pygame.mouse.get_pressed()[0]:
            self.doneshopping=1
        #hint
        hint="CLICK to back home  PRESS to perchase"

        self.window.blit(self.font3.render(hint, True, self.fontColor),(self.imgx+250, self.start[2]+110))
    def showbg(self):
        if self.index3==236:
            self.index3=0
        else:
            self.index3+=1
        if self.index==31:
            self.index=0
        else:
            self.index+=1
        if self.index2==20:
            self.index2=-20
        else:
            self.index2+=1
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))

        self.window.blit(self.transparent_rect, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        b=abs(self.index2*10)
        self.selectionrect.fill((160,160,160,b))

        self.window.blit(self.selectionrect,(self.imgx-10,self.start[self.selection]))
        pygame.transform.flip(self.image[self.index3//4], True, False)
        self.window.blit(self.image[self.index3//4], (self.playerX,
                                          self.playerY+150))
        self.window.blit(self.images[0], (self.imgx,
                                          self.start[0]))
        self.window.blit(self.images[1], (self.imgx,
                                          self.start[1]))
        self.window.blit(self.eggimg[self.index%4], (self.imgx,
                                          self.start[2]))

        self.window.blit(self.font.render(self.title, True, self.fontColor),(self.imgx+50, self.imgy-50))
        for i in range(len(self.texts)):
            self.window.blit(self.font2.render(self.texts[i], True, self.fontColor),(self.imgx+130, self.start[i]+38)) 
        
        
        
        text = "LeftMoney: " + str(self.player.money)
        self.window.blit(self.font3.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+20, BattleSettings.boxStartY+30)) 

        text = "My initial ATK: " + str(int(self.player.ATK))
        self.window.blit(self.font3.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+270, BattleSettings.boxStartY+30)) 

        text = "My initial HP: " + str(int(self.player.HP))
        self.window.blit(self.font3.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+520, BattleSettings.boxStartY+30)) 

        text = "My egg: " + str(int(self.player.egg))
        self.window.blit(self.font3.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+770, BattleSettings.boxStartY+30)) 