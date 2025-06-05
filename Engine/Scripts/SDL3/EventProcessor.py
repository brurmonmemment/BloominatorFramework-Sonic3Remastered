from Engine.Scripts.Global.Logging import Logging
from Engine.Scripts.SDL3 import WindowManager
from ctypes import c_bool
from sdl3 import (
    SDL_Event, SDL_PollEvent, SDL_HideCursor,
    SDL_RestoreWindow, SDL_SetWindowFullscreen,
    SDL_EVENT_WINDOW_MAXIMIZED,
    SDL_EVENT_WINDOW_CLOSE_REQUESTED,
)

Running = False

def Start():
    global Running
    Running = True
    while Running:
        ProcessEvents()

def ProcessEvents():
    Event = SDL_Event()
    while SDL_PollEvent(Event):
        ProcessEvent(Event)

def ProcessEvent(Event):
    global Running
    if Event.type == SDL_EVENT_WINDOW_MAXIMIZED:
        SDL_RestoreWindow(WindowManager.Window)
        SDL_SetWindowFullscreen(WindowManager.Window, c_bool(False))
        if not SDL_HideCursor():
            SDL_HideCursor()
        Logging.PrintConsole("Event Processor", "Info", "Maximized window")
    elif Event.type == SDL_EVENT_WINDOW_CLOSE_REQUESTED:
        Running = False
        Logging.PrintConsole("Event Processor", "Task", "Closing window...")