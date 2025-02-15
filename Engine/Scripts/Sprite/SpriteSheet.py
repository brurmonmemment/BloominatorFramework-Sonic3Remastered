import ctypes
from sdl3 import *

class SpriteSheet:
    def __init__(self, Renderer, Path, FrameWidth, FrameHeight):
        self.Surface = IMG_Load(Path)
        self.Texture = SDL_CreateTextureFromSurface(Renderer, self.Surface)
        SDL_SetTextureScaleMode(self.Texture, SDL_SCALEMODE_NEAREST)
        self.Renderer = Renderer
        self.Width = ctypes.c_int()
        self.Height = ctypes.c_int()
        self.WidthVal = self.Width.value
        self.HeightVal = self.Height.value
        self.FrameWidth = FrameWidth
        self.FrameHeight = FrameHeight
        self.Frames = []
        self.GenFrames()

    def GenFrames(self):
        Columns = self.WidthVal // self.FrameWidth
        Rows = self.HeightVal // self.FrameHeight
        for Row in range(Rows):
            for Column in range(Columns):
                Rectangle = SDL_FRect(Column * self.FrameWidth,
                                     Row * self.FrameHeight,
                                     self.FrameWidth, self.FrameHeight)
                self.Frames.append(Rectangle)
        if not self.Frames:
            self.Frames.append(SDL_FRect(0, 0, self.FrameWidth, self.FrameHeight))