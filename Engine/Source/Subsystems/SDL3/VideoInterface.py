# ======================== #
# Imports                  #
# ======================== #
from sdl3 import *
from Structs.Game.Metadata import GameInfo
from Enums.Video.States import WINDOW_STATE
from Structs.Settings.Video import VideoSettings

def _EXISTS(OBJ): return True if OBJ else False

def GetWindowFlags():
    WindowFlags = 0
    if not VideoSettings.Bordered:
        WindowFlags |= SDL_WINDOW_BORDERLESS
    if VideoSettings.Fullscreen.Enabled:
        WindowFlags |= SDL_WINDOW_FULLSCREEN

    return WindowFlags

class WindowObject:
    def __init__(self, Title, Width, Height, Flags):
        self.Title = Title
        self.Width = Width
        self.Height = Height
        self.Flags = Flags
        self.Window = None

        if _EXISTS(self.Window):
            print()

        self.Window = SDL_CreateWindow(
            self.Title.encode(),
            self.Width, self.Height,
            self.Flags
        )

        if not _EXISTS(self.Window):
            print(f"ERR: Window couldn't be created ({SDL_GetError()})")

        SDL_HideCursor()

    @property
    def ptr(self):
        return self.Window

class RendererObject:
    def __init__(self, WindowA: WindowObject):
        self.Window = WindowA
        self.Renderer = None

        if _EXISTS(self.Renderer):
            print()

        SDL_SetHint(SDL_HINT_RENDER_VSYNC, b"1" if VideoSettings.VSync else b"0") # type: ignore

        self.Renderer = SDL_CreateRenderer(self.Window.ptr, None) # type: ignore

        if not _EXISTS(self.Renderer):
            print(f"ERR: Renderer couldn't be created ({SDL_GetError()})")

    @property
    def ptr(self):
        return self.Renderer


# ======================== #
# Window & renderer stuff  #
# ======================== #

class VideoInterface:
    Window: WindowObject | None     = None
    Renderer: RendererObject | None = None
    WindowState: WINDOW_STATE = WINDOW_STATE.PREPARING

    FBWidth = 424
    FBHeight = 240
    # Framebuffer = [[(0, 0, 0) for NOPE in range(FBWidth)] for AGAIN_NOPE in range(FBHeight)]

    @classmethod
    def __init__(cls):
        SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS)

        cls.Window = WindowObject(GameInfo.Title,
                                  VideoSettings.Lookup("CalculatedW"), VideoSettings.Lookup("CalculatedH"),
                                  GetWindowFlags())
        cls.Renderer = RendererObject(cls.Window)

        SDL_SetHint(SDL_HINT_RENDER_VSYNC, b"1" if VideoSettings.VSync else b"0") # type: ignore

    @classmethod
    def Quit(cls):
        if cls.Renderer:
            SDL_DestroyRenderer(cls.Renderer.ptr)
            cls.Renderer = None
        if cls.Window:
            SDL_DestroyWindow(cls.Window.ptr)
            cls.Window = None

        SDL_QuitSubSystem(SDL_INIT_VIDEO | SDL_INIT_EVENTS)
        SDL_Quit()

# ======================== #
# Renderer management      #
# ======================== #