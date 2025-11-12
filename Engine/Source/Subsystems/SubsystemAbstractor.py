from enum import Enum
from typing import Optional

from Enums.Common.Subsystems import SUBSYSTEMS

CurrentSubsystems: dict[str, Optional[Enum]] = {SSYS: None for SSYS in ["AIO", "Video", "Audio", "Input", "Events"]}

AIO_MAP = {
    SUBSYSTEMS.AIO.SDL3: { # map VAIE to SDL3, open as seen here to allow for mix and matching if you wanted to
        "Video":  SUBSYSTEMS.VIDEO.SDL3,
        "Audio":  SUBSYSTEMS.AUDIO.SDL3,
        "Input":  SUBSYSTEMS.INPUT.SDL3,
        "Events": SUBSYSTEMS.EVENTS.SDL3,
    }
}

SCRIPT_MAP = {
    "Video": "VideoInterface",
    "Audio": "AudioInterface",
    "Input": "InputProcesser",
    "Events": "EventManager"
}

_DEFAULT_SUBSYS = SUBSYSTEMS.AIO.SDL3

# ======================== #
# Setter helpers           #
# ======================== #
def SetAIOSubsystem(Subsystem: SUBSYSTEMS.AIO):
    print("Current subsystem is " + str(CurrentSubsystems["AIO"]))
    print("Attempting to switch AIO subsystems...")
    CurrentSubsystems["AIO"] = Subsystem

    try:
        for Key, Value in AIO_MAP[Subsystem].items():
            CurrentSubsystems[Key] = Value
            print(f"Set {str(Value)} to {str(Key)}")
    except KeyError:
        print("WARNING: AIO subsys does not exist! Will fall back to SDL3")
        for Key, Value in AIO_MAP[_DEFAULT_SUBSYS].items():
            CurrentSubsystems[Key] = Value

    print("New subsystem is " + str(CurrentSubsystems["AIO"]))
    return True

def SetSubsystem(Type: str, Subsystem: Enum): # i love python
    if Type not in CurrentSubsystems:
        print("ERR: Subsystem type does not exist")
        return False

    CurrentSubsystems[Type] = Subsystem
    print(f"Set {str(Type)} subsystem to {str(Subsystem)}")
    return True

# ======================== #
# Get helpers              #
# ======================== #
def GetCurrentSubsystem(Type) -> Optional[SUBSYSTEMS]: return CurrentSubsystems.get(Type, None) # so pycharm is hapi

def GetModulePathFromCurrentSubsystemType(Type):
    _CURRENT_SUBSYS = GetCurrentSubsystem(Type)
    if _CURRENT_SUBSYS is None:
        print("ERR: No subsystem found, cannot get module")
        return False

    SubsystemFolder = _CURRENT_SUBSYS.name # type: ignore
    Script = SCRIPT_MAP.get(Type, "ScriptName")

    ModulePath = f"Subsystems.{SubsystemFolder}.{Script}"
    return ModulePath