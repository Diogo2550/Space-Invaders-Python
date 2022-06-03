# coding=utf-8

class SceneManager:

    __scenes = {}
    __currentScene = None
    __onSceneChangeEvent = []

    @classmethod
    def addScene(cls, scene):
        cls.__scenes[scene.getSceneName()] = scene

    @classmethod
    def getSceneByIndex(self, index):
        sceneName = list(self.__scenes.keys())[index]
        return self.__scenes[sceneName]

    @classmethod
    def changeScene(cls, sceneName):
        cls.__currentScene = cls.__scenes[sceneName]
        cls.__currentScene.activeScene()

    @classmethod
    def getCurrentScene(cls):
        return cls.__currentScene

    @classmethod
    def onSceneChange(cls, function):
        cls.__onSceneChangeEvent.append(function)

    @classmethod
    def sceneChangeHandler(cls):
        for event in cls.__onSceneChangeEvent:
            event(cls.getCurrentScene())
