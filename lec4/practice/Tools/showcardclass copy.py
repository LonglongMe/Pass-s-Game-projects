import pygame
import sys
fontlist=pygame.font.get_fonts()
card_backround_list=[r"./assets/cards/ATK.jpg",
                    r"./assets/cards/CURE.jpg",
                    r"./assets/cards/BUFF.jpg",
                    r"./assets/cards/PURE.jpg",
                    r"./assets/cards/DEBUFF.jpg",
                    r"./assets/cards/EMPTY.png"]
card_image_list=[]
game_background_list=[]
effect_animate=[]

class cardnum:
    "ATK"==0
    "CURE"==1
    "BUFF"==2
    "PURE"==3
    "DEBUFF"==4
    "EMPTY"==5

for i in range(6):                     
    card_backround=pygame.image.load(card_backround_list[i])
    card_backround = pygame.transform.scale(card_backround, (120, 180))
    card_image_list.append(card_backround)
game_backround=pygame.image.load(card_backround_list[i])
game_backround = pygame.transform.scale(card_backround, (120, 180))
class card():
    fliped=[]
    pressed=0

    def __init__(self,sort,level,window,order):

        self.sort=sort
        self.level=level
        self.x=30+(order-1)*130
        self.y=350
        self.window=window
        self.order=order
        

    def show_card(self):
        if self.level==1:
            content_color = (50,130, 250,140)
        if self.level==2:
            content_color=(150,15,160,180)
        if self.level==3:
            content_color=(180,15,10,210)
    
        margin_color=(45,70,130)

        width = 5
       
        d=pygame.font.SysFont(fontlist[6], 15)
        card.choose_Card(self)
        for x in card.fliped:
            if self.order==x:
                self.y-=40
        position = ( self.x+width-2, self.y+width-1, 124, 182 )
        self.window.blit(card_image_list[self.sort],(self.x+width,self.y+width))
        transparent_rect = pygame.Surface((120, 73), pygame.SRCALPHA)
        transparent_rect.fill(content_color)
        self.window.blit(transparent_rect, (self.x+5, self.y+110))
        pygame.draw.rect( self.window, margin_color, position, width,border_radius=9 )
    def choose_Card(self):
        mousepos=pygame.mouse.get_pos()
        pygame.draw.rect( self.window, (100,0,0), (mousepos[0],mousepos[1],10,10), 0)
        if pygame.mouse.get_pressed()[0]==False:
            card.pressed=1
            
        if mousepos[0] >= self.x and mousepos[0]<self.x+120 and mousepos[1] >self.y  and mousepos[1]<self.y+180  and pygame.mouse.get_pressed()[0] and card.pressed==1:

            if len(card.fliped)<3 and self.order not in card.fliped:
                card.fliped.append(self.order)
            elif self.order in card.fliped:
                card.fliped.remove(self.order)
            card.pressed=0


        print(card.fliped)




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

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.showbg()
        m=0
        a=card(m,1,window,1)
        a.show_card()
        b=card(m,2,window,2)
        b.show_card()
        c=card(m,3,window,3)
        c.show_card()
        d=card(m,1,window,4)
        d.show_card()
        e=card(m,2,window,5)
        e.show_card()
        f=card(m,3,window,6)
        f.show_card()

        pygame.display.flip()

if __name__ == "__main__":
    run_game()

