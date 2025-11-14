# ======================== #
# Imports                  #
# ======================== #
from sdl3 import *
from Enums.Video.States import WINDOW_STATE
from Structs.Settings.Video import VideoSettings
import Subsystems.Common.VideoInterface as VideoInterface

# ======================== #
# Session event manager    #
# ======================== #
class EventManager:
    def __init__(self):
        self.Running = False

    def FilterEvent(self, Event):
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
            self.Running = False
        elif Event.type == SDL_EVENT_TERMINATING:
            self.Running = False
        elif Event.type == SDL_EVENT_QUIT:
            self.Running = False

    def PollEvents(self):
        NewEvent = SDL_Event()
        while SDL_PollEvent(NewEvent):
            self.FilterEvent(NewEvent)

    @property
    def IsRunning(self):
        return self.Running

# ======================== #
# FPS capping              #
# ======================== #
class FPSCap:
    def __init__(self):
        self.FrequencyTarget = SDL_GetPerformanceFrequency() / VideoSettings.RefreshRate  # type: ignore
        self.CurrentTicks    = 0
        self.PreviousTicks   = 0

    def FrameTickOver(self):
        self.CurrentTicks = SDL_GetPerformanceCounter()
        return self.CurrentTicks >= self.PreviousTicks + self.FrequencyTarget # type: ignore

    def UpdateTicks(self): self.PreviousTicks = self.CurrentTicks