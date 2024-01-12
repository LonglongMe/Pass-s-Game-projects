# -*- coding:utf-8 -*-

class Collidable:
    def __init__(self):
        self.collidingWith = {
            "obstacle": False, 
            "npc": False, 
            "monster": False, 
            "boss": False, 
            "bra":False,
            "portal":False
        }
        self.collidingObject = {
            "obstacle":[], 
            "npc":[], 
            "monster": None, 
            "boss": None, 
            "bra":[],
            "portal":[]
        }
    
    def is_colliding(self):
        return (self.collidingWith["obstacle"] or 
                self.collidingWith["npc"] or 
                self.collidingWith["monster"] or
                self.collidingWith["portal"] or 
                self.collidingWith["boss"] or
                self.collidingWith["bra"]
                )
    
    def is_colliding_bra(self):
        return self.collidingWith["bra"]
    
    def is_colliding_portal(self):
        return self.collidingWith["portal"]