from enum import Enum, auto

# ======================== #
# NOTICE                   #
# ========================================================= #
# The only currently working subsystem(s) as of now are SDL3.
# Everything else is merely dummy values for in case someone
# else wants to take a stab at implementing it.
# ========================================================= #

# ======================== #
# Categorized subsystems   #
# ======================== #
class SUBSYS_AIO(Enum):
    SDL3 = auto()

class SUBSYS_VIDEO(Enum):
    SDL3 = auto()
    OPENGL = auto()
    METAL = auto()
    VULKAN = auto()

class SUBSYS_AUDIO(Enum):
    SDL3 = auto()
    OPENAL = auto()

class SUBSYS_INPUT(Enum):
    SDL3 = auto()
    XINPUT = auto()
    CUSTOM_RAW = auto()

class SUBSYS_EVENTS(Enum):
    SDL3 = auto()

# ======================== #
# Main subsystems class    #
# ======================== #
class SUBSYSTEMS:
    AIO = SUBSYS_AIO
    VIDEO = SUBSYS_VIDEO
    AUDIO = SUBSYS_AUDIO
    INPUT = SUBSYS_INPUT
    EVENTS = SUBSYS_EVENTS