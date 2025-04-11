from collections import defaultdict

class Scene:
    def __init__(self, Category, Name, BackgroundColor, TimerEnabled=False, ExecFunctions=None):
        self.Category = Category
        self.Name = Name
        self.BackgroundColor = BackgroundColor
        self.TimerEnabled = TimerEnabled
        self.Timer = {"Minutes": 0, "Seconds": 0, "Frames": 0}
        self.Layers = defaultdict(list)
        self.ExecFunctions = ExecFunctions if ExecFunctions else []

    def AddLayer(self, Layer):
        if Layer not in self.Layers:
            self.Layers[Layer] = []

    def RemoveLayer(self, Layer):
        if Layer in self.Layers:
            del self.Layers[Layer]

    def ToggleLayerVisibility(self, Layer, Visible):
        if Layer in self.Layers:
            if Visible:
                print(f"Layer {Layer} is now Visible.")
            else:
                print(f"Layer {Layer} is now hidden.")

    def UpdateTimer(self):
        if self.TimerEnabled:
            self.Timer["Frames"] += 1
            if self.Timer["Frames"] >= 60:
                self.Timer["Frames"]  = 0
                self.Timer["Seconds"] += 1
            if self.Timer["Seconds"] >= 60:
                self.Timer["Seconds"] = 0
                self.Timer["Minutes"] += 1

    def ExecuteFunctions(self):
        for Function in self.ExecFunctions:
            Function(self)

""" 
--- example of creating a scene
---
--- ExScene = Scene(
---     Category="Gameplay",
---     Name="ExampleScene",
---     BackgroundColor=(255, 255, 255),
---     TimerEnabled=True,
---     ExecFunctions=[lambda scene: print("Example scene started!")]
--- )
---
--- now you can register and use it with SceneManager! 
"""