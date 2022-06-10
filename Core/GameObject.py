# coding= utf-8
from .PPlay.gameobject import GameObject as GameObjectP
from .Component import Component
from .Vector import Vector2
from .Components.TransformComponent import TransformComponent
from .Components.Abstracts.DrawingComponent import DrawingComponent
from .Components.CollisionComponent import CollisionComponent

# Classe customizada para manipula��o de gameobjects
class GameObject(GameObjectP):
    def __init__(self, name = ''):
        super().__init__()
        self.components = []
        
        self.transform = TransformComponent()
        self.addComponent(self.transform)
        
        self.name = name
        self.enabled = True

        self.__awaked = False

    def setName(self, name):
        self.transform.setName(name)

    def getName(self):
        return self.transform.name

    def destroy(self):
        if(self.transform.parent):
            self.transform.parent.removeChild(self)
        else:
            print('objeto principal destruido')
        self.disable()

    def setParent(self, parent):
        self.transform.parent = parent

#------------------------COMPONENTS METHODS-------------------------------
    def addComponent(self, component):
        ''' Adiciona uma nova instância de um Component qualquer ao gameobject '''
        if(isinstance(component, Component)):
            component.setGameObject(self)
            self.components.append(component)
        else:
            raise Exception(f"Instancia da classe {component.__class__} nao pertence ao tipo Component.")

    def getComponent(self, componentType):
        ''' Pega a instância do ComponentType requisitado, caso haja, presente no objeto. Retorna None caso não encontra '''
        for component in self.components:
            if(isinstance(component, componentType)):
                return component
        return None


#------------------------LIFECICLE METHODS OF GAMEOBJECTS-------------------------------
    def awake(self):
        if(not self.__awaked):
            self._awake()
            self.__awaked = True

    def start(self):
        for component in self.components:
            component.start()
        self._start()

    def update(self):
        if(self.enabled):
            for component in self.components:
                if(isinstance(component, CollisionComponent) and self.transform.parent):
                    parentCollision = self.transform.parent.gameObject.getComponent(CollisionComponent)
                    if(parentCollision and parentCollision.isColliding()):
                        component.update()
                else:
                    component.update()
                
        for child in self.transform.children:
            if(child != None):
	            child.update()

        self._update()
        self._afterUpdated()
        
    def addChild(self, child):
        self.transform.addChild(child)

    def removeChild(self, child):
        self.transform.removeChild(child)

    def getChildByType(self, childType):
        return self.transform.getChildByType(childType)
    
    def getChildByName(self, childName):
        return self.transform.getChildByName(childName)

    def draw(self):
        if (self.enabled):
            drawingComponent = self.getComponent(DrawingComponent)
            if (drawingComponent):
                drawingComponent.draw()

            for child in self.transform.children:
                child.draw()
                
    def disable(self):
        self.enabled = False
        
    def enable(self):
        self.enabled = True


#------------------------POSITION METHODS-------------------------------
    def setPosition(self, position):
        self.transform.setPosition(position)
        
    def setLocalPosition(self, position):
        if(self.transform.parent):
            self.setPosition(self.transform.parent.getPosition() + position)
        else:
            self.setPosition(position)
        
    def getPosition(self):
        return self.transform.getPosition()

    def translate(self, position):
        ''' Move o objeto, a partir da posição atual, o vetor translate dado '''
        self.transform.translate(position)
    

#------------------------SIZE METHODS-------------------------------
    def getSize(self):
        return Vector2(self.width, self.height)

    def setSize(self, witdh, height):
        self.width = witdh
        self.height = height

    def getCenterPoint(self):
        ''' Obtém o ponto centro do objeto '''
        return Vector2(
			self.width / 2,
			self.height / 2
		)

#------------------------LIFECICLE METHODS OF INSTANCES-------------------------------        
    def _awake(self):
        pass

    def _start(self):
        pass

    def _update(self):
        pass
	
    def _afterUpdated(self):
        pass

#-------------------------MOUSE EVENTS-------------------------------
    def onClick(self):
        pass

    def onKeyDown(self):
        pass

    def onKeyPressed(self):
        pass

    def onKeyUp(self):
        pass
    
#-------------------------EVENTS-------------------------------
    def onCollided(self, gemeObject):
        pass