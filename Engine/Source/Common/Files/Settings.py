import os
from Structs.Settings.Video import VideoSettings
from Utilities.FS.File import ReadSection, ReadKey, WriteSection, WriteKey

SettingsFile = "Settings.ini"
FullPath = os.path.join(os.getcwd(), SettingsFile)

VS_TYPE_MAP = {
    "Width": int,
    "Height": int,
    "Scale": int | float | tuple | dict,
    "Bordered": lambda v: v.lower() == "true", # 400 iq move
    "VSync": lambda v: v.lower() == "true",
    "Shaders": lambda v: v.lower() == "true",
    "RefreshRate": int
}

def UpdateVideoSettingsFromIni():
    Video = ReadSection(FullPath, "Video")
    for Key, Value in Video.items():
        setattr(VideoSettings, Key, VS_TYPE_MAP[Key](Value))

UpdateVideoSettingsFromIni()