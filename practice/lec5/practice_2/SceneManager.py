# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import NPC
import ShoppingBox
import Scene
from Scene import *
class SceneManager:
    def __init__(self, window):
        self.scene = CityScene(window)
        self.window = window

    
    def check_event_shopping(self, player, keys):
        pass

    def flush_scene(self):
        if self.scene.type == SceneType.CITY:
            self.scene = WildScene(self.window)
        elif self.scene.type == SceneType.WILD:
            self.scene = CityScene(self.window)

    def update(self):
        # update npc
        for each in self.scene.npcs.sprites():
            each.update()
        print(f"{self.scene.type}")

    def render(self):
        self.scene.render()

    
