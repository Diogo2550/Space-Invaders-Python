# coding= utf-8
from Core.Vector import *
from Core.Game import *


class TransformComponent(Component):
    ''' Componente que representa uma coordenada no espaço e um container de objetos '''
    def __init__(self):
        super().__init__()
        self.position = Vector2(0, 0)
        self.parent = None
        self.children = []
        self.rotateAngle = 0

        self.onRotateEvent = []

    def _update(self):
        self.gameObject.x = self.position.x
        self.gameObject.y = self.position.y
        
    def addChild(self, child):
        child.setParent(self)
        self.children.append(child)

        child.awake()
        child.start()

    def removeChild(self, child):
        self.children.remove(child)

    def rotate(self, angle):
        self.rotateAngle = angle

        for event in self.onRotateEvent:
            event(angle)
        
    def getChildByType(self, childType):
        for child in self.children:
            if(isinstance(child, childType)):
                return child
        return None
    
    def getChildByName(self, childName):
        for child in self.children:
            if(self.name == childName):
                return child
        return None
    
    def setName(self, name):
        self.name = name
        
    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position
        
    def translate(self, translate):
        ''' Move o objeto, a partir da posição atual, o vetor translate dado '''
        self.position += translate * Game.DELTA_TIME

    def onRotate(self, function):
        self.onRotateEvent.append(function)