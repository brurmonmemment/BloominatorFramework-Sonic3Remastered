# ======================== #
# Imports                  #
# ======================== #
from enum import Enum, auto

class LEVELS(Enum):
    INFO      = auto()
    WARNING   = auto()
    ERROR     = auto()
    SUCCESS   = auto()
    IMPORTANT = auto()
    VERBOSE   = auto()