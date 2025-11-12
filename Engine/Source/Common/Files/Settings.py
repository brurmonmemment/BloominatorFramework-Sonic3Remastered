import os
from Structs.Settings.Video import VideoSettings
from Utilities.FS.File import ReadSection, WriteSection, WriteKey, UpdateCurrentPath

SettingsFile = "Settings.ini"
FullPath = os.path.join(os.getcwd(), SettingsFile)

def UpdateVideoSettingsFromIni():
    UpdateCurrentPath(FullPath)
    Video = ReadSection("Video")
    if not Video:
        return False
    for Key, Value in Video.items():
        setattr(VideoSettings, Key, Value)
    Fullscreen = ReadSection("Video.Fullscreen")
    if not Fullscreen:
        return False
    for Key, Value in Fullscreen.items():
        setattr(VideoSettings.Fullscreen, Key, Value)
    return True

def FlushVideoSettingsToIni(): # same thing but in reverse essentially
    UpdateCurrentPath(FullPath)
    WriteSection( "Video", {
        "Width": VideoSettings.Width,
        "Height": VideoSettings.Height,
        "Bordered": VideoSettings.Bordered,
        "VSync": VideoSettings.VSync,
        "Shaders": VideoSettings.Shaders,
        "RefreshRate": VideoSettings.RefreshRate
    })
    WriteSection( "Video.Fullscreen", {
        "Enabled": VideoSettings.Fullscreen.Enabled,
        "Exclusive": VideoSettings.Fullscreen.Exclusive
    })

    # optional vals
    if VideoSettings.Scale:
        WriteKey("Video", "Scale", VideoSettings.Scale)

    if VideoSettings.Fullscreen.Width:
        WriteKey("Video.Fullscreen", "Width", VideoSettings.Fullscreen.Width)
    if VideoSettings.Fullscreen.Height:
        WriteKey("Video.Fullscreen", "Height", VideoSettings.Fullscreen.Height)