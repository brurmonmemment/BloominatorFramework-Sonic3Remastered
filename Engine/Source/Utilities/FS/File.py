import os
import shutil
from configparser import ConfigParser

# ======================== #
# General file management  #
# ======================== #
def Exists(Path): return os.path.exists(Path)

def Delete(Path):
    if Exists(Path):
        return os.remove(Path)
    else:
        return False

def Copy(Source, Dest):
    if not Exists(Dest):
        os.mkdir(Dest)
    if Exists(Source):
        return shutil.copy(Source, Dest)
    return False

def Move(Source, Dest):
    if not Exists(Dest):
        os.mkdir(Dest)
    if Exists(Source):
        return shutil.move(Source, Dest)
    return False

def Duplicate(Source, NewName=None, Extension=" (Copy)"):
    _DESTINATION = ""
    if not Exists(Source):
        return False
    _SOURCEFILE_DIR = os.path.dirname(Source)
    _BASE, _EXTENSION = os.path.splitext(os.path.basename(Source))
    if NewName:
        _DESTINATION = os.path.join(_SOURCEFILE_DIR, NewName)
        shutil.copy(Source, str(_DESTINATION))
    else:
        _BASE += Extension
        while Exists(os.path.join(_SOURCEFILE_DIR, _BASE + _EXTENSION)):
            _BASE += Extension
        _BASE_COPY = _BASE + _EXTENSION
        _DESTINATION = os.path.join(_SOURCEFILE_DIR, _BASE_COPY)
        shutil.copy(Source, str(_DESTINATION))
    return _DESTINATION

# ======================== #
# INI management           #
# ======================== #
_P = ConfigParser()
_P.optionxform = str # silly ConfigParser
_CUR_PATH = None

def _CHK_CFG_INI_DATA(Path, IGNORE_CLR_WARN = 1): # ignore = 0, clear = 1, warn = 2
    global _CUR_PATH
    if _CUR_PATH != Path:
        if _P.sections():
            if IGNORE_CLR_WARN == 1:
                _P.clear()
            elif IGNORE_CLR_WARN == 2:
                print("WARNING: ConfigParser already has leftover data, reading multiple files at a time may cause bugs")
            return True
        _CUR_PATH = Path
    return None

def _PARSE_DATA(Value, AUTOPARSE_TUPLES=True):
    if not isinstance(Value, str):
        return Value

    # could be a boolean?
    if Value.lower() == "true":
        return True
    elif Value.lower() == "false":
        return False

    # could be an integer?
    try:
        return int(Value)
    except ValueError:
        pass

    # could be a float?
    try:
        return float(Value)
    except ValueError:
        pass

    # could be a tuple?
    if Value.startswith("(") and Value.endswith(")"):
        _IN = Value[1:-1].strip()
        if not _IN:
            return tuple()

        _ITMS = [_ITM.strip() for _ITM in _IN.split(",")]
        if AUTOPARSE_TUPLES: # I HATE THIS SO MUCH
            _PI = []
            for _ITM in _ITMS:
                try:
                    _PI.append(_PARSE_DATA(_ITM))
                except (TypeError, ValueError):
                    _PI.append(_ITM)
            return tuple(_PI)
        return tuple(_IN)

    # TODO? add more casting, likely not though

    # well it wasn't any of those so :(
    return Value

def ReadSection(Path, Section):
    if not Exists(Path):
        return None
    _CHK_CFG_INI_DATA(Path)
    _P.read(Path)
    if not _P.has_section(Section):
        return None
    return dict(_P.items(Section))

def WriteSection(Path, Section, Data):
    _CHK_CFG_INI_DATA(Path)
    if not _P.has_section(Section):
        _P.add_section(Section)
    for _K, _VAL in Data.items():
        _P.set(Section, _K, str(_VAL)) # like i know it says it in the docs that it has to be a string, but why?
    with open(Path, "w") as Ini:
        _P.write(Ini)
    return True

def ReadKey(Path, Section, Key, Default=None):
    _SECTION = ReadSection(Path, Section)
    if not _SECTION:
        return Default
    return _SECTION.get(Key, Default)

def WriteKey(Path, Section, Key, Value):
    _CHK_CFG_INI_DATA(Path)
    if not _P.has_section(Section):
        _P.add_section(Section)
    _P.set(Section, Key, _PARSE_DATA(Value))
    with open(Path, "w") as Ini:
        _P.write(Ini)
    return True