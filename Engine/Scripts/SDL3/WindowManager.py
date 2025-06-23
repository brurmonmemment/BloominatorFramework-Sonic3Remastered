ShowDFText = True

from Engine.Scripts.Settings.Video.VideoSettings import VideoSettings
from Engine.Scripts.Settings.Game.GameConfig import GameConfig
from Engine.Scripts.Global.Logging import Logging
from Engine.Scripts.Global.Constants import Paths
import os as OsLib
from sdl3 import (
    SDL_SetWindowTitle, SDL_HideWindow,
    IMG_Load, SDL_SetWindowIcon, SDL_SetWindowBordered,
    SDL_CreateRenderer, SDL_HideCursor, SDL_RestoreWindow,
    SDL_SetWindowFullscreen, SDL_CreateWindow, SDL_INIT_VIDEO,
    SDL_GetError, SDL_RenderClear, SDL_RenderPresent, SDL_Init,
    SDL_LOGICAL_PRESENTATION_INTEGER_SCALE, SDL_BLENDMODE_BLEND,
    SDL_SetRenderLogicalPresentation, SDL_SetRenderDrawBlendMode,
)

Window   = None
Renderer = None

def Init():
    CreateWindow()
    CreateRenderer()

def ApplyVSettings():
    if not VideoSettings.Fullscreen:
        SDL_RestoreWindow(Window)

        if not VideoSettings.ExFullscreen:
            SDL_SetWindowFullscreen(Window, True)

        SDL_HideCursor()

    if not VideoSettings.Bordered == True:
        SDL_RestoreWindow(Window)
        SDL_SetWindowBordered(Window, False)

    Logging.PrintConsole("Window Manager", "Info", "Applied video settings to the newly created window")
    Logging.PrintConsole("Window Manager", "Info",f"Video settings:")
    Logging.PrintConsole("Window Manager", "Info", f" - Width: {VideoSettings.WinWidth}, Height: {VideoSettings.WinHeight}, Viewport Width: {VideoSettings.ViewportWidth} ({    int(s) if (s := VideoSettings.WinWidth / VideoSettings.ViewportWidth).is_integer() else round(s, 2)}x Window Scale)")
    Logging.PrintConsole("Window Manager", "Info", f" - Bordered: {VideoSettings.Bordered}, {"(Exclusive)" if VideoSettings.ExFullscreen else ""} Fullscreen: {VideoSettings.Fullscreen}")
    Logging.PrintConsole("Window Manager", "Info", f" - Refresh Rate: {VideoSettings.RefreshRate}")

def CreateWindow():
    global Window
    Logging.PrintConsole("Window Manager", "Task", f"Creating a window...")

    SDL_Init(SDL_INIT_VIDEO)

    Window = SDL_CreateWindow(
        bytes(GameConfig.Name + (" (Data Folder)" if OsLib.path.isdir(Paths.Project) and ShowDFText else ""), "utf-8"),
        VideoSettings.WinWidth, VideoSettings.WinHeight,
        0
    )

    WindowIconPath = bytes(Paths.BloominatorPath + GameConfig.Icon, "utf-8")
    SDL_SetWindowIcon(Window, IMG_Load(WindowIconPath))

    # hide till done
    SDL_HideWindow(Window)

    if not Window:
        Logging.PrintConsole("Window Manager", "Error", f"Failed to create window! {SDL_GetError()}")
        exit(0)

    Logging.PrintConsole("Window Manager", "Success", "Successfully created a new window!")
    Logging.PrintConsole("Window Manager", "Info", "Window configuration: ")
    Logging.PrintConsole("Window Manager", "Info", f" - Title: {GameConfig.Name} ")
    Logging.PrintConsole("Window Manager", "Info", " - Window icon path: " + str(WindowIconPath)[2:-1]) # not today, b''
    ApplyVSettings()

def UpdateWindowTitle(Title):
    SDL_SetWindowTitle(Window, bytes(Title + (" (Data Folder)" if OsLib.path.isdir(Paths.Project) and ShowDFText else ""), "utf-8"))

def UpdateWindowIcon(IconPath):
    WindowIconPath = bytes(Paths.BloominatorPath + str(IconPath), "utf-8")
    SDL_SetWindowIcon(Window, IMG_Load(WindowIconPath))

def CreateRenderer():
    global Renderer
    Logging.PrintConsole("Window Manager", "Task", f"Creating a renderer...")

    if not Window:
        Logging.PrintConsole("Window Manager", "Error", "No existing window found!")
        exit(0)

    Renderer = SDL_CreateRenderer(Window, b"gpu")

    if not Renderer:
        Logging.PrintConsole("Window Manager", "Error", f"Failed to create renderer! {SDL_GetError()}")
        exit(0)

    Logging.PrintConsole("Window Manager", "Success", "Created renderer!")

    SDL_SetRenderLogicalPresentation(Renderer,
                                     w=VideoSettings.ViewportWidth, h=VideoSettings.WinHeight // (VideoSettings.WinWidth // VideoSettings.ViewportWidth),
                                     mode=SDL_LOGICAL_PRESENTATION_INTEGER_SCALE)
    SDL_SetRenderDrawBlendMode(Renderer, SDL_BLENDMODE_BLEND)

    SDL_RenderClear(Renderer)
    SDL_RenderPresent(Renderer)