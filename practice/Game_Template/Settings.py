# -*- coding:utf-8 -*-

from enum import Enum
import pygame

class WindowSettings:
    name = "Thgink Luos"
    width = 1280
    height = 720
    outdoorScale = 1.5 # A necessary scale to allow camera movement in outdoor scenes

class SceneSettings:
    tileXnum = 36#48 # 64
    tileYnum = 19#27 # 36
    tileWidth = tileHeight = 40

class PlayerSettings:
    # Initial Player Settings
    playerSpeed = 7
    playerWidth = 60
    playerHeight = 55
    playerHP = 20
    playerAttack = 5
    playerDefence = 1
    playerMoney = 100

class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60

class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3
    

class BossSettings:
    width = 300
    height = 300
    coordX = (SceneSettings.tileXnum / 2) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2

class SceneType(Enum):
    HOME = 1
    WILD = 2
    BOSS = 3
    MENU = 4

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class BattleSettings:
    boxWidth = WindowSettings.width * 3 // 4 
    boxHeight = WindowSettings.height * 3 // 4 
    boxStartX = WindowSettings.width // 8           # Coordinate X of the box
    boxStartY = WindowSettings.height // 8
    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 
    textPlayerStartX = WindowSettings.width // 4          # Coordinate X of the first line of dialog
    textMonsterStartX = WindowSettings.width // 2 +100   
    textStartY = WindowSettings.height // 3         # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3            # Vertical distance of two lines

    playerWidth = WindowSettings.width // 6
    playerHeight = WindowSettings.height // 3
    playerCoordX = WindowSettings.width // 8
    playerCoordY = WindowSettings.height // 2 

    monsterWidth = WindowSettings.width // 6
    monsterHeight = WindowSettings.height // 3
    monsterCoordX = WindowSettings.width * 5 // 8
    monsterCoordY = WindowSettings.height // 2 

    stepSize = 20

class ShopSettings:
    boxWidth = 800
    boxHeight = 200
    boxStartX = WindowSettings.width // 4   # Coordinate X of the box
    boxStartY = WindowSettings.height // 3  # Coordinate Y of the box

    textSize = 56 # Default font size
    textStartX = boxStartX + 10         # Coordinate X of the first line of dialog
    textStartY = boxStartY + 25    # Coordinate Y of the first line of dialog

class GamePath:
    # Window related path

    wild = r".\assets\background\wild.png"
    mapBlock = r".\assets\background\map.png"

    # player/npc related path
    npc = r".\assets\npc\npc.png"
 

    #monster = r".\assets\npc\monster\1.png"
    boss = r".\assets\npc\boss.png"

    groundTiles = [
        r".\assets\tiles\ground1.png", 
        r".\assets\tiles\ground2.png", 
        r".\assets\tiles\ground3.png", 
        r".\assets\tiles\ground4.png", 
        r".\assets\tiles\ground5.png", 
        r".\assets\tiles\ground6.png", 
    ]

    cityTiles = [
        r".\assets\tiles\city1.png", 
        r".\assets\tiles\city2.png", 
        r".\assets\tiles\city3.png", 
        r".\assets\tiles\city4.png", 
        r".\assets\tiles\city5.png", 
        r".\assets\tiles\city6.png", 
    ]

    cityWall = r".\assets\tiles\cityWall.png"

    bossTiles = [
        r".\assets\tiles\boss1.png", 
        r".\assets\tiles\boss2.png", 
        r".\assets\tiles\boss3.png", 
        r".\assets\tiles\boss4.png", 
        r".\assets\tiles\boss5.png", 
        r".\assets\tiles\boss6.png", 
    ]

    bossWall = r".\assets\tiles\bossWall.png"

    #portal = r".\assets\background\portal.png"

    tree = r".\assets\tiles\tree.png"

    bgm = [r".\assets\bgm\city.mp3",
           r".\assets\bgm\wild.mp3",
           r".\assets\bgm\boss.mp3"]
    menu=  r"./assets/background/menubg.jpg"
    player = [f"./assets/player/Paimon/{i}.png" for i in range(1,122)]

    npc = r".\assets\npc\npc.png"
    monster =[f"./assets/npc/enemy/enemy1/{i}.jpg" for i in range(1,17)]

    groundTiles = [f"./assets/tiles/ground{i}.png" for i in range(1,7)]

    tree = r".\assets\tiles\tree.png"
    card_backround_list=[r"./assets/cards/ATK.jpg",
                    r"./assets/cards/CURE.jpg",
                    r"./assets/cards/BUFF.jpg",
                    r"./assets/cards/SPELL.jpg",
                    r"./assets/cards/DEBUFF.jpg",
                    r"./assets/cards/EMPTY.png",
                    r"./assets/cards/SACRIFICE.jpg",
                    r"./assets/cards/REBOUND.jpg",
                    r"./assets/cards/DESPRATE.jpg",
                    r"./assets/cards/JOKER.jpg"]
    background=r"./assets/background/bg6.jpg"
    dialog=r"./assets/background/bg7.png"
    cure=[f"./assets/gif/curegif/curegif{i}.png" for i in range(1,4)]
    lightning=[f"./assets/gif/accumulate/{i}.png" for i in range(1,6)]
    animate=[f"./assets/gif/animate/{i}.png" for i in range(1,82)]
    lightshield=[f"./assets/gif/lightshield/{i}.png" for i in range(1,10)]
    fire=[f"./assets/gif/fire/{i}.png" for i in range(1,7)]
    menu=[f"./assets/gif/menubggif/{i}.png" for i in range(1,96)]
    portal=[f"./assets/gif/portal/{i}.png" for i in range(1,8)]
class PortalSettings:
    width = 320
    height = 320
    coordX = (SceneSettings.tileXnum - 10) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2

class GameState(Enum):
    MAIN_MENU = 1
    GAME_TRANSITION = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6
    GAME_PLAY_HOME = 7
    GAME_PLAY_BOSS = 8

class GameEvent:
    EVENT_BATTLE = pygame.USEREVENT + 1
    EVENT_DIALOG = pygame.USEREVENT + 2
    EVENT_SWITCH = pygame.USEREVENT + 3
    EVENT_RESTART = pygame.USEREVENT + 4
    EVENT_SHOP = pygame.USEREVENT + 5
