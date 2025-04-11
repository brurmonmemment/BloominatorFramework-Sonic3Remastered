from Engine.Scripts.Settings.Video.VideoSettings import VideoSettings
from Engine.Scripts.Settings.Game.GameConfig import GameConfig
from ctypes import (c_char_p, c_int, c_ubyte, POINTER)
from Engine.Scripts.Global.Paths import Paths
from sdl3 import (
    IMG_Load, SDL_SetWindowIcon, SDL_SetWindowBordered,
    SDL_SetWindowFullscreen, SDL_CreateWindow, SDL_FALSE, SDL_Window,
    SDL_CreateRenderer, SDL_HideCursor, SDL_WINDOW_FULLSCREEN,
    SDL_RestoreWindow, SDL_GetError, SDL_RenderClear, SDL_RenderPresent,
    SDL_SetRenderLogicalPresentation, SDL_SetRenderDrawBlendMode,
    SDL_LOGICAL_PRESENTATION_INTEGER_SCALE, SDL_BLENDMODE_BLEND, SDL_Renderer,
    SDL_SetRenderDrawColor, SDL_Init, SDL_INIT_VIDEO
)

CurrentWindow    = None
CurrentRenderer  = None

def Init():
    global CurrentWindow
    global CurrentRenderer
    CurrentWindow = CreateWindow()
    if CurrentWindow:
        CurrentRenderer = CreateRenderer(CurrentWindow)

def CreateWindow() -> POINTER(SDL_Window):
    SDL_Init(SDL_INIT_VIDEO)

    Window = SDL_CreateWindow(
        c_char_p(bytes(GameConfig.Name, "utf-8")),
        c_int(VideoSettings.WinWidth), c_int(VideoSettings.WinHeight),
        0
    )

    if not Window:
        print(f"Failed to create Window! {SDL_GetError()}")
        return None

    print("Created Window!")
    ApplyVSettings(Window)
    return Window

def ApplyVSettings(Window):
    if not VideoSettings.Fullscreen:
        SDL_RestoreWindow(Window)
        if not VideoSettings.ExFullscreen:
            SDL_SetWindowFullscreen(Window, SDL_WINDOW_FULLSCREEN)
        SDL_HideCursor()

    if not VideoSettings.Bordered == True:
        SDL_RestoreWindow(Window)
        SDL_SetWindowBordered(Window, SDL_FALSE)

def CreateRenderer(Window) -> POINTER(SDL_Renderer):
    if not Window:
        print("Window is not created!")
        return None

    Renderer = SDL_CreateRenderer(Window, c_char_p(b"gpu"))

    if not Renderer:
        print(f"Failed to create Renderer! {SDL_GetError()}")
        return None

    print("Created Renderer!")

    WindowIconPath = bytes(Paths.Project, "utf-8") + b"Sprites/ProjectIcon.gif"
    SDL_SetWindowIcon(Window, IMG_Load(c_char_p(WindowIconPath)))

    SDL_SetRenderLogicalPresentation(Renderer,
                                     w=c_int(424), h=c_int(240),
                                     mode=SDL_LOGICAL_PRESENTATION_INTEGER_SCALE)
    SDL_SetRenderDrawBlendMode(Renderer, SDL_BLENDMODE_BLEND)

    # visual rendering test
    SDL_SetRenderDrawColor(Renderer,
                           c_ubyte(16), c_ubyte(16), c_ubyte(16),
                           c_ubyte(255))
    SDL_RenderClear(Renderer)
    SDL_RenderPresent(Renderer)

    return Renderer
