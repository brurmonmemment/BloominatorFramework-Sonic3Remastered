from sdl3 import *

from Engine.Source.Structs.Settings.Video import VideoSettings
from Engine.Source.Subsystems.SDL3.VideoInterface import WindowInstance

Running = False

# ======================== #
# Event management funcs   #
# ======================== #

# noinspection PyTypeChecker
def ProcessEvent(Event):
    global Running

    if Event.type == SDL_EVENT_WINDOW_MAXIMIZED:
        # noinspection PyTypeChecker
        SDL_SetWindowFullscreen(WindowInstance, True)
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