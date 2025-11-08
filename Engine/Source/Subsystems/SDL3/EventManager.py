from sdl3 import *
from Engine.Source.Enums.Video.States import WINDOW_STATE
from Engine.Source.Structs.Settings.Video import VideoSettings
import Engine.Source.Subsystems.Common.VideoInterface as VideoInterface

# ======================== #
# Window events            #
# ======================== #
Running = False

# noinspection PyTypeChecker
def ProcessEvent(Event):
    global Running

    if Event.type == SDL_EVENT_WINDOW_FOCUS_GAINED:
        VideoInterface.WindowState = WINDOW_STATE.FOCUSED
    if Event.type == SDL_EVENT_WINDOW_FOCUS_LOST:
        VideoInterface.WindowState = WINDOW_STATE.UNFOCUSED
    elif Event.type == SDL_EVENT_WINDOW_MAXIMIZED:
        # noinspection PyTypeChecker
        SDL_SetWindowFullscreen(VideoInterface.WindowInstance, True)
        SDL_HideCursor()
        VideoSettings.Fullscreen.Enabled = True
    elif Event.type == SDL_EVENT_WINDOW_CLOSE_REQUESTED:
        Running = False
    elif Event.type == SDL_EVENT_TERMINATING:
        Running = False
    elif Event.type == SDL_EVENT_QUIT:
        Running = False

def ProcessEvents():
    global Running

    NewEvent = SDL_Event()
    while SDL_PollEvent(NewEvent):
        ProcessEvent(NewEvent)

# ======================== #
# FPS capping              #
# ======================== #
FrequencyTarget = None
CurrentTicks    = None
PreviousTicks   = None

def SetupCap():
    global FrequencyTarget, CurrentTicks, PreviousTicks

    FrequencyTarget = SDL_GetPerformanceFrequency() / VideoSettings.RefreshRate  # type: ignore[arg-type]
    CurrentTicks    = 0
    PreviousTicks   = 0

def FrameTickOver():
    global FrequencyTarget, CurrentTicks, PreviousTicks

    CurrentTicks = SDL_GetPerformanceCounter()
    return CurrentTicks >= PreviousTicks + FrequencyTarget

def UpdateTicks():
    global CurrentTicks, PreviousTicks
    PreviousTicks = CurrentTicks