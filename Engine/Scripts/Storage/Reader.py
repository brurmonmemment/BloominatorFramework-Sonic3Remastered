import configparser
from Engine.Scripts.Global.Constants import Binaries

class Ini:
    def __init__(self):
        self.ConfigParser = None

    def LoadIni(self, Path: str):
        self.ConfigParser = configparser.ConfigParser()
        self.ConfigParser.read(Path)

    def GetGameSettings(self):
        GameSettings = self.ConfigParser["Game"]
        GameMap      = {
            "Logging": GameSettings.getboolean("Logging"),
            "Debug":   GameSettings.getboolean("Debug")
        }
        return GameMap

    def GetVideoSettings(self):
        VideoSettings = self.ConfigParser["Video"]
        VideoMap      = {
            "Fullscreen":    VideoSettings.getboolean("Fullscreen"),
            "Bordered":      VideoSettings.getboolean("Bordered"),
            "ExFullscreen":  VideoSettings.getboolean("ExFullscreen"),
            "VSync":         VideoSettings.getboolean("VSync"),
            "WinWidth":      VideoSettings.getint("WinWidth"),
            "WinHeight":     VideoSettings.getint("WinHeight"),
            "RefreshRate":   VideoSettings.getint("RefreshRate"),
            "ViewportWidth": VideoSettings.getint("ViewportWidth")
        }
        return VideoMap

    def GetAudioSettings(self):
        AudioSettings = self.ConfigParser["Video"]
        AudioMap      = {
            "MusicStreaming": AudioSettings.getboolean("MusicStreaming"),
            "MusicVolume":    AudioSettings.getint("MusicVolume"),
            "SFXVolume":      AudioSettings.getint("SFXVolume")
        }
        return AudioMap

    def GetInputSettings(self):
        IS = []
        for Player in range(1, 5):
            if self.ConfigParser.has_section(f"Input{Player}"):
                InputData = self.ConfigParser[f"Input{Player}"]
                InputMap  = {
                    "Type":         InputData.get("Type"),
                    "ButtonUp":     InputData.get("ButtonUp"),
                    "ButtonDown":   InputData.get("ButtonDown"),
                    "ButtonLeft":   InputData.get("ButtonLeft"),
                    "ButtonRight":  InputData.get("ButtonRight"),
                    "ButtonA":      InputData.get("ButtonA"),
                    "ButtonB":      InputData.get("ButtonB"),
                    "ButtonC":      InputData.get("ButtonC"),
                    "ButtonX":      InputData.get("ButtonX"),
                    "ButtonY":      InputData.get("ButtonY"),
                    "ButtonZ":      InputData.get("ButtonZ"),
                    "ButtonStart":  InputData.get("ButtonStart"),
                    "ButtonSelect": InputData.get("ButtonSelect")
                }
                IS.append(InputMap)
        return IS

class Config:
    def __init__(self):
        self.Config = None
        self.Path   = None

    def LoadConfig(self, Path: str):
        self.Path = Path
        with open(Path, "rb") as ConfigFile:
            self.Config = ConfigFile.read()

    def GetGameConfigData(self):
        if Binaries.GameConfig in self.Path:
            ConfigData = self.Config.split(b"\x00")

            GameCfgMap = {
                "Name":    ConfigData[4].decode("utf-8")[1:-1],
                "Version": int(ConfigData[5].decode("utf-8")[1:]),
                "Icon":    ConfigData[7][11:-1].decode("utf_8")
            }

            return GameCfgMap
        else:
            print("Can't get game config data if there isn't a game config file!!!!!")
            return None

    def GetSceneConfigData(self):
        if Binaries.SceneConfig in self.Path:
            ConfigData = self.Config.split(b"\x00")

            def GetCategoriesAndScenes():
                Category = None
                Categories = {}

                for Line in ConfigData[3:]:
                    if Line.startswith(b"\x14\x14 "):
                        Category             = Line[10:]
                        Categories[Category] = []
                    if Line.startswith(b"\x14 ") and Category is not None:
                        Categories[Category].append(Line[2:])

                return Categories

            SceneConfigMap = { GetCategoriesAndScenes() }
            return SceneConfigMap
        else:
            print("Can't get scene config data if there isn't a scene config file!!!!!")
            return None

class Scene:
    def __init__(self):
        self.BackgroundColor = None