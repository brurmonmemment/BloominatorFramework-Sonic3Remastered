from sdl3 import (
    SDL_Event, SDL_PollEvent, SDL_HideCursor,
    SDL_WINDOW_FULLSCREEN, SDL_RestoreWindow,
    SDL_SetWindowFullscreen, SDL_EVENT_WINDOW_MAXIMIZED,
    SDL_EVENT_WINDOW_CLOSE_REQUESTED, SDL_Window,
)

class EventProcessor:
    def __init__(self, Window: SDL_Window):
        self.Window  = Window
        self.Running = False

    def Start(self):
        self.Running = True
        while self.Running:
            self.ProcessEvents()

    def ProcessEvents(self):
        Event = SDL_Event()
        while SDL_PollEvent(Event):
            self.ProcessEvent(Event)

    def ProcessEvent(self, Event):
        if Event.type == SDL_EVENT_WINDOW_MAXIMIZED:
            SDL_RestoreWindow(self.Window)
            SDL_SetWindowFullscreen(self.Window, SDL_WINDOW_FULLSCREEN)
            if not SDL_HideCursor():
                SDL_HideCursor()
        elif Event.type == SDL_EVENT_WINDOW_CLOSE_REQUESTED:
            self.Running = False