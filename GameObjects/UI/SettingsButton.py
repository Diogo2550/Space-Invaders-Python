# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *

from GameObjects.UI._Button import UIButton;

# Classe responsável por representar a bola do Pong
class SettingsButton(UIButton):
    def __init__(self):
        super().__init__()

    def _awake(self):
        super()._awake()
        
        settingsSprite = SpriteComponent('assets/images/ui/menu/settings_button.png')
        self.addComponent(settingsSprite)

    def _start(self):
        self.setPosition(Game.getWindowCenter() - Vector2(self.width, 0) * 1)

    def _update(self):
        pass

    def onClick(self):
        Game.findGameObjectWithName('main_menu').enabled = False
        Game.findGameObjectWithName('settings_menu').enabled = True