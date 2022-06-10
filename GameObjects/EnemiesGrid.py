# coding=utf-8

from Core.GameObject import GameObject
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.CollisionComponent import CollisionComponent
from Core.Vector import Vector2

from GameObjects.Enemy import Enemy
from Core.Game import Game

class EnemiesGrid(GameObject):
    def __init__(self, width = 3, height = 2):
        super().__init__()
        
        self.gridWidth = width
        self.gridHeight = height
        self.enemySize = Vector2(0, 0)
                
    def _awake(self):
        self.collision = CollisionComponent()
        
        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                self.addChild(Enemy())
        
        self.enemySize = self.transform.children[0].getSize()
        
        self.updateGridPosition()
        self.kinetics = KineticsComponent()
        self.addComponent(self.kinetics)
        self.addComponent(self.collision)
        
    def _start(self):
        self.kinetics.disableGravity()
        self.kinetics.setVelocity(Vector2((Game.moveSpeedBase) / 3 / Game.GAME_DIFFICULTY, 0))
        
        self.updateGridSize()
        
    def _update(self):
        self.updateGridPosition()
        
        if(self.getPosition().x < 0 or self.getPosition().x > Game.WINDOW_WIDTH - self.width):
            self.kinetics.setVelocity(self.kinetics.velocity * -1)
            self.setPosition(self.getPosition() + Vector2(0, self.enemySize.y))

    def _afterUpdated(self):
        if(self.x < 0 or self.x > Game.WINDOW_WIDTH - self.width):
            self.translate(self.kinetics.velocity)
        
    def getEnemy(self, i, j):
        return self.transform.children[j * self.gridWidth + i]
    
    def updateGridPosition(self):
        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                enemy = self.getEnemy(i, j)
                
                position = Vector2(enemy.width, enemy.height)
                offset = Vector2(enemy.width / 2, enemy.height / 2)
                
                positionFinal = position + offset
                enemy.setLocalPosition(
                    Vector2(positionFinal.x * i, positionFinal.y * j)
                )
                
    def updateGridSize(self):
        self.width = (self.enemySize.x + self.enemySize.x / 2) * self.gridWidth - self.enemySize.x / 2
        self.height = (self.enemySize.y + self.enemySize.y / 2) * self.gridHeight - self.enemySize.y / 2
        