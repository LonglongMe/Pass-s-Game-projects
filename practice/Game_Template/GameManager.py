# -*- coding:utf-8 -*-

import sys
import pygame
import Maps
from Player import Player
import Scene 
from Scene import *
from Settings import *
from PopUpBox import *

class GameManager:
    def __init__(self,window):
        self.state=GameState.MAIN_MENU
        self.player=Player(60,20)
        self.scene = StartMenu(window)
        self.window = window
        self.clock = pygame.time.Clock()
        

    def game_reset(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Necessary game components here ↓
    def tick(self, fps):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def get_time(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Scene-related update functions here ↓
    def flush_scene(self):
        if self.scene.type == SceneType.HOME:
            self.scene = WildScene(self.window)
            self.state= GameState.GAME_PLAY_WILD
        elif self.scene.type == SceneType.WILD:
            self.scene = HomeScene(self.window)
            self.state= GameState.GAME_PLAY_HOME
        elif self.scene.type == SceneType.MENU:
            self.state= GameState.GAME_PLAY_HOME
            self.scene = WildScene(self.window)
            print("scene changed")
            print(f"{self.scene.type}")

    def update(self):
        self.clock.tick(30)
        if self.state == GameState.MAIN_MENU:
            self.update_main_menu(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_HOME:
            self.update_home(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_WILD:
            self.update_wild(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_BOSS:
            self.update_boss(pygame.event.get())
  

    def update_main_menu(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 传送
            if event.type == GameEvent.EVENT_SWITCH:
                GameManager.flush_scene(self)
                self.state=GameState.GAME_PLAY_WILD

        

    def update_home(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_wild(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 传送
            if event.type== GameEvent.EVENT_SWITCH:
                GameManager.flush_scene()
        self.update_collide()
        for each in self.scene.obstacles.sprites():
            each.update()
        for each in self.scene.decorates.sprites():
            each.update()
    def update_boss(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Collision-relate update funtions here ↓
    def update_collide(self):
        self.player.try_move()
        if pygame.sprite.spritecollide(self.player, self.scene.obstacles, False) :
            self.player.collidingWith["obstacle"]=True
        else:
            self.player.collidingWith["obstacle"]=False


        # Player -> NPCs; if multiple NPCs collided, only first is accepted and dealt with.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> Monsters
        if pygame.sprite.spritecollide(self.player, self.scene.monster, False) :
            self.player.collidingWith["monster"]=True
        else:
            self.player.collidingWith["monster"]=False
        
        # Player -> Portals
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Player -> Boss
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_NPCs(self):
        # This is not necessary. If you want to re-use your code you can realize this.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Render-relate update functions here ↓
    def render(self):
        if self.scene.type==SceneType.MENU:
            self.render_main_menu()
        elif self.scene.type == SceneType.WILD:           
            self.render_wild()
        elif self.scene.type == SceneType.HOME:
            self.render_home()
    
    def render_main_menu(self):
        StartMenu.update_menu(self)
        #self.window.fill((255,255,255))
        #self.update_main_menu(self.scene.type)
        #print(self.scene.position2)
        self.window.blit(self.scene.image,(0,75))
        pygame.draw.rect(self.window,(200,200,200), self.scene.position1,0,border_radius=9 )
        #self.window.blit(self.scene.button,self.scene.position,0,9)
        self.window.blit(self.scene.text,(self.scene.position2))
        self.window.blit(self.scene.text2,(self.scene.position3))
        
    
    def render_home(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render_wild(self):
        #print("rendering")
        self.update()
        self.scene.render(self.player)

    def render_boss(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

