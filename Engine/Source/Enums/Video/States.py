# ======================== #
# Imports                  #
# ======================== #
from enum import Enum, auto

class WINDOW_STATE(Enum):
    PREPARING = auto()
    FOCUSED   = auto()
    UNFOCUSED = auto()