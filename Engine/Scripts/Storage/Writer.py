from Engine.Scripts.Settings.Game.SceneConfig import SceneConfig
from Engine.Scripts.Storage.Reader import Ini, Config
from Engine.Scripts.Settings.Game.GameConfig import GameConfig
from Engine.Scripts.Settings.Video.VideoSettings import VideoSettings

class Variables:
    # the from import statements are placed in the functions so no circular import bullshit
    @staticmethod
    def UpdateVideoSettings():
        from Engine.Scripts.Global.Constants import Paths
        IniTool = Ini()
        IniTool.LoadIni(Paths.BloominatorPath + "Settings.ini")
        RetrievedSettings           = IniTool.GetVideoSettings()
        VideoSettings.Fullscreen    = RetrievedSettings["Fullscreen"]
        VideoSettings.Bordered      = RetrievedSettings["Bordered"]
        VideoSettings.ExFullscreen  = RetrievedSettings["ExFullscreen"]
        VideoSettings.VSync         = RetrievedSettings["VSync"]
        VideoSettings.WinWidth      = RetrievedSettings["WinWidth"]
        VideoSettings.WinHeight     = RetrievedSettings["WinHeight"]
        VideoSettings.RefreshRate   = RetrievedSettings["RefreshRate"]
        VideoSettings.ViewportWidth = RetrievedSettings["ViewportWidth"]

    @staticmethod
    def UpdateGameConfigSettings():
        from Engine.Scripts.Global.Constants import Paths
        ConfigTool = Config()
        ConfigTool.LoadConfig(Paths.Project + "Game/GameConfig.bin")
        RetrievedData      = ConfigTool.GetGameConfigData()
        GameConfig.Name    = RetrievedData["Name"]
        GameConfig.Version = RetrievedData["Version"]
        GameConfig.Icon    = RetrievedData["Icon"]

    @staticmethod
    def UpdateSceneConfigSettings():
        from Engine.Scripts.Global.Constants import Paths
        ConfigTool = Config()
        ConfigTool.LoadConfig(Paths.Project + "Game/SceneConfig.bin")
        RetrievedData          = ConfigTool.GetSceneConfigData()
        SceneConfig.Categories = None