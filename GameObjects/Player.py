# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.GunFire import GunFire

# Classe responsável por representar a bola do Pong
class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.vidas = 3
        self.tempoInvuneravel = 2
        self.invuneravel = True

        self.__lastFire = 0
        self.__lastHit = 0
        
        self.spriteInvuneravel = 'assets/images/sprites/player_red.png'
        self.spriteNormal = 'assets/images/sprites/player.png'

    def _awake(self):
        self.sprite = SpriteComponent(self.spriteNormal)
        self.addComponent(self.sprite)
        
        self.addComponent(KineticsComponent())
        self.addComponent(CollisionComponent())

    def _start(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.collision = self.getComponent(CollisionComponent)

        self.fireReload = .3 / Game.GAME_DIFFICULTY
        
        self.restart()

    def _update(self):
        self.moveSpeedBase = Game.moveSpeedBase * Game.GAME_DIFFICULTY

        keyboard = Game.getKeyboard()
        velocity = Vector2(0, 0)
        if(keyboard.key_pressed('A') and self.getPosition().x > 0):
            velocity = Vector2(-self.moveSpeedBase, 0)
        elif(keyboard.key_pressed('D') and self.getPosition().x < Game.WINDOW_WIDTH - self.width):
            velocity = Vector2(self.moveSpeedBase, 0)

        if(keyboard.key_pressed('SPACE') and self.__lastFire < 0):
            self.fire()

        self.kinetics.setVelocity(velocity)
        self.__lastFire -= Game.DELTA_TIME
        self.__lastHit += Game.DELTA_TIME

    def _afterUpdated(self):
        if(self.x < 0 or self.x > Game.WINDOW_WIDTH - self.width):
            self.translate(self.kinetics.velocity)
            
        if(self.__lastHit > self.tempoInvuneravel):
            self.desabilitaInvunerabilidade()

    def fire(self):
        self.__lastFire = self.fireReload

        fire = GameObjectBuilder.startBuild(GunFire())\
                .setPosition(self.getPosition() + Vector2(self.width / 2, 0))\
                .build()
        
        fire.setVelocity(Vector2(0, -(Game.moveSpeedBase * Game.GAME_DIFFICULTY)))
        fire.addColissionWithEnemies()
        
        self.addChild(fire)
        
    def tookDamage(self):
        if(self.invuneravel):
            return
        
        self.vidas -= 1
        
        lifesHub = Game.findGameObjectWithName('hub_lifes_text')
        if(self.vidas == 0):
            Game.gameOver()
            
        lifesHub.setLifes(self.vidas)
        self.__lastHit = 0
            
        self.restart()
            
    def restart(self):
        bottomOffset = 10
        
        self.setPosition(
            Vector2(Game.WINDOW_WIDTH / 2, Game.WINDOW_HEIGHT) + Vector2(-self.width / 2, -self.height - bottomOffset)
        )
        
        self.habilitaInvunerabilidade()
        
    def habilitaInvunerabilidade(self):
        self.invuneravel = True
        self.sprite.changeSprite(self.spriteInvuneravel)
    
    def desabilitaInvunerabilidade(self):
        self.invuneravel = False
        self.sprite.changeSprite(self.spriteNormal)