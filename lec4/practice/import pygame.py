import pygame
import pygame.gfxdraw
from pygame.locals import *

def gradient_fill_rect(screen, rect, start_color, end_color):
    start_color = pygame.Color(start_color)
    end_color = pygame.Color(end_color)

    pygame.gfxdraw.hgradient(screen, rect.left, rect.top, rect.width, rect.height, start_color, end_color)

pygame.init()
screen = pygame.display.set_mode((400, 300))
rect = pygame.Rect(100, 100, 200, 100)
start_color = "blue"
end_color = "green"

gradient_fill_rect(screen, rect, start_color, end_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
