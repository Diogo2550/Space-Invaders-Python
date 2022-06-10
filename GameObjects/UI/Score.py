# coding=utf-8

from Core.GameObject import GameObject
from Core.Game import Game
from Core.Vector import Vector2

from Core.Components.TextComponent import TextComponent

class Score(GameObject):
    def __init__(self):
        super().__init__()
    
    def _awake(self):
        self.text = TextComponent()
        self.addComponent(self.text)
        
    def _start(self):
        self.text.setFontSize(24)
        self.setPosition(Vector2(Game.WINDOW_WIDTH - 240, 10))
        
    def _update(self):
        self.text.setText(f'Score: {Game.score}')