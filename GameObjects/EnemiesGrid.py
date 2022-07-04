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
        
        self.setPosition(Vector2(1, 0))
        
        self.gridWidth = width
        self.gridHeight = height
        self.enemySize = Vector2(0, 0)
        
        # Limite esquerdo da grid. Guardará os índices dos inimigos mais a esquerda
        self.limitLeft = []
        # Limite direito da grid. Guardará os índices dos inimigos mais a direita
        self.limitRight = []
        
        self.columnsDestroyedLeft = 0
        self.columnsDestroyedRight = 0
        self.totalOfEnemies = width * height
                
    def _awake(self):
        self.collision = CollisionComponent()
        
        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                enemy = Enemy()
                enemy.index = i * self.gridHeight + j
                self.addChild(enemy)
        
        self.enemySize = self.transform.children[0].getSize()
        
        self.updateGridPosition()
        self.kinetics = KineticsComponent()
        self.addComponent(self.kinetics)
        self.addComponent(self.collision)
        
    def _start(self):
        self.shootDelay = .1 * Game.GAME_DIFFICULTY
        self.__lastShoot = 0
        
        self.kinetics.disableGravity()
        self.kinetics.setVelocity(Vector2((Game.moveSpeedBase) / 3 * (Game.GAME_DIFFICULTY * .6), 0))
        
        self.updateGridSize()
        self.collision.addCollisionWith(Game.player)
        
    def _update(self):
        self.updateGridPosition()
        
        if(self.getPosition().x <= 0 or self.getPosition().x >= Game.WINDOW_WIDTH - self.width):
            self.kinetics.setVelocity(self.kinetics.velocity * -1)
            self.setPosition(self.getPosition() + Vector2(0, self.enemySize.y))
            
        if(self.__lastShoot > self.shootDelay):
            self.fire()      

    def _afterUpdated(self):
        if(self.x < 0 or self.x > Game.WINDOW_WIDTH - self.width):
            self.kinetics.undoMoviment()
        self.__lastShoot += Game.DELTA_TIME
        
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
                    Vector2(positionFinal.x * i, positionFinal.y * j) - Vector2(positionFinal.x * (self.columnsDestroyedLeft), 0)
                )
                
    def updateGridSize(self):
        self.limitLeft = self.__findLimit()
        self.limitRight = self.__findLimit(False)
        
        if(len(self.limitLeft) > 0):
            self.columnsDestroyedLeft = self.limitLeft[0] % self.gridWidth
        if(len(self.limitRight) > 0):
            self.columnsDestroyedRight = self.gridWidth - self.limitRight[0] % self.gridWidth - 1
        
        self.width = (self.enemySize.x + self.enemySize.x / 2) * (self.gridWidth - (self.columnsDestroyedLeft + self.columnsDestroyedRight)) - self.enemySize.x / 2
        self.height = (self.enemySize.y + self.enemySize.y / 2) * self.gridHeight - self.enemySize.y / 2
        
    def childDestroyed(self, childIndex):
        if(childIndex in self.limitLeft):
            self.limitLeft.remove(childIndex)
            
            if(len(self.limitLeft) == 0):
                self.updateGridSize()
                
                children = self.transform.children[childIndex]
                self.setPosition(
                    self.getPosition() +
                    Vector2(children.width + children.width / 2, 0)
                )
                
        if(childIndex in self.limitRight):
            self.limitRight.remove(childIndex)
            
            if(len(self.limitRight) == 0):
                self.updateGridSize()
                
        self.totalOfEnemies -= 1
        if(self.totalOfEnemies == 0):
            self.destroy()
            Game.newLevel()
        
        speedPercent = (1 + ((self.gridWidth * self.gridHeight - self.totalOfEnemies) / 100))
        self.kinetics.velocity *= speedPercent
                        
    def fire(self):
        from random import randint
        
        enemy = self.__getShooter()
        if(enemy != None):
	        enemy.fire()
        
        self.__lastShoot = 0
        self.shootDelay = 2 / (Game.GAME_DIFFICULTY) + (randint(6, 6)/10)
        
    def __findLimit(self, left = True):
        totalElements = self.gridWidth * self.gridHeight
        futher = self.gridWidth if left else 0
        limit = []
        
        for i in range(totalElements):
            if(left):
	            if(self.transform.children[i].enabled and i % self.gridWidth < futher):
                	futher = i
            else:
                if(self.transform.children[i].enabled and i % self.gridWidth > futher):
                	futher = i
        
        for i in range(futher, totalElements, self.gridWidth):
            if(self.transform.children[i].enabled):
                limit.append(i)
        
        return limit
    
    def __getShooter(self):
        from random import randint
        minOffset = self.columnsDestroyedLeft
        maxOffset = self.gridWidth - self.columnsDestroyedRight - 1
        
        shooter = None
        gameFinished = self.columnsDestroyedLeft + self.columnsDestroyedRight >= self.gridWidth - 1
        while(shooter == None and not gameFinished):
            column = randint(minOffset, maxOffset)
            
            for enemyLine in range(self.gridHeight - 1, -1, -1):
                shooterAux = self.getEnemy(column, enemyLine)
                if(shooterAux.enabled):
                    shooter = shooterAux
                    break
        
        return shooter