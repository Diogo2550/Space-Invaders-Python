# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder
from Core.Components.CollisionComponent import CollisionComponent

from GameObjects.GunFire import GunFire
from GameObjects.Enemy import Enemy

# Classe responsável por representar a bola do Pong
class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.lifes = 3
        self.scoreValue = 500
        
    def _awake(self):
        self.addComponent(SpriteComponent('assets/images/sprites/boss.png'))