import ctypes

import sdl3
from sdl3 import *
from enum import Enum, auto
from Engine.Scripts.Window.RenderWindow import RenderWindow

class POS_OFFSET:
    def __init__(self, base, offset):
        self.base = base
        self.offset = offset

class SpritePos(Enum):
    SPRITEPOS_HORIZONTAL_LEFT     = auto()
    SPRITEPOS_HORIZONTAL_CENTERED = auto()
    SPRITEPOS_HORIZONTAL_RIGHT    = auto()
    SPRITEPOS_VERTICAL_TOP        = auto()
    SPRITEPOS_VERTICAL_CENTERED   = auto()
    SPRITEPOS_VERTICAL_BOTTOM     = auto()

    # for detecting things like SPRITEPOS_VERTICAL_CENTER - or + a value
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

class Sprite:
    def __init__(self, SpriteSheet, X, Y, Animation=None):
        FrameWidth = SpriteSheet.FrameWidth
        FrameHeight = SpriteSheet.FrameHeight

        self.SpriteSheet = SpriteSheet
        self.Animation = Animation
        self.CurrentFrame = 0

        ScreenWidth = ctypes.c_int()
        ScreenHeight = ctypes.c_int()
        RLPMode = ctypes.c_int() # ughhhhhhhhhhahsdjhajksd
        SDL_GetRenderLogicalPresentation(RenderWindow.Renderer, ScreenWidth, ScreenHeight, RLPMode)

        if isinstance(X, POS_OFFSET): # Process the SPRITEPOS + number check for X
            BaseX = X.base
            OffsetX = X.offset
        else:
            BaseX = X
            OffsetX = 0 # this is for my safety

        if BaseX == SpritePos.SPRITEPOS_HORIZONTAL_LEFT:
            self.X = 0 + OffsetX
        elif BaseX == SpritePos.SPRITEPOS_HORIZONTAL_CENTERED:
            self.X = ((ScreenWidth.value - FrameWidth) // 2) + OffsetX
        elif BaseX == SpritePos.SPRITEPOS_HORIZONTAL_RIGHT:
            self.X = (ScreenWidth.value - FrameWidth) + OffsetX
        else:
            self.X = 0 + OffsetX

        if isinstance(Y, POS_OFFSET):  # Same thang for Y
            BaseY = Y.base
            OffsetY = Y.offset
        else:
            BaseY = Y
            OffsetY = 0

        if BaseY == SpritePos.SPRITEPOS_VERTICAL_TOP:
            self.Y = 0 + OffsetY
        elif BaseY == SpritePos.SPRITEPOS_VERTICAL_CENTERED:
            self.Y = ((ScreenHeight.value - FrameHeight) // 2) + OffsetY
        elif BaseY == SpritePos.SPRITEPOS_VERTICAL_BOTTOM:
            self.Y = (ScreenHeight.value - FrameHeight) + OffsetY
        else:
            self.Y = 0 + OffsetY
        
    def Update(self, Delta):
        if self.Animation:
            self.Animation.Update(Delta)
            
    def Draw(self, Renderer):
        if self.Animation:
            SRCRectangle = self.Animation.GetFrame()
        else:
            SRCRectangle = self.SpriteSheet.Frames[self.CurrentFrame]
        DSTRectangle = SDL_FRect(int(self.X), int(self.Y), SRCRectangle.w, SRCRectangle.h)
        SDL_RenderTexture(Renderer, self.SpriteSheet.Texture, SRCRectangle, DSTRectangle)