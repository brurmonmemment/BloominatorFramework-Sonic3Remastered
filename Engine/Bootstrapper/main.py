# To ensure imports work correctly
import sys, os

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

from sdl3 import SDL_ShowWindow
from Engine.Scripts.SDL3 import WindowManager
from Engine.Scripts.SDL3 import EventProcessor
from Engine.Scripts.Global.Logging import Logging
from Engine.Scripts.Storage.Writer import Variables
from Engine.Scripts.Scene import SceneManager
from Engine.Scripts.Global.Constants import Project as PCheck
from Engine.Scripts.Settings.Game.GameConfig import GameConfig

def TextColorway():
    Colors = [(224, 224, 0), (224, 128, 0), (224, 32, 0), (160, 0, 96)]
    Text = "[Bloominator Framework] Version 1.0"

    def GetCode(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    Index = 0
    PatternDirection = 1
    ColoredText = []

    for I, Character in enumerate(Text):
        if Character != " ":
            ColoredText.append(GetCode(*Colors[Index]) + Character)
        else:
            ColoredText.append(Character)

        if (I + 1) % 3 == 0:
            if PatternDirection == 1:
                Index += 1
                if Index == len(Colors):
                    PatternDirection = -1
                    Index -= 2
            else:
                Index -= 1
                if Index < 0:
                    PatternDirection = 1
                    Index += 2

    print("".join(ColoredText) + "\033[0m")

class Project:
    @staticmethod
    def Load():
        if PCheck.CheckProjectType():
            Engine.UpdateVariables()
            if PCheck.CheckProjectType() == "DataFolder":
                Project.LoadDataFolder()
            elif PCheck.CheckProjectType() == "DataPack":
                Project.LoadDataPack()
            else:
                Logging.PrintConsole("Bootstrapper", "Error", "Failed to find a project!")

    @staticmethod
    def LoadDataFolder():
        if PCheck.CheckProjectType() == "DataFolder":
            Variables.UpdateGameConfigSettings()

            Logging.PrintConsole("Bootstrapper", "Info", "Detected data folder!")
            Logging.PrintConsole("Bootstrapper", "Info", "Game configuration:")
            Logging.PrintConsole("Bootstrapper", "Info", f" - Name: {GameConfig.Name}, Version {GameConfig.Version}")
            Logging.PrintConsole("Bootstrapper", "Info", f" - Icon: {GameConfig.Icon}")

            WindowManager.UpdateWindowTitle(GameConfig.Name)
            WindowManager.UpdateWindowIcon(GameConfig.Icon)

            Logging.PrintConsole("Bootstrapper", "Info", "Updated game config settings")

            # WHERES THE FIRST SCENEEEEEE

    @staticmethod
    def LoadDataPack(): # todo: do something here
        if PCheck.CheckProjectType() == "DataPack":
            Logging.PrintConsole("Bootstrapper", "Info", "Detected data pack!")

    @staticmethod
    def LoadStartScene():
        if SceneManager.ActiveScene and SceneManager.ActiveScene.InitFuncs:
            for Function in SceneManager.ActiveScene.InitFuncs:
                Function()

class Engine:
    @staticmethod
    def Start():
        TextColorway()

        # Load game
        Project.Load()
        
        # WM start
        WindowManager.Init()
        SDL_ShowWindow(WindowManager.Window)

        # EP
        Logging.PrintConsole("Bootstrapper", "Info", "Started event processor")
        EventProcessor.Start()

    @staticmethod
    def UpdateVariables():
        Variables.UpdateVideoSettings()
        Logging.PrintConsole("Bootstrapper", "Task", "Updating video settings...")

if __name__ == "__main__":
    Engine.Start()