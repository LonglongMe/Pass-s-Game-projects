# -*- coding:utf-8 -*-

class Collidable:
    def __init__(self):
        self.collidingWith = {
            "obstacle": False, 
            "npc": False, 
            "monster": False,
            "shop_npc": False,
            "dialog_npc":False,  
            "portal": False, 
            "boss": False, 
            "bra":False,
            "animal":False
        }
        self.collidingObject = {
            "obstacle": [], 
            "npc": None, 
            "shop_npc":[],
            "dialog_npc":[], 
            "monster": None, 
            "portal": None, 
            "boss": None, 
            "bra":[]
        }
    
    def is_colliding(self):
        return (self.collidingWith["obstacle"] or 
                self.collidingWith["npc"] or 
                self.collidingWith["monster"] or
                self.collidingWith["shop_npc"] or
                self.collidingWith["dialog_npc"] or
                self.collidingWith["portal"] or 
                self.collidingWith["boss"] or
                self.collidingWith["animal"] or
                self.collidingWith["bra"])
    def is_colliding_bra(self):
        return self.collidingWith["bra"]
    def is_colliding_portal(self):
        return self.collidingWith["portal"]