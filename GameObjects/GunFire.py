# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.Components.CollisionComponent import CollisionComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder


# Classe responsável por representar a bola do Pong
class GunFire(GameObject):
    def __init__(self):
        super().__init__()

    def _awake(self):
        self.collision = CollisionComponent()

        self.addComponent(SpriteComponent('assets/images/sprites/effects/fire01.png'))
        self.addComponent(KineticsComponent())        
        self.addComponent(self.collision)

    def _start(self):
        self.setPosition(self.getPosition() - Vector2(self.width / 2, 0))
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.moveSpeedBase = Game.moveSpeedBase * Game.GAME_DIFFICULTY

        self.kinetics.setVelocity(Vector2(0, -self.moveSpeedBase))
        self.__addColissionWithEnemies()

    def _afterUpdated(self):
        if(self.y < 0):
            self.destroy()
            
    def __addColissionWithEnemies(self):
        enemies = Game.findGameObjectWithName('enemies')
        for enemy in enemies.transform.children:
            enemy.collision.addCollisionWith(self)
        enemies.collision.addCollisionWith(self)
    
    def onCollided(self, gameObject):
        from GameObjects.Enemy import Enemy
        
        if(isinstance(gameObject, Enemy)):
            self.destroy()
            gameObject.destroy()
            Game.score += 100