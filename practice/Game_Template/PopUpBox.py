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
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        

class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)) :
        self.window = window
        # 最基础的字体和背景图片设置
        self.font = pygame.font.Font(None, 40)
        self.hpfont = pygame.font.Font(None, 15)
        self.hpfontcolor=(255,255,255)
        self.fontColor=(0,0,0)

        self.bg = pygame.Surface((BattleSettings.boxWidth,
            BattleSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)

        # 初始化相关角色的参数，没有实际操作的权力
        self.player = player
        self.playeratk=player.ATK
        self.playerHP = player.HP
        self.playerinitialhp=player.HP
        self.playerImg = pygame.transform.scale(player.image, 
            (BattleSettings.playerWidth, BattleSettings.playerHeight))
        
        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY
        
        self.monster = monster
        self.monsteratk=monster.ATK
        self.monsterHP = monster.HP
        self.monsterinitialhp=monster.HP
        self.monsterImg = pygame.transform.scale(monster.image, 
            (BattleSettings.monsterWidth, BattleSettings.monsterHeight))
        
        self.monsterX = BattleSettings.monsterCoordX
        self.monsterY = BattleSettings.monsterCoordY

        #初始化玩家卡牌列表
        self.player_card_list=[Card(5,1,i) for i in range(6)]
        self.selected=[]
        self.monster_card_list=[Card(5,1,i) for i in range(3)]


        #动画，点击等图象变化的帧变量
        self.pressed=0#mouse press detect
        self.leftround=10
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
        #战斗过程数据变量
        self.atktimes=0
        self.Accumulated_atk=1
        self.Hp_change=0
        self.real_ATK=0

        self.enemyatktimes=0
        self.enemy_Accumulated_atk=1
        self.enemy_realatk=0
        self.enemy_round_count=0


    def DrawNewCard(self):
        for cards in self.player_card_list:
            if cards.sort==5:
                self.player_card_list=[cards.random_card() if i==cards else i for i in self.player_card_list]
 
    def Seclect_Card(self):#detect mouse and append pointed cards into a list
        #get key events        
        mousepos=pygame.mouse.get_pos()
        #for trail: show mouse

        for cards in self.player_card_list:
        #select card by mouse
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
            cards.rendermycard(self.window)#second render for beauty




                #print(self.selected)
    def curegif(self):#gif after player play cure cards
        if self.actcuregif>0 :
            images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth-50, PlayerSettings.playerHeight)) for img in GamePath.cure]
            image = images[self.actcuregif%3]
            if self.actcuregif>20:
                self.actcuregif=0
            else:
                self.actcuregif+=1
            #render blood volume change
            text4 = "+ "+str((self.Hp_change))
            self.window.blit(self.hpfont.render(text4, True, self.hpfontcolor),(BattleSettings.boxStartX+70+self.actcuregif//2,BattleSettings.boxStartY+10)) 
            self.window.blit(image, (BattleSettings.boxStartX+100,BattleSettings.boxStartY+200)) 
    def accumulategif(self):#gif of player's accumulate atk
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightshield]
        for i in range(int(self.Accumulated_atk//2)):
            imagee = images[(self.accumulateatkgifindex//2+1+i)%9]
            self.window.blit(imagee, (BattleSettings.boxStartX+28,200))
        if self.accumulateatkgifindex==16:
            self.accumulateatkgifindex=1
        else:
            self.accumulateatkgifindex+=1   

        if self.retoreenergyindex>0:
            text = "energy restored: "+str(int(self.Accumulated_atk))
            self.window.blit(self.font.render(text, True, (255,255,255)),(BattleSettings.boxStartX+30,BattleSettings.boxStartY+70)) 
            if self.retoreenergyindex>30:
                self.retoreenergyindex=0
            else:
                self.retoreenergyindex+=1
    def enemyaccumulategif(self):
        images = [pygame.transform.scale(pygame.image.load(img), 
                        (200,184)) for img in GamePath.lightshield]
        for i in range(int(self.Accumulated_atk//2)):
            imagee = images[(self.accumulateatkgifindex//2+1+i)%9]
            self.window.blit(imagee, (BattleSettings.boxStartX+478,200))
        if self.accumulateatkgifindex==16:
            self.accumulateatkgifindex=1
        else:
            self.accumulateatkgifindex+=1   

        if self.enemyretoreenergyindex>0:
            text = "energy restored: "+str(int(self.Accumulated_atk))
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
            
            imagee = images[self.actlightninggif//2]
            
            self.window.blit(imagee, (BattleSettings.boxStartX+470,200))
            if self.actlightninggif==8:
                self.actlightninggif=0
            else:
                self.actlightninggif+=1
            #atk effect: enemy hp reduce gif
        for i in range(self.atktimes):
            text3 = "- "+str(int(self.real_ATK//(self.atktimes)))
            self.window.blit(self.font.render(text3, True, (255,255,255)),(BattleSettings.boxStartX+730+self.atkgif+2*i,BattleSettings.boxStartY+250+40*i)) 
        if self.atkgif>40:
            self.atkgif=0
            self.atktimes=0
        else:
            self.atkgif+=1
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
            print("built enemy accumlate data change in enemyatkgif")
            text = "energy restored "+str(int(self.enemy_Accumulated_atk))
            self.window.blit(self.font.render(text, True, (255,255,255)),(BattleSettings.boxStartX+430,BattleSettings.boxStartY+70)) 
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
        Accumulate_ATK=self.Accumulated_atk

        #1 player data adjust

        for card in self.selected:
            if card.sort==0:#card=atk
                enhancement=[1.1,1.2,1.5]
                real_ATK+=enhancement[card.level-1]
                self.atktimes+=1
            if card.sort==1:#card=cure
                enhancement=[0.1,0.2,0.3]
                Hp_change+=enhancement[card.level-1]
            if card.sort==2:#card=buff-accumulate atk
                enhancement=[1,2.3,3.4]
                Accumulate_ATK+=enhancement[card.level-1]
        print(f"hpchange:{Hp_change}  realatk:{int(real_ATK)}  accumulated:{Accumulate_ATK}  player informationcheck")    
        if real_ATK!=0:#plaer atk number adjust and activate animate
            real_ATK=real_ATK*Accumulate_ATK*self.playeratk          
            if Accumulate_ATK>13:
                self.actlightninggif=1
            self.Accumulated_atk=1
        else:
            self.Accumulated_atk+=Accumulate_ATK
            self.retoreenergyindex=1
        if Hp_change>0:#plaer hp number adjust and activate animate
            self.Hp_change=self.playerinitialhp*Hp_change
            self.actcuregif=1
            if self.playerHP+self.Hp_change<self.playerinitialhp:
                self.playerHP+=self.Hp_change
            else:
                self.Hp_change=self.playerinitialhp-self.playerHP
                self.playerHP=self.playerinitialhp



        self.real_ATK=int(real_ATK)

        #2 enemy hp number adjust

        if self.monsterHP-real_ATK>0:
            self.monsterHP-=int(real_ATK)
        else:
            self.monsterHP=0
        
        self.ismyround=0 #change into stage 2
    def act_enemy_change(self):#change into stage 4
        
        real_atk=0
        Accumulate_ATK=self.enemy_Accumulated_atk

        #1 enemy data adjust

        for card in self.monster_card_list:
            if card.sort==5:#initial enemy card list
                self.monster_card_list=[card.random_card_enemy() if i==card else i for i in self.monster_card_list]
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
            self.enemy_Accumulated_atk=Accumulate_ATK#restore accumulated atk

        
        #2player hp number adjust and activate animate
            
        self.enemy_realatk=int(real_atk)
        print(self.enemy_realatk)
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
        if self.atktimes>0:
            self.atk_gif()
        if self.enemy_realatk>0:
            self.enemy_atk_gif()


        if self.ismyround==0 and self.enemy_round_count==0:

            #print(self.actcuregif,self.actlightninggif,self.atkgif,self.roundchangeindex)
            #trigger round change animate
            if self.actcuregif==0 and self.actlightninggif==0 and self.atkgif==0 and self.roundchangeindex==0:
                print("changeround")
                self.roundchangeindex=1
                #reset public data
                self.real_ATK=0
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
        bg=pygame.transform.scale(pygame.image.load(GamePath.dialog), (900, 200))
        b=pygame.font.SysFont("impact", 50)
        if self.monsterHP==0 and self.leftround>=0:
            text = b.render("You win! in " + str(20-self.leftround)+"rounds",True,(20,0,0))
        elif self.monsterHP>0 and self.leftround<=0:
            text = b.render("You Lose by "+ str(20-self.leftround)+"rounds",True,(20,0,0))

        self.window.blit(bg, (BattleSettings.boxStartX+30, BattleSettings.boxStartY+170))
        self.window.blit(text,(BattleSettings.boxStartX+250,BattleSettings.boxStartY+240))

    def Update_card(self):
        self.showbg()
        #render player's card
        for cards in self.player_card_list:
            cards.rendermycard(self.window)
        #render enemy's card
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
                self.DrawNewCard()#draw new card
                self.Seclect_Card()# 1 select card in list by mouse
                self.Playcards()# 2 play 3 cards selceted by "space"

            #STAGE2 player's animations
            if self.ismyround==0 and self.enemy_round_count==0:
                self.gifrender()

            #STAGE3 enemy's selection and act effect
            if self.ismyround==0 and self.enemy_round_count==1:
                self.act_enemy_change()
                self.Hp_change=0

            #STAGE4 enemy's animations
            if self.ismyround==1 and self.enemy_round_count==1 :
                self.gifrender()
                mousepress=pygame.mouse.get_pressed()#detect change from enemy round to my round
                if mousepress[0] and self.animatedonechecker():
                    print("detected stage4-stage1 in updatecard")                           
                    self.monster_card_list=[Card(5,1,i) for i in range(3)]
                    self.roundchangeindex=-1

            #STAGE: one round finished

        if self.monsterHP==0 or self.playerHP==0 or self.leftround==0:#determin whether win
            self.win=1
            self.Win()
            mousepress=pygame.mouse.get_pressed()#detect change from enemy round to my round
            if mousepress[0]:
                self.readytoleave=1



        #display mouse to see whether the program working correctly

        mousepos=pygame.mouse.get_pos()
        pygame.draw.circle(self.window, (100,0,0), (mousepos[0],mousepos[1]),5, width=0)

    def showbg(self):
        #bg=pygame.transform.scale(pygame.image.load(GamePath.background), (960, 540))
        #self.window.blit(bg, (0, 0))
        #self.gradient_fill_rect(self.window, (0,350,960,250), (0,0,0,140), (0,0,0,255))
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        transparent_rect = pygame.Surface((960, 250), pygame.SRCALPHA)
        transparent_rect.fill((0, 0,0, 140))
        #self.window.blit(transparent_rect, (BattleSettings.boxStartX, 200+ BattleSettings.boxStartY))
        databg = pygame.Surface((960,100), pygame.SRCALPHA)
        databg.fill((200,200,200,100))
        self.window.blit(databg,(BattleSettings.boxStartX, BattleSettings.boxStartY))
        self.window.blit(self.playerImg, (self.playerX,
                                          self.playerY))
        self.window.blit(self.monsterImg, (self.monsterX,
                                           self.monsterY))
                #render general information:
        #1 render player hp
        pygame.draw.rect(self.window,(240,60,60), (BattleSettings.boxStartX+20,BattleSettings.boxStartY+10,self.playerHP/self.playerinitialhp*300,10),0,border_radius=5 )
        #2 render enmey hp
        pygame.draw.rect(self.window,(240,60,60), (BattleSettings.boxStartX+500,BattleSettings.boxStartY+10,self.monsterHP/self.monsterinitialhp*400,10),0,border_radius=5)
        text1 = str(int(self.monsterHP))
        self.window.blit(self.hpfont.render(text1, True, self.hpfontcolor),(BattleSettings.boxStartX+530,BattleSettings.boxStartY+10)) 
        text2 = str(int(self.playerHP))
        self.window.blit(self.hpfont.render(text2, True, self.hpfontcolor),(BattleSettings.boxStartX+50,BattleSettings.boxStartY+10))
        #3 render left rounds and atk accumulation:


        text = "Accumulated ATK: " + str(int(self.Accumulated_atk))
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+20, BattleSettings.boxStartY+30)) 

        text = "Left round: " + str(self.leftround)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+20, BattleSettings.boxStartY+60))

        text = "Accumulated ATK: " + str(int(self.enemy_Accumulated_atk))
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.boxStartX+520, BattleSettings.boxStartY+30)) 

class ShoppingBox:
    def __init__(self, window, npc, player,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def buy(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
