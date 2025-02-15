import ctypes
from sdl3 import *
from enum import Enum, auto
from Engine.Scripts.Window.RenderWindow import RenderWindow

# Textpos comiong soon
class POS_OFFSET:
    def __init__(self, base, offset):
        self.base = base
        self.offset = offset

class TextPos(Enum):
    TEXTPOS_HORIZONTAL_LEFT     = auto()
    TEXTPOS_HORIZONTAL_CENTERED = auto()
    TEXTPOS_HORIZONTAL_RIGHT    = auto()
    TEXTPOS_VERTICAL_TOP        = auto()
    TEXTPOS_VERTICAL_CENTERED   = auto()
    TEXTPOS_VERTICAL_BOTTOM     = auto()

    # for detecting things like TEXTPOS_VERTICAL_CENTER - or + a value
    def EnumArithmeticCheckA(self, other):
        if isinstance(other, int):
            return POS_OFFSET(self, other)
        return NotImplemented

    def EnumArithmeticCheckS(self, other):
        if isinstance(other, int):
            return POS_OFFSET(self, -other)
        return NotImplemented

    __add__ = __radd__ = EnumArithmeticCheckA
    __sub__ = __rsub__ = EnumArithmeticCheckS
    
class Font:
    def __init__(self, Renderer, Path, Type):
        if Type == "Small":
            self.CharWidth = 8
            self.CharHeight = 8
            self.Columns = 17
        self.Renderer = Renderer
        self.Path = Path
        self.Surface = IMG_Load(Path)
        SDL_SetSurfaceColorKey(self.Surface, SDL_TRUE, SDL_MapRGB(SDL_GetPixelFormatDetails(self.Surface.contents.format), SDL_GetSurfacePalette(self.Surface), 255, 0, 255)) # no bink
        self.Texture = SDL_CreateTextureFromSurface(Renderer, self.Surface)
        SDL_SetTextureScaleMode(self.Texture, SDL_SCALEMODE_NEAREST)
        Width = ctypes.c_float()
        Height = ctypes.c_float()
        SDL_GetTextureSize(self.Texture, ctypes.byref(Width), ctypes.byref(Height))
        self.WidthVal = Width.value
        self.HeightVal = Height.value
        self.CharRange = """          *+,-./'0123456789:;(=)?" ABCDEFGHIJKLMNO PQRSTUVWXYZ[\\]^_!"""
        self.Mapping = {}
        for I, Character in enumerate(self.CharRange):
            self.Mapping[Character] = I
        self.Frames = []
        self.GenFrames()

    def GenFrames(self):
        CellWidth = self.CharWidth + 1
        CellHeight = self.CharHeight + 1
        TotalChars = len(self.CharRange)
        for I in range(TotalChars):
            Row = I // self.Columns
            Column = I % self.Columns
            X = (Column * CellWidth) + 1
            Y = (Row * CellHeight) + 1
            rect = SDL_FRect(float(X), float(Y), float(self.CharWidth), float(self.CharHeight))
            self.Frames.append(rect)

    def RenderText(self, Text, X, Y):
        CurrentX = X
        CurrentY = Y
        for Character in Text:
            if Character == "\n":
                CurrentY += self.CharHeight
                CurrentX = X
                continue
            IDX = self.Mapping.get(Character)
            if IDX is None:
                CurrentX += self.CharWidth
                continue
            SourceRectangle = self.Frames[IDX]
            DestinationRectangle = SDL_FRect(float(CurrentX), float(CurrentY), SourceRectangle.w, SourceRectangle.h)
            SDL_RenderTexture(self.Renderer, self.Texture, SourceRectangle, DestinationRectangle)
            CurrentX += self.CharWidth
