# -*- coding:utf-8 -*-

import pygame
import sys
from Map import Fire
from Card import Card ,CardSet
from SceneManager import SceneManager
from Settings import *
from Player import Player

def run_game():
    pygame.init()

    window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))
    pygame.display.set_caption(WindowSettings.name)

    scene = SceneManager(window)
    firegif=Fire(1,40*3,40*8)
    # 创建角色 和 NPC 精灵
    player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
    clock = pygame.time.Clock()
    # 创建牌库
    cards=[Card(5,1,i) for i in range(6)]
    Handset=CardSet(cards,window)
    # 游戏主循环
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 获取按键状态
        keys = pygame.key.get_pressed()

        # 更新 NPC / Player
        player.update(keys, scene)    # 主要是角色移动
        scene.update()                # 主要是场景中对象的动画更新，暂时不涉及player的部分
        Handset.Update_card()
        # talking 的render 必须要在scene render以后，不然会被背景盖掉
        scene.render()                
        player.draw(window)
        firegif.draw(window)

        scene.check_event_talking(player, keys)
        scene.check_event_battle(player, keys)
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
