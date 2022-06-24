# coding=utf-8

from Core.GameObject import GameObject
from Core.Game import Game
from Core.Vector import Vector2

from Core.Components.TextComponent import TextComponent

class LifesDisplay(GameObject):
    def __init__(self):
        super().__init__()
        self.playerLifes = 3
    
    def _awake(self):
        self.text = TextComponent()
        self.addComponent(self.text)
        
    def _start(self):
        self.text.setFontSize(24)
        self.setPosition(Vector2(Game.WINDOW_WIDTH / 2 - 120, 10))
        
    def _update(self):
        self.text.setText(f'Vidas: {self.playerLifes}')
        
    def setLifes(self, lifes):
        self.playerLifes = lifes