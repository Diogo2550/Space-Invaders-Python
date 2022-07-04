# coding= utf-8
from Core.Component import *
from Core.PPlay.sprite import *
from Core.Game import Game
from pygame import *

from .Abstracts.DrawingComponent import *

# Componente utilizado para a renderização de textos
# Não será possível obter o tamanho dos textos escritos pois seria necessário o uso explícito do pygame
class TextComponent(DrawingComponent):
    def __init__(self):
        super().__init__()
        self.font_color = (255, 255, 255)
        self.font_family = "Arial"
        self.font_size = 12
        self.text = ""
        
    def _update(self):
        pass

    def draw(self):
        font = pygame.font.SysFont(self.font_family, self.font_size, False, False)

        lines = self.text.splitlines()
        for i, l in enumerate(lines):
            Game.window.screen.blit(font.render(l, 0, self.font_color), (self.gameObject.x, self.gameObject.y + self.font_size*i))
        
    def setText(self, text):
        self.text = text
        
    def setFontSize(self, fontSize):
        self.font_size = fontSize
        
    def setFontFamily(self, fontFamily):
        self.font_family = fontFamily
        
    def setFontColor(self, color):
        self.font_color = color
