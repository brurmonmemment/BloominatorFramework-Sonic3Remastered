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
        _MODULE = importlib.import_module(GetModulePathFromCurrentSubsystemType("Events"))
    return getattr(_MODULE, ClassName)

# ======================== #
# Stubs                    #
# ======================== #
EventManager = _GET_CLASS("EventManager")
FPSCap       = _GET_CLASS("FPSCap")