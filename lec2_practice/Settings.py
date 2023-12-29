# -*- coding:utf-8 -*-
import pygame
from enum import Enum

class WindowSettings:
    name = "Thgink Luos Ton"
    width = 1280
    height = 720
    outdoorScale = 1.5 # A necessary scale to allow camera movement in outdoor scenes

class PlayerSettings:
    playerSpeed = 10
    playerWidth = 120
    playerHeight = 133

class SceneSettings:
    tileXnum = 48
    tileYnum = 27
    tileWidth = tileHeight = 40

class GamePath:
    player = []
    for i in range(1,122):
        a=(pygame.image.load(f"./lec2_practice/assets/player/Paimon/{i}.png"))
        player.append(pygame.transform.scale(a,(PlayerSettings.playerWidth, PlayerSettings.playerHeight)))

    groundTiles = []
    for i in range(1,7):
        a=(pygame.image.load(f"./lec2_practice/assets/tiles/ground{i}.png"))
        groundTiles.append(pygame.transform.scale(a,(SceneSettings.tileWidth, SceneSettings.tileHeight)))


    tree = r".lec2_practice/assets/tiles/tree.png"

class GameState(Enum):
    MAIN_MENU = 1
    GAME_LOADING = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6