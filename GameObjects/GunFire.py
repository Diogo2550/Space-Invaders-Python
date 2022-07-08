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
        self.addComponent(KineticsComponent())        
        self.kinetics = self.getComponent(KineticsComponent)

        self.addComponent(SpriteComponent('assets/images/sprites/effects/fire01.png'))

        self.collision = CollisionComponent()
        self.addComponent(self.collision)

    def _awake(self):
        pass

    def _start(self):
        self.setPosition(self.getPosition() - Vector2(self.width / 2, 0))
        self.kinetics.disableGravity()

    def _afterUpdated(self):
        if(self.y < 0):
            self.destroy()
            
    def addColissionWithEnemies(self):
        enemies = Game.findGameObjectWithName('enemies')
        for enemy in enemies.transform.children:
            enemy.collision.addCollisionWith(self)
        enemies.collision.addCollisionWith(self)
        
    def addColisionWithPlayer(self):
        player = Game.findGameObjectWithName('player')
        player.collision.addCollisionWith(self)
    
    def setVelocity(self, velocity):
        self.kinetics.setVelocity(velocity)
    
    def onCollided(self, gameObject):
        from GameObjects.Enemy import Enemy
        from GameObjects.Player import Player
        
        if(isinstance(gameObject, Enemy)):
            self.destroy()
            gameObject.damage()
            Game.score += gameObject.scoreValue
        
        if(isinstance(gameObject, Player)):
            gameObject.tookDamage()
            self.destroy()