import os as OsLib

class Project:
    @staticmethod
    def CheckProjectType():
        IsDataPack   = OsLib.path.exists(OsLib.path.join(OsLib.path.dirname(__file__), "..", "..", "..", Project.Types.PROJECT_DATAPACK))
        IsDataFolder = OsLib.path.isdir(OsLib.path.join(OsLib.path.dirname(__file__), "..", "..", "..", Project.Types.PROJECT_DATAFOLDER))
        if IsDataFolder:
            return "DataFolder"
        elif IsDataPack:
            return "DataPack"
        return "None"

    class Types:
        PROJECT_DATAPACK   = "Data.bsdk"
        PROJECT_DATAFOLDER = "Data"

class Paths:
    BloominatorPath = str(OsLib.path.abspath(OsLib.path.join(OsLib.path.dirname(__file__), "..", "..", ".."))) + "/"
    Engine          = BloominatorPath + "Engine/"
    Project         = BloominatorPath + f"{Project.Types.PROJECT_DATAFOLDER if Project.CheckProjectType() == 'DataFolder' else Project.Types.PROJECT_DATAPACK}/"

class Binaries:
    GameConfig  = "GameConfig.bin"
    SceneConfig = "SceneConfig.bin"