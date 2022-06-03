# coding= utf-8
from Core.Vector import *
from Core.Game import *

# Possibilitará a presença de cinética dentro de um gameobject
class CollisionComponent(Component):
    def __init__(self):
        super().__init__()
        self.objects = []
        self.collidedList = []
        
    def addCollisionWith(self, object):
        if(isinstance(object, list)):
            self.objects.extend(object)
        else:
            self.objects.append(object)

    def _update(self):
        self.collidedList = []
        
        for obj in self.objects:
            if(self.gameObject.collided(obj)):
                self.collidedList.append(obj)
                
    def isColliding(self):
        return len(self.collidedList) > 0