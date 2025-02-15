import sys
from Engine.Scripts.GlobalValues import GlobalValues
from Engine.Scripts.Window.VideoSettings import VideoSettings
from Engine.Scripts.User.Core import UserCore
try:
    from sdl3 import *
except ImportError:
    print("Ya need SDL3 silly!")

class RenderWindow:
    Window = None
    Renderer = None

    def __init__(self): print("Run the Init() function dumbahh")

    @staticmethod
    def Init():
        SDL_InitSubSystem(SDL_INIT_VIDEO | SDL_INIT_EVENTS)

        UserCore.LoadSettings()

        if RenderWindow.CreateWindow() and RenderWindow.CreateRenderer():
            return True
        else:
            return False

    @staticmethod
    def CreateWindow():
        SDL_SetHint(SDL_HINT_RENDER_VSYNC, b"1" if VideoSettings.VSync else b"0")

        Window = SDL_CreateWindow(
            b"Bloominator Framework", # title
            VideoSettings.WinWidth, VideoSettings.WinHeight, # width n height
            4 # flags
        )

        if not Window:
            print(f"ERROR! Failed to create window. {SDL_GetError()}")
            return False

        if not VideoSettings.Windowed:
            SDL_RestoreWindow(Window)
            SDL_SetWindowFullscreen(Window, SDL_WINDOW_FULLSCREEN_DESKTOP)
            SDL_HideCursor()

        if not VideoSettings.Bordered:
            SDL_RestoreWindow(Window)
            SDL_SetWindowBordered(Window, SDL_FALSE)

        RenderWindow.Window = Window
        return Window

    @staticmethod
    def CreateRenderer():
        Window = RenderWindow.Window
        Renderer = SDL_CreateRenderer(
            Window,
            None
        )

        if not Renderer:
            print(f"ERROR! Failed to create renderer. {SDL_GetError()}")
            return False

        # window icon shiz
        SDL_WindowIcon = IMG_Load(bytes(str(GlobalValues.Paths.Engine) + "/Images/BloominatorIcn.png", "utf-8"))
        SDL_SetWindowIcon(Window, SDL_WindowIcon)

        SDL_RenderClear(Renderer)
        SDL_RenderPresent(Renderer)
        SDL_SetRenderLogicalPresentation(Renderer, w=VideoSettings.PixWidth, h=240, mode=SDL_LOGICAL_PRESENTATION_INTEGER_SCALE)
        SDL_SetRenderDrawBlendMode(Renderer, SDL_BLENDMODE_BLEND)

        RenderWindow.Renderer = Renderer
        return Renderer

# Don't mind this comment this is because I'm using pycharm lol!
# noinspection PyGlobalUndefined
class FPSCap:
    TargetFrequency = None
    CurrentTicks    = None
    PreviousTicks   = None

    @staticmethod
    def InitCap():
        global TargetFrequency
        global CurrentTicks
        global PreviousTicks
        TargetFrequency = SDL_GetPerformanceFrequency() / VideoSettings.RefreshRate
        CurrentTicks = 0
        PreviousTicks = 0

    @staticmethod
    def CheckCap():
        global CurrentTicks

        CurrentTicks = SDL_GetPerformanceCounter()
        if CurrentTicks >= (PreviousTicks + TargetFrequency):
            return True
        else:
            return False

    @staticmethod
    def UpdateCap():
        global PreviousTicks

        PreviousTicks = CurrentTicks

class WindowEvents: # insp by retro engine
    WindowRunning = False

    @staticmethod
    def ProcessEvent(Event):
        if Event.type == SDL_EVENT_WINDOW_MAXIMIZED:
            SDL_RestoreWindow(Window)
            SDL_SetWindowFullscreen(Window, SDL_WINDOW_FULLSCREEN_DESKTOP)
            SDL_HideCursor()
            VideoSettings.Windowed = False
        elif Event.type == SDL_EVENT_WINDOW_CLOSE_REQUESTED:
            WindowEvents.WindowRunning = False
        # I'm probably not going to add a lost focus state like in the Retro Engine
        # But if I really changed my mind and wanted to, I could probably uncomment this code
        # elif event.window.event == SDL_EVENT_WINDOW_FOCUS_GAINED:
        #    FocusState = 0
        # elif event.window.event == SDL_EVENT_WINDOW_FOCUS_LOST:
        #    FocusState = 1

    @staticmethod
    def ProcessEvents():
        SDLEvent = SDL_Event()

        while SDL_PollEvent(SDLEvent):
            WindowEvents.ProcessEvent(SDLEvent)