import os as OsLib
from Engine.Bootstrapper.Bootstrapper import ProjectTypes, CheckProjectType

class Paths:
    BloominatorPath = str(OsLib.path.abspath(OsLib.path.join(OsLib.path.dirname(__file__), "..", "..", ".."))) + "/"
    Engine          = BloominatorPath + "Engine/"
    Project         = BloominatorPath + f"{ProjectTypes.PROJECT_DATAFOLDER if CheckProjectType() == 'DataFolder' else ProjectTypes.PROJECT_DATAPACK}/"