# coding=utf-8

from Core.GameObject import GameObject
from Core.Vector import Vector2

from GameObjects.Enemy import Enemy

class EnemiesGrid(GameObject):
    def __init__(self, width = 3, height = 2):
        super().__init__()
        
        self.width = width
        self.height = height
        
    def _awake(self):
        for i in range(self.width):
            for j in range(self.height):
                self.addChild(Enemy())
                
        self.updateGridPosition()
                
    def _update(self):
        self.updateGridPosition()
        
    def getEnemy(self, i, j):
        return self.transform.children[j * self.width + i]
    
    def updateGridPosition(self):
        for i in range(self.width):
            for j in range(self.height):
                enemy = self.getEnemy(i, j)
                
                position = Vector2(enemy.width, enemy.height)
                offset = Vector2(enemy.width / 2, enemy.height / 2)
                
                positionFinal = position + offset
                enemy.setPosition(
                    Vector2(positionFinal.x * i, positionFinal.y * j)
                )