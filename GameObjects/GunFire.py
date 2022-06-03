# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

# Classe responsável por representar a bola do Pong
class GunFire(GameObject):
    def __init__(self):
        super().__init__()

    def _awake(self):
        self.addComponent(SpriteComponent('assets/images/sprites/effects/fire01.png'))
        self.addComponent(KineticsComponent())

    def _start(self):
        self.setPosition(self.getPosition() - Vector2(self.width / 2, 0))
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.moveSpeedBase = Game.moveSpeedBase * Game.GAME_DIFFICULTY

        self.kinetics.setVelocity(Vector2(0, -self.moveSpeedBase))

    def _afterUpdated(self):
        if(self.y < 0):
            self.destroy()