# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Components.ClickableComponent import ClickableComponent

# Classe responsável por representar a bola do Pong
class UIButton(GameObject):
    def __init__(self):
        super().__init__()

    def _awake(self):
        self.addComponent(ClickableComponent())