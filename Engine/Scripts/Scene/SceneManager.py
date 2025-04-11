from ctypes import c_ubyte
from sdl3 import SDL_SetRenderDrawColor, SDL_RenderClear, SDL_RenderPresent
from collections import defaultdict
from Engine.Scripts.SDL3 import WindowManager


def ApplyBackgroundColor(Color):
    SDL_SetRenderDrawColor(WindowManager.CurrentRenderer,
                           c_ubyte(Color[0]), c_ubyte(Color[1]), c_ubyte(Color[2]), c_ubyte(255))
    SDL_RenderClear(WindowManager.CurrentRenderer)
    SDL_RenderPresent(WindowManager.CurrentRenderer)


class SceneManager:
    def __init__(self):
        self.Categories = defaultdict(dict)
        self.ActiveScene = None

    def RegisterScene(self, Scene):
        self.Categories[Scene.Category][Scene.Name] = Scene

    def SetActiveScene(self, Category, SceneName):
        if Category in self.Categories and SceneName in self.Categories[Category]:
            self.ActiveScene = self.Categories[Category][SceneName]
            print(f"Activated Scene {SceneName} from Category {Category}")
            ApplyBackgroundColor(self.ActiveScene.BackgroundColor)

    def Update(self):
        if self.ActiveScene:
            self.ActiveScene.UpdateTimer()
            self.ActiveScene.ExecuteFunctions()