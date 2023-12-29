# -*- coding:utf-8 -*-

import pygame
import sys

from SceneManager import SceneManager
from Settings import *
from Player import Player

class MainGame:
    window=None
    player=None

    def run_game():
        pygame.init()

        MainGame.window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))
        pygame.display.set_caption(WindowSettings.name)

        scene = SceneManager(MainGame.window)

        # 创建角色，sprites暂时写在这里
        sprites = pygame.sprite.Group()
        MainGame.player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
        sprites.add(MainGame.player)
       

        # 游戏主循环
        while True:
            scene.tick(30)  # 控制帧率

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 获取按键状态
            keys = pygame.key.get_pressed()

            # 更新Player
            MainGame.player.update(keys, scene)
            scene.update_camera(MainGame.player)
        
            # 渲染场景
            scene.render()

            # 渲染player
            MainGame.player.show()
            MainGame.window.blit(MainGame.player.image,MainGame.player.rect)
           # sprites.draw(window)

            pygame.display.flip()

if __name__=="__main__":
    
    MainGame.run_game()
