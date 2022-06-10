# coding= utf-8

from Core.Components.KineticsComponent import *
from Core.Components.SpriteComponent import SpriteComponent

from GameObjects.UI.PlayButton import PlayButton
from GameObjects.UI.CloseButton import CloseButton
from GameObjects.UI.SettingsButton import SettingsButton
from GameObjects.UI.RankingButton import RankingButton
from GameObjects.UI.DifficultyChangeButton import DifficultyChangeButton
from GameObjects.UI.Score import Score
from GameObjects.Player import Player
from GameObjects.EnemiesGrid import EnemiesGrid

from Core.GameObject import GameObject
from Core.Builders.GameObjectBuilder import GameObjectBuilder
from Core.Game import *

from Core.Scene.SceneManager import SceneManager
from Core.Scene.Scene import Scene

game = Game()


# Instanciação de sprites


# Instanciação de cenas e objetos
# SCENE - MAIN MENU
scene = Scene('main_menu')

playButton = PlayButton()
closeButton = CloseButton()
settingsButton = SettingsButton()
rankingButton = RankingButton()

easy_button = GameObjectBuilder.startBuild(DifficultyChangeButton())\
                .addComponent(SpriteComponent('assets/images/ui/menu/easy_button.png'))\
                .setPosition(Game.getWindowCenter() - GameObjectBuilder.instance.getCenterPoint() - Vector2(0, 50))\
                .build()
easy_button.difficulty = 1

normal_button = GameObjectBuilder.startBuild(DifficultyChangeButton())\
                .addComponent(SpriteComponent('assets/images/ui/menu/normal_button.png'))\
                .setPosition(Game.getWindowCenter() - GameObjectBuilder.instance.getCenterPoint())\
                .build()
normal_button.difficulty = .8

hard_button = GameObjectBuilder.startBuild(DifficultyChangeButton())\
                .addComponent(SpriteComponent('assets/images/ui/menu/hard_button.png'))\
                .setPosition(Game.getWindowCenter() - GameObjectBuilder.instance.getCenterPoint() + Vector2(0, 50))\
                .build()
hard_button.difficulty = .5

main_menu = GameObject()
main_menu.setName('main_menu')
main_menu.addChild(playButton)
main_menu.addChild(closeButton)
main_menu.addChild(rankingButton)
main_menu.addChild(settingsButton)

settings_menu = GameObject()
settings_menu.setName('settings_menu')
settings_menu.addChild(easy_button)
settings_menu.addChild(normal_button)
settings_menu.addChild(hard_button)
settings_menu.enabled = False

scene.addGameObject(main_menu)
scene.addGameObject(settings_menu)


# SCENE - GAMEPLAY
scene = Scene('gameplay')

player = Player()
placar = Score()
enemyGrid = EnemiesGrid(7, 4)
enemyGrid.setName('enemies')

scene.addGameObject(player)
scene.addGameObject(enemyGrid)
scene.addGameObject(placar)


# Adição dos gameobjects ao game
game.setPlayer(player)


# Iniciação do game loop
game.developmentMode()
game.start()