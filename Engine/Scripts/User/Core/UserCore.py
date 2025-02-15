import importlib
from pathlib import Path, PosixPath
from configparser import ConfigParser as IniParser
from Engine.Scripts.GlobalValues import GlobalValues
from sdl3 import SDL_SetWindowTitle, SDL_GetWindowTitle
from Engine.Scripts.Window.VideoSettings import VideoSettings

# dynamically import renderwindow to circumvent the tragic circular import errors
# dirty workaround but hey i mean it works ( ͡° ͜ʖ ͡°) and you could use this somewhere else
def LazyModuleImport(Module, Attribute=None):
    IModule = importlib.import_module(Module)
    if Attribute:
        IAttribute = getattr(IModule, "RenderWindow")
        return IModule, IAttribute()
    return IModule

def LoadSettings():
    Ini = IniParser()
    Ini.read(GlobalValues.Paths.Main / "Settings.ini")
    if Ini:
        VideoSettings.Windowed        = Ini.getboolean("Video", "Windowed")
        VideoSettings.Bordered        = Ini.getboolean("Video", "Bordered")
        VideoSettings.ExclFullscreen  = Ini.getboolean("Video", "ExclFullscreen")
        VideoSettings.VSync           = Ini.getboolean("Video", "VSync")
        VideoSettings.TripleBuffering = Ini.getboolean("Video", "TripleBuffering")
        VideoSettings.WinWidth        = Ini.getint("Video", "WinWidth")
        VideoSettings.WinHeight       = Ini.getint("Video", "WinHeight")
        VideoSettings.RefreshRate     = Ini.getint("Video", "RefreshRate")
        VideoSettings.ShaderSupport   = Ini.getboolean("Video", "ShaderSupport")
        VideoSettings.ScreenShader    = Ini.getint("Video", "ScreenShader")
        VideoSettings.PixWidth        = Ini.getint("Video", "PixWidth")
    else:
        VideoSettings.Windowed        = True
        VideoSettings.Bordered        = True
        VideoSettings.ExclFullscreen  = True
        VideoSettings.VSync           = True
        VideoSettings.TripleBuffering = False
        VideoSettings.WinWidth        = 1272
        VideoSettings.WinHeight       = 720
        VideoSettings.RefreshRate     = 60
        VideoSettings.ShaderSupport   = True
        VideoSettings.ScreenShader    = 0
        VideoSettings.PixWidth        = 424

class Loader:
    @staticmethod
    def LoadGame(GamePath):
        Module, Instance = LazyModuleImport("Engine.Scripts.Window.RenderWindow", "RenderWindow")
        Window = Instance.Window

        if Path(GamePath).suffix == ".blfk":
            pass # insert loading logic for data pack mode (regular)
        elif Path(GamePath).suffix == "":
            SDL_SetWindowTitle(Window, SDL_GetWindowTitle(Window) + b" (Data Folder Mode)")
            pass # insert loading logic for data folder mode