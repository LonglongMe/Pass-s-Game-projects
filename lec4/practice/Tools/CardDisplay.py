import pygame

import sys

card_backround_list=[r"./assets/cards/ATK.png"
                    r"./assets/cards/Cure.png" 
                    r"./assets/cards/Buff.png"
                    r"./assets/cards/Pure.png"
                    r"./assets/cards/Debuff.png"
                    r"./assets/cards/Ban.png"
                    r"./assets/cards/Empty.png"]
card_image_list=[]
for i in range(7):                     
    card_backround=pygame.image.load(card_backround_list[i])
    card_backround = pygame.transform.scale(card_backround, (99, 140))
    card_image_list.append(card_backround)
a=pygame.font.get_fonts()
def DrawRect(screen,x,y):
    margincolcor = (208, 242, 203)
    contentcolor=(170,180,250)
    position = ( x, y, 100, 170 )
    width = 5
    position = ( x+width, y+width, 100, 170 )
    
    screen.blit(card_backround,(x+width,y+width))

    transparent_rect = pygame.Surface((200, 100), pygame.SRCALPHA)
    transparent_rect.fill((0, 0,0, 140))



    pygame.draw.rect( screen, contentcolor, (x+5,y+135,100,35), 0 ,border_radius=6 )
    #draw card's margin
    pygame.draw.rect( screen, margincolcor, position, width,border_radius=6 )
    #draw card's content
    
    b=pygame.font.SysFont(a[14], 25)
    c=pygame.font.SysFont(a[17], 24)
    d=pygame.font.SysFont(a[6], 15)
    text = b.render("ATK",True,(20,0,0))
    textdamage=c.render("DAMAGE",False,(20,0,0))
    textatkorigin=d.render("Origin ATK",False,(20,0,0))
    textatkorigin2=d.render(" 110%",False,(20,0,0))
    screen.blit(text,(x+2*width,y+2*width))
    screen.blit(textdamage,(x+2*width+2,y+2*width+90))
    screen.blit(textatkorigin,(x+2*width+2,y+2*width+127))
    screen.blit(textatkorigin2,(x+2*width+2,y+2*width+142))
   
def run_game():
    pygame.init()
    window = pygame.display.set_mode((960,540))


    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(6):
            DrawRect(window,5+110*i,540-170-20)
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
