# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.GunFire import GunFire

# Classe responsável por representar a bola do Pong
class Enemy(GameObject):
    def __init__(self):
        super().__init__()

    def _awake(self):
        self.addComponent(SpriteComponent('assets/images/sprites/enemy.png'))

    def _start(self):
        pass

    def _update(self):
        pass
    