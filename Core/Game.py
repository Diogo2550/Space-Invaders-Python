# coding= utf-8
from Core.PPlay.window import *
from Core.Components.Abstracts.DrawingComponent import *
from Core.PPlay.gameimage import *
from Core.Vector import Vector2

from Core.Scene.SceneManager import SceneManager

# Destruir objetos instanciados dinamicamente ao inciar cena

class Game:

    DEVELOPMENT_MODE = False

    # Configurações da janela
    WINDOW_TITLE = 'Space Warriors'
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 700
    DELTA_TIME = 0

    SPEED_MULTIPLIER = 1
    GAME_DIFFICULTY = 1
    GAME_MODE = 2

    moveSpeedBase = 360
    window = None
    player = None
    debug = {
		'scene': None
	}
    score = 0
    
    def __init__(self):
        self.__bootstrap()
        

#------------------------------- ESTÁTICOS -------------------------------------
    @classmethod
    def getWindowCenter(cls):
        ''' Obtém o ponto central da janela do jogo '''
        return Vector2(
            Game.WINDOW_WIDTH / 2,
            Game.WINDOW_HEIGHT / 2
        )

    @classmethod
    def getKeyboard(cls):
        ''' Obtém a atual instância do teclado sendo utilizada '''
        return Game.window.get_keyboard()

    @classmethod
    def getMouse(cls):
        ''' Obtém a atual instância do mouse sendo utilizada '''
        return Game.window.get_mouse()

    @staticmethod
    def findGameObjectWithName(name):
        return SceneManager.getCurrentScene().getGameObjectWithName(name)

    @classmethod
    def developmentMode(cls):
        cls.DEVELOPMENT_MODE = True

# ------------------------------- ADIÇÃO DE ELEMENTOS -------------------------------------
    def setBackground(self, backgroundPath):
        ''' Adiciona um background para o Game '''
        self.background = GameImage(backgroundPath)

    @classmethod
    def setPlayer(cls, player):
        ''' Seta o jogador para que o mesmo possa ser visto globalmente '''
        cls.player = player

# ------------------------------- LIFECYCLE -------------------------------------
    def __bootstrap(self):
        window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        window.set_title(Game.WINDOW_TITLE)

        Game.window = window

    def start(self):
        if(Game.DEVELOPMENT_MODE):
            from Core.Debug import index
            
            SceneManager.changeScene(SceneManager.getSceneByIndex(1).getSceneName())

            index.createDebugScene()
            index.showFramerate()
            
            Game.debug['scene'].activeScene()
        else:
            SceneManager.changeScene(SceneManager.getSceneByIndex(0).getSceneName())

        self.__gameLoop()

    def __gameLoop(self):
        while(True):
            Game.DELTA_TIME = self.window.delta_time()

            # Inputs
            if (Game.getKeyboard().key_pressed('ESC')):
                SceneManager.changeScene('main_menu')

            # Desenhando background
            try:
                self.background.draw()
            except Exception:
                Game.window.set_background_color((0, 0, 0))

            SceneManager.getCurrentScene().play()
            
            if(Game.DEVELOPMENT_MODE):
                Game.debug['scene'].play()

            # Atualizando a janela
            Game.window.update()