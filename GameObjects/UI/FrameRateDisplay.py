# coding=utf-8

from Core.GameObject import GameObject

from Core.Components.TextComponent import TextComponent

class FrameRateDisplay(GameObject):
    def awake(self):
        self.text = TextComponent()
        
        self.addComponent(self.text)
        
    def update(self):
        self.text.setText('koe')