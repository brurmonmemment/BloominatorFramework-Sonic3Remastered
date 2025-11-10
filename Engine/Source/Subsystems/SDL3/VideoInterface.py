from sdl3 import *
from typing import Any
import math, time
from Structs.Game.Metadata import GameInfo
from Enums.Video.States import WINDOW_STATE
from Structs.Settings.Video import VideoSettings

WindowInstance: Any   = None
RendererInstance: Any = None
WindowState: WINDOW_STATE = WINDOW_STATE.PREPARING

# ======================== #
# Window & renderer stuff  #
# ======================== #

# For simple initializing
def Init():
    return InitSubsystems() and \
           CreateWindow() and \
           CreateRenderer(WindowInstance)

def InitSubsystems():
    if not SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS):
        return False

    SDL_SetHint(SDL_HINT_RENDER_VSYNC, bytes(int(VideoSettings.VSync))) # type: ignore
    return True

def CreateWindow():
    global WindowInstance
    if WindowInstance is not None:
        return False

    Properties = SDL_CreateProperties()
    # core window creation props
    SDL_SetStringProperty(Properties, SDL_PROP_WINDOW_CREATE_TITLE_STRING, GameInfo.Title.encode()) # type: ignore
    SDL_SetNumberProperty(Properties, SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER, VideoSettings.Lookup("CalculatedW")) # type: ignore
    SDL_SetNumberProperty(Properties, SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER, VideoSettings.Lookup("CalculatedH")) # type: ignore

    # external
    SDL_SetBooleanProperty(Properties, SDL_PROP_WINDOW_CREATE_FULLSCREEN_BOOLEAN, VideoSettings.Fullscreen.Enabled) # type: ignore
    SDL_SetBooleanProperty(Properties, SDL_PROP_WINDOW_CREATE_BORDERLESS_BOOLEAN, not VideoSettings.Bordered) # type: ignore

    WindowInstance = SDL_CreateWindowWithProperties(Properties)
    if WindowInstance is None:
        print(f"ERR: Window couldn't be created ({SDL_GetError()})")
        return False

    SDL_HideCursor()
    return True

def CreateRenderer(Window: SDL_Window):
    global RendererInstance
    if RendererInstance is not None:
        return False

    Properties = SDL_CreateProperties()

    # core renderer creation props
    SDL_SetPointerProperty(Properties, SDL_PROP_RENDERER_CREATE_WINDOW_POINTER, Window) # type: ignore
    SDL_SetNumberProperty(Properties, SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_NUMBER, 1 if VideoSettings.VSync else 0) # type: ignore # also this line exists just in case the hint doesn't work

    RendererInstance = SDL_CreateRendererWithProperties(Properties)
    if RendererInstance is None:
        print(f"ERR: Renderer couldn't be created ({SDL_GetError()})")
        return False

    return True

# ======================== #
# Renderer management      #
# ======================== #
def UpdateScreen():
    # TEMP UPDATE, will be replaced later once we are able to draw stuff
    timey    = time.time()
    RGBRed   = int((math.sin(timey) * 0.5 + 0.5) * 255)
    RGBGreen = int((math.sin(timey * 2) * 0.5 + 0.5) * 255)
    RGBBlue  = int((math.sin(timey * 4) * 0.5 + 0.5) * 255)
    SDL_SetRenderDrawColor(RendererInstance, RGBRed, RGBGreen, RGBBlue, 255) # type: ignore
    SDL_RenderClear(RendererInstance)
    SDL_RenderPresent(RendererInstance)

# ======================== #
# Quit                     #
# ======================== #
def Quit():
    global WindowInstance, RendererInstance

    if RendererInstance:
        SDL_DestroyRenderer(RendererInstance)
        RendererInstance = None
    if WindowInstance:
        SDL_DestroyWindow(WindowInstance)
        WindowInstance = None

    SDL_QuitSubSystem(SDL_INIT_VIDEO | SDL_INIT_EVENTS)
    SDL_Quit()