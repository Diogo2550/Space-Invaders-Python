# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.GunFire import GunFire

# Classe responsável por representar a bola do Pong
class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.__lastFire = 0

    def _awake(self):
        self.addComponent(SpriteComponent('assets/images/sprites/player.png'))
        self.addComponent(KineticsComponent())

    def _start(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()

        bottomOffset = 10
        self.setPosition(
            Vector2(Game.WINDOW_WIDTH / 2, Game.WINDOW_HEIGHT) + Vector2(-self.width / 2, -self.height - bottomOffset)
        )

    def _update(self):
        self.fireReload = .5 / Game.GAME_DIFFICULTY
        self.moveSpeedBase = Game.moveSpeedBase * Game.GAME_DIFFICULTY

        keyboard = Game.getKeyboard()
        velocity = Vector2(0, 0)
        if(keyboard.key_pressed('A') and self.getPosition().x > 0):
            velocity = Vector2(-self.moveSpeedBase, 0)
        elif(keyboard.key_pressed('D') and self.getPosition().x < Game.WINDOW_WIDTH - self.width):
            velocity = Vector2(self.moveSpeedBase, 0)

        if(keyboard.key_pressed('SPACE') and self.__lastFire < 0):
            self.fire()

        self.kinetics.setVelocity(velocity)
        self.__lastFire -= Game.DELTA_TIME

    def _afterUpdated(self):
        if(self.x < 0 or self.x > Game.WINDOW_WIDTH - self.width):
            self.translate(self.kinetics.velocity)

    def fire(self):
        self.__lastFire = self.fireReload

        fire = GameObjectBuilder.startBuild(GunFire())\
                .setPosition(self.getPosition() + Vector2(self.width / 2, 0))\
                .build()

        self.addChild(fire)