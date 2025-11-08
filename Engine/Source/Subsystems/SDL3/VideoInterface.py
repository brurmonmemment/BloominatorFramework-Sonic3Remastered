from typing import Any
from sdl3 import *
from Engine.Source.Structs.Settings.Video import VideoSettings, VS_Lookup
from Engine.Source.Enums.Video.States import WINDOW_STATE

WindowInstance: Any   = None
RendererInstance: Any = None
WindowState: WINDOW_STATE = WINDOW_STATE.PREPARING

# ======================== #
# For simple initializing  #
# ======================== #

def Init():
    if InitSubsystems() and \
       CreateWindow() and \
       CreateRenderer(WindowInstance):
        return True

    return False

# ======================== #
# Core funcs               #
# ======================== #

def InitSubsystems():
    if not SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS):
        return False

    SDL_SetHint(SDL_HINT_RENDER_VSYNC, b"1" if VideoSettings.VSync else b"0") # type: ignore[arg-type]
    return True

def CreateWindow():
    global WindowInstance
    if WindowInstance is not None:
        return False

    Properties = SDL_CreateProperties()
    # core window creation props
    SDL_SetStringProperty(Properties, SDL_PROP_WINDOW_CREATE_TITLE_STRING, "Obama have dih 💔🥀".encode()) # type: ignore[arg-type]
    SDL_SetNumberProperty(Properties, SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER, VS_Lookup("CalculatedW")) # type: ignore[arg-type]
    SDL_SetNumberProperty(Properties, SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER, VS_Lookup("CalculatedH")) # type: ignore[arg-type]

    # external
    SDL_SetBooleanProperty(Properties, SDL_PROP_WINDOW_CREATE_FULLSCREEN_BOOLEAN, VideoSettings.Fullscreen.Enabled) # type: ignore[arg-type]
    SDL_SetBooleanProperty(Properties, SDL_PROP_WINDOW_CREATE_BORDERLESS_BOOLEAN, not VideoSettings.Bordered) # type: ignore[arg-type]

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
    SDL_SetPointerProperty(Properties, SDL_PROP_RENDERER_CREATE_WINDOW_POINTER, Window) # type: ignore[arg-type]
    SDL_SetNumberProperty(Properties, SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_NUMBER, 1 if VideoSettings.VSync else 0) # type: ignore[arg-type] # also this line exists just in case the hint doesn't work

    RendererInstance = SDL_CreateRendererWithProperties(Properties)
    if RendererInstance is None:
        print(f"ERR: Renderer couldn't be created ({SDL_GetError()})")
        return False

    return True

def QuitSubsystem():
    global WindowInstance, RendererInstance

    if RendererInstance:
        SDL_DestroyRenderer(RendererInstance)
        RendererInstance = None
    if WindowInstance:
        SDL_DestroyWindow(WindowInstance)
        WindowInstance = None

    SDL_QuitSubSystem(SDL_INIT_VIDEO | SDL_INIT_EVENTS)
    SDL_Quit()

# ======================== #
# Renderer management      #
# ======================== #
def UpdateScreen():
    # TODO: add proper renderer update logic
    SDL_SetRenderDrawColor(RendererInstance, 0, 255, 0, 255) # type: ignore[arg-type]
    SDL_RenderClear(RendererInstance)
    SDL_RenderPresent(RendererInstance)