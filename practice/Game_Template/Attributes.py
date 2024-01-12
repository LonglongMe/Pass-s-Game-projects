# -*- coding:utf-8 -*-

class Collidable:
    def __init__(self):
        self.collidingWith = {
            "obstacle": False, 
            "npc": False, 
            "monster": False, 
            "portal": False, 
            "boss": False, 
            "bra":False,
            "animal":False
        }
        self.collidingObject = {
            "obstacle": [], 
            "npc": None, 
            "monster": None, 
            "portal": None, 
            "boss": None, 
            "bra":[]
        }
    
    def is_colliding(self):
        return (self.collidingWith["obstacle"] or 
                self.collidingWith["npc"] or 
                self.collidingWith["monster"] or
                self.collidingWith["portal"] or 
                self.collidingWith["boss"] or
                self.collidingWith["animal"] or
                self.collidingWith["bra"])
    def is_colliding_bra(self):
        return self.collidingWith["bra"]
    #def is_colliding_animal(self):
     #   return self.collidingWith["animal"]