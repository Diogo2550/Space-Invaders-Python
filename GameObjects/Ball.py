# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *

# Classe responsável por representar a bola do Pong
class Ball(GameObject):
    def __init__(self):
        super().__init__()
        self.moveSpeedBase = 320

    def _start(self):
        # Ajusta os parâmetros de movimentação
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.kinetics.setVelocity(Vector2(self.moveSpeedBase, self.moveSpeedBase))

        # Seta a posição inicial para o centro da tela
        self.setPosition(Game.getWindowCenter() - self.getCenterPoint());

    def _update(self):
        windowWidth = Game.window.width;
        windowHeight = Game.window.height;
        position = self.getPosition()
        speed = self.kinetics.velocity

        if(position.x >= windowWidth - self.width):
            speed.x = -abs(speed.x)

        if(position.x <= 0):
            speed.x = abs(speed.x)

        if(position.y >= windowHeight - self.height):
            speed.y = -abs(speed.y)

        if(position.y <= 0):
            speed.y = abs(speed.y)

        self.kinetics.velocity = speed