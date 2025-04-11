import os as OsLib
from Engine.Scripts.SDL3 import WindowManager
from Engine.Scripts.Storage.Writer import Variables
from Engine.Scripts.Scene.SceneManager import SceneManager
from Engine.Scripts.SDL3.EventProcessor import EventProcessor

class ProjectTypes:
    PROJECT_DATAPACK   = "Data.bsdk"
    PROJECT_DATAFOLDER = "Data"

def CheckProjectType(): # too tired to use Engine.Scripts.Global.Paths
    IsDataPack   = OsLib.path.exists(OsLib.path.join("..", "..", ProjectTypes.PROJECT_DATAPACK))
    IsDataFolder = OsLib.path.isdir(OsLib.path.join(OsLib.path.dirname(__file__), "..", "..", ProjectTypes.PROJECT_DATAFOLDER))
    if IsDataFolder:
        return "DataFolder"
    elif IsDataPack:
        return "DataPack"

class Project:
    @staticmethod
    def Load():
        if CheckProjectType() == "DataFolder":
            Engine.UpdateVariables()
        elif CheckProjectType() == "DataPack":
            pass

    @staticmethod
    def LoadDataFolder():
        if CheckProjectType() == "DataFolder":
            Engine.UpdateVariables()

    @staticmethod
    def LoadDataPack():
        if CheckProjectType() == "DataPack":
            pass

    @staticmethod
    def LoadStartScene():
        LocalSceneManager = SceneManager()
        if LocalSceneManager.ActiveScene and LocalSceneManager.ActiveScene.ExecFunctions:
            for Function in LocalSceneManager.ActiveScene.ExecFunctions:
                Function()

class Engine:
    def Start(self):
        Project.Load()
        WindowManager.Init()
        self.EventProcessor = EventProcessor(WindowManager.CurrentWindow) if WindowManager.CurrentWindow else None
        self.StartEventProcessor()

    @staticmethod
    def UpdateVariables():
        Variables.UpdateVideoSettings()
        Variables.UpdateGameConfigSettings()

    def StartEventProcessor(self):
        if self.EventProcessor:
            self.EventProcessor.Start()

if __name__ == "__main__":
    Engine().Start()