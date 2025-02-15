import pathlib as Dir

class GlobalValues:
    class Paths:
        Scripts = Dir.Path().resolve().parent
        Engine = Scripts.parent
        Main = Engine.parent
        Data = Main / "Data"