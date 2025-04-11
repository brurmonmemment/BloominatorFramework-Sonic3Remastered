class SceneConfigData:
    def __init__(self):
        print("Scene Configuration")
        self.CNames = []
        self.Scenes = {}
        self.GetCategories()

    def GetCategories(self):
        CNums = int(input("How many categories do you have? "))
        for CNum in range(CNums):
            self.CName = input(f"What do you want category #{CNum + 1} to be called?: ")
            self.CNames.append(self.CName)
            self.Scenes[self.CName] = self.GetScenes()

    def GetScenes(self):
        Scenes = []
        SNums = int(input(f"How many scenes do you want in {self.CName}? "))
        for SNum in range(SNums):
            SName = input(f"What do you want scene #{SNum + 1} to be called? ")
            SFolder = input(f"And what's the name of the folder that houses the scene (typically in Data/Scenes)? ")
            Scenes.append([SName, SFolder])
        return Scenes

def Write():
    with open("SceneConfig.bin", "wb") as SceneConfigBinary:
        Lines = [
            b"SceneConfig\x00\x00List\x00\x00"
        ]

        SceneData = SceneConfigData()
        for Category in SceneData.CNames:
            Lines.append(f"\x14\x14 {Category}\x00".encode())
            for Scene in SceneData.Scenes[Category]:
                Lines.append(f"\x14 {Scene[0]} - {Scene[1]}\x00".encode())

        for Line in Lines:
            SceneConfigBinary.write(Line)

        print("Created SceneConfig.bin")
        print("Written data: " + str(Lines))


Write()