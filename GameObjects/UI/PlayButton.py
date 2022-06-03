# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *

from GameObjects.UI._Button import UIButton;

# Classe responsável por representar a bola do Pong
class PlayButton(UIButton):
    def __init__(self):
        super().__init__()

    def _awake(self):
        super()._awake()

        playSprite = SpriteComponent('assets/images/ui/menu/start_button.png')
        self.addComponent(playSprite)

    def _start(self):
        self.setPosition(Game.getWindowCenter() - Vector2(self.width, 0) * 3)
        pass

    def _update(self):
        pass

    def onClick(self):
        SceneManager.changeScene('gameplay')
