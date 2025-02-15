from sdl3 import *
from Engine.Scripts.Sprite.Font import Font
from Engine.Scripts.GlobalValues import GlobalValues
from Engine.Scripts.Sprite.SpriteSheet import SpriteSheet
from Engine.Scripts.Sprite.Sprite import Sprite, SpritePos
from Engine.Scripts.Window.RenderWindow import RenderWindow

class BloominatorSplash:
    @staticmethod
    def Load():
        Renderer = RenderWindow.Renderer
        if not Renderer:
            return

        LogoS = SpriteSheet(Renderer, bytes(str(GlobalValues.Paths.Engine) + "/Images/BloominatorIcn.png", "utf-8"), 48, 48)

        Logo = Sprite(LogoS, SpritePos.SPRITEPOS_HORIZONTAL_CENTERED, SpritePos.SPRITEPOS_VERTICAL_CENTERED - 2)

        SDL_SetRenderDrawColor(Renderer, 15, 15, 15, 255)
        SDL_RenderClear(Renderer)

        Logo.Draw(Renderer)
        FontS = Font(Renderer, bytes(str(GlobalValues.Paths.Engine) + "/Images/Font.gif", "utf-8"), "Small")
        FontS.RenderText("NO GAME FOUND!", 3, 2)
        FontS.RenderText("NO GAME FOUND!", 3, 2)
        FontS.RenderText("NO GAME FOUND!", 3, 2)
        SDL_RenderPresent(Renderer)