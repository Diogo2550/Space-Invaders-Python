# coding=utf-8

from Core.Scene.SceneManager import SceneManager
from Core.Components.Abstracts.DrawingComponent import DrawingComponent

class Scene:
    def __init__(self, sceneName):
        self.__sceneName = sceneName
        self.__gameObjects = []
        self.__activated = False

        SceneManager.addScene(self)
        SceneManager.onSceneChange(self.__onSceneChangeHandler)

    def addGameObject(self, gameObject):
        self.__gameObjects.append(gameObject)

    def getGameObjects(self):
        return self.__gameObjects

    def getGameObjectWithName(self, name):
        for gameObject in self.__gameObjects:
            if(gameObject.getName() == name):
                return gameObject
        return None

    def getSceneName(self):
        return self.__sceneName

    def activeScene(self):
        self.__activated = True
        self.__startGameObjects()

    def play(self):
        # Update
        for gameObject in self.__gameObjects:
            gameObject.update()

        # Desenho
        for gameObject in self.__gameObjects:
            gameObject.draw()

    def __startGameObjects(self):
        for gameObject in self.__gameObjects:
            gameObject.awake()

        for gameObject in self.__gameObjects:
            gameObject.start()

    def __onSceneChangeHandler(self, sceneName):
        if(sceneName == self.__sceneName):
            self.activeScene()
        else:
            self.__activated = False
