# coding=utf-8

from Core.GameObject import GameObject
from Core.Game import Game

from Core.Components.TextComponent import TextComponent

class FramerateDisplay(GameObject):
    def __init__(self):
        super().__init__()
        self.framerate = {
            'interval': .5,
			'sum': 0,
			'timeElapsed': 0
		}
    
    def _awake(self):
        self.text = TextComponent()
        
        self.addComponent(self.text)
        
    def _start(self):
        self.text.setFontSize(24);
        
    def _update(self):
        self.framerate['timeElapsed'] += Game.DELTA_TIME
        
        if(Game.DELTA_TIME > 0):
	        self.framerate['sum'] += 1/Game.DELTA_TIME
        
        if(self.framerate['timeElapsed'] >= self.framerate['interval']):
            self.text.setText(f"Frames: {self.framerate['sum'] / self.framerate['interval']}")
            
            self.framerate['timeElapsed'] = 0
            self.framerate['sum'] = 0