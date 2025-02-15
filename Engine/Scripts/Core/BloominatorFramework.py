import time
from Engine.Scripts.GlobalValues import GlobalValues
from Engine.Scripts.User.Core.UserCore import Loader
from Engine.Scripts.Splash.DefaultSplash import BloominatorSplash
from Engine.Scripts.Window.RenderWindow import RenderWindow, WindowEvents

def InitEngine():
    WindowEvents.WindowRunning = False  # what is the poimt of this brhjas
    if RenderWindow.Init():
        WindowEvents.WindowRunning = True

    Loader.LoadGame(GlobalValues.Paths.Data)

    while WindowEvents.WindowRunning:
        WindowEvents.ProcessEvents()

if __name__ == "__main__":
    InitEngine()