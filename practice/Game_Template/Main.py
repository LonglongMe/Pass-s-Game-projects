# -*- coding:utf-8 -*-
import sys
import pygame
from GameManager import GameManager
from Settings import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))
    pygame.display.set_caption(WindowSettings.name)

    manager = GameManager(window)
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 传送
            if event.type == GameEvent.EVENT_SWITCH:
                manager.flush_scene()
        manager.update()
        manager.render()
        pygame.display.flip()

if __name__ == "__main__":
    main()