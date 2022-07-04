# coding=utf-8

from Core.GameObject import GameObject
from Core.Game import Game
from Core.Vector import Vector2

from Core.Components.TextComponent import TextComponent
from Core.FileScoreManager import obterPontuacao

class RankingText(GameObject):
    def __init__(self):
        super().__init__()
    
    def _awake(self):
        self.text = TextComponent()
        self.addComponent(self.text)
        
    def _start(self):
        self.text.setFontSize(24)
        self.setPosition(Vector2(
            Game.WINDOW_WIDTH / 2 - 200, 
            Game.WINDOW_HEIGHT / 2 - 100
        ))
        
        ranking = obterPontuacao()
        text = ''
        for score in ranking:
            text += f'{score[0]:40} {score[1]}\n'
        text += '\nPressione ESC para retornar ao menu'
        
        self.text.setText(text)
    
    def _update(self):
        if(Game.getKeyboard().key_pressed('ESC')):
            Game.findGameObjectWithName('settings_menu').enabled = False
            Game.findGameObjectWithName('main_menu').enabled = True
            Game.findGameObjectWithName('ranking_menu').enabled = False