# ======================== #
# Imports                  #
# ======================== #
from dataclasses import dataclass
from Enums.Video.Settings import FULLSCREEN

@dataclass
class FullscreenSettings:
    Enabled   = False
    Exclusive = True
    Width     = FULLSCREEN.WIDTH_AUTO
    Height    = FULLSCREEN.HEIGHT_AUTO

@dataclass
class VideoSettings:
    Width                             = 424
    Height                            = 240
    Scale: int | float | tuple | dict = 1
    Bordered                          = True
    VSync                             = True
    Shaders                           = True
    RefreshRate                       = 60

    # FS
    Fullscreen = FullscreenSettings()

    @staticmethod
    def Lookup(Item):
        print(f"[VideoSettings] Looking up {str(Item)}...")

        # help vars
        _SCALE = VideoSettings.Scale

        # helper functions to assist with finding items
        def VS_CalcScreen(Dimension):
            nonlocal _SCALE

            # pluh
            _DIMENSION = getattr(VideoSettings, Dimension.capitalize(), None)
            if _DIMENSION is None:
                return False

            __SCALE = None
            match _SCALE:
                case int() | float():
                    __SCALE = max(_SCALE, 1)
                case (w, h):
                    __SCALE = max(w if Dimension.lower() == "width" else h, 1)
                case {"width": w, "height": h}:
                    __SCALE = max(w if Dimension.lower() == "width" else h, 1)
                case _:
                    __SCALE = 1

            return __SCALE * VideoSettings.Width if Dimension.lower() == "width" else __SCALE * VideoSettings.Height # could be mildly dangerous

        Items = {
            "CalculatedW": VS_CalcScreen("WiDtH"),
            "CalculatedH": VS_CalcScreen("heIGht"),
        }

        try:
            return Items.get(Item)
        except KeyError as err:
            print(f"[VS_lookup] ERR while looking up item: {err}")
            return False