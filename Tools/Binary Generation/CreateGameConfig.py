class GameConfigData:
    ProjectName      = input("What's the name of your game? ").encode()
    ProjectVersion   = input("And the current version? ").encode()
    ProjectSceneData = input("What's the name of your scene configuration file (you can make one with the CreateSceneConfig script)? ").encode()

    # class Categories:
        # def __init__(self):
        #     print("Scene List")
        #     self.CNames = []
        #     self.Scenes = {}
        #     self.GetCategories()

        # def GetCategories(self):
        #     CNums = int(input("How many categories do you have? "))
        #     for CNum in range(CNums):
        #         self.CName = input(f"What do you want category #{CNum + 1} to be called?: ")
        #         self.CNames.append(self.CName)
        #         self.Scenes[self.CName] = self.GetScenes()
        #
        # def GetScenes(self):
        #     Scenes = []
        #     SNums = int(input(f"How many scenes do you want in {self.CName}? "))
        #     for SNum in range(SNums):
        #         SName = input(f"What do you want scene #{SNum + 1} to be called? ")
        #         Scenes.append(SName)
        #     return Scenes

def Write():
    with open("GameConfig.bin", "wb") as GameConfigBinary:
        Lines = [
            b"GameConfig\x00\x00Game Info\x00\x00",
            f"{GameConfigData.ProjectName}\x00v{GameConfigData.ProjectVersion}\x00\x00".encode(),
            b"Scene Data\x00\x00",
            f"File: {GameConfigData.ProjectSceneData}\x00\x00".encode(),
        ]

        # SceneData = GameConfigData.Categories()
        # for Category in SceneData.CNames:
        #     Lines.append(f"-- {Category}\x00".encode())
        #     for Scene in SceneData.Scenes[Category]:
        #         Lines.append(f"- {Scene}\x00".encode())

        for Line in Lines:
            GameConfigBinary.write(Line)

        print("Created GameConfig.bin")
        print("Written data: " + str(Lines))

Write()