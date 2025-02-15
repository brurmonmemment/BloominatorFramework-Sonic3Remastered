import configparser
from Engine.Scripts.GlobalValues import GlobalValues
from pathlib import Path

# dont worry you silly goose all these variables get updated in UserCore via LoadSettings()
# python likes to be a little silly and forces you to assign values to your variables even if you just want it to be empty
class VideoSettings:
    Windowed        = None
    Bordered        = None
    ExclFullscreen  = None
    VSync           = None
    TripleBuffering = None
    WinWidth        = None
    WinHeight       = None
    RefreshRate     = None
    ShaderSupport   = None
    ScreenShader    = None
    PixWidth        = None