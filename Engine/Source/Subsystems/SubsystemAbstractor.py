# ======================== #
# Imports                  #
# ======================== #
from enum import Enum
from typing import Optional
from Enums.Common.Subsystems import SUBSYSTEMS

SS_TYPES = ["AIO", "Video", "Audio", "Input", "Events"]
CurrentSubsystems: dict[str, Optional[Enum]] = {SSYS: None for SSYS in SS_TYPES}

AIO_MAP = {
    SUBSYSTEMS.AIO.SDL3: { # map VAIE to SDL3, open as seen here to allow for mix and matching if you wanted to
        SS_TYPES[1]:  SUBSYSTEMS.VIDEO.SDL3,
        SS_TYPES[2]:  SUBSYSTEMS.AUDIO.SDL3,
        SS_TYPES[3]:  SUBSYSTEMS.INPUT.SDL3,
        SS_TYPES[4]: SUBSYSTEMS.EVENTS.SDL3,
    }
}

SCRIPT_MAP = {
    SS_TYPES[1]: "VideoInterface",
    SS_TYPES[2]: "AudioInterface",
    SS_TYPES[3]: "InputProcesser",
    SS_TYPES[4]: "EventManager"
}

_FALLBACK_SUBSYS = SUBSYSTEMS.AIO.SDL3

_MP_CACHE = {}

# ======================== #
# Get helpers              #
# ======================== #
def GetCurrentSubsystem(Type, Fallback=None) -> Optional[SUBSYSTEMS]: return CurrentSubsystems.get(Type, Fallback) # so pycharm is hapi

def GetModulePathFromCurrentSubsystemType(Type):
    if Type in _MP_CACHE:
        return _MP_CACHE[Type]

    _CURRENT_SUBSYS = GetCurrentSubsystem(Type)
    if _CURRENT_SUBSYS is None:
        print("ERR: No subsystem found, cannot get module")
        return None

    SubsystemFolder = _CURRENT_SUBSYS.name # type: ignore
    Script = SCRIPT_MAP.get(Type, "ScriptName")

    ModulePath = f"Subsystems.{SubsystemFolder}.{Script}"
    _MP_CACHE[Type] = ModulePath
    return ModulePath

# ======================== #
# Setter helpers           #
# ======================== #
def SetAIOSubsystem(Subsystem: SUBSYSTEMS.AIO):
    print("Current subsystem is " + str(CurrentSubsystems["AIO"]))
    print("Attempting to switch AIO subsystems...")
    CurrentSubsystems["AIO"] = Subsystem

    _MAP = AIO_MAP.get(Subsystem, AIO_MAP[_FALLBACK_SUBSYS]).items()
    for Key, Value in _MAP:
        CurrentSubsystems[Key] = Value
        print(f"Set {str(Value)} to {str(Key)}")
    if not Subsystem in SUBSYSTEMS.AIO: # goes back around to line 4
        print("WARNING: AIO subsys does not exist! Will fall back to SDL3")

    print("New subsystem is " + str(CurrentSubsystems["AIO"]))
    return True

def SetSubsystem(Type: str, Subsystem: Enum): # i love python
    if Type not in CurrentSubsystems:
        print("ERR: Subsystem type does not exist")
        return False

    CurrentSubsystems[Type] = Subsystem
    print(f"Set {Type} subsystem to {str(Subsystem)}")
    return True