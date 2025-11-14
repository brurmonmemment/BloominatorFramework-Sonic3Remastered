# ======================== #
# Imports                  #
# ======================== #
import importlib
from Subsystems.SubsystemAbstractor import GetModulePathFromCurrentSubsystemType
# ======================== #
# Helper boy               #
# ======================== #
_MODULE = None
def _GET_CLASS(ClassName):
    global _MODULE
    if not _MODULE: # probably haven't already cached the module so actually import it
        _MODULE = importlib.import_module(GetModulePathFromCurrentSubsystemType("Video"))
    return getattr(_MODULE, ClassName)

# ======================== #
# Stubs                    #
# ======================== #
VideoInterface = _GET_CLASS("VideoInterface")