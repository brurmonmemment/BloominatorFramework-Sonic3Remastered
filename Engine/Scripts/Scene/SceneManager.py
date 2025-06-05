from ctypes import c_ubyte
from Engine.Scripts.SDL3 import WindowManager
from sdl3 import SDL_SetRenderDrawColor, SDL_RenderClear, SDL_RenderPresent

def ApplyBackgroundColor(Color):
    SDL_SetRenderDrawColor(WindowManager.Renderer,
                           c_ubyte(Color[0]), c_ubyte(Color[1]), c_ubyte(Color[2]), c_ubyte(255))
    SDL_RenderClear(WindowManager.Renderer)
    SDL_RenderPresent(WindowManager.Renderer)

Categories  = {}
ActiveScene = None

def FetchScenes(Scene):
    global Categories
    Categories[Scene.Category][Scene.Name] = Scene

def SetActiveScene(Category, SceneName):
    global ActiveScene
    if Category in Categories and SceneName in Categories[Category]:
        ActiveScene = Categories[Category][SceneName]
        print(f"Activated Scene {SceneName} from Category {Category}")
        ApplyBackgroundColor(ActiveScene.BackgroundColor)
        ActiveScene.ExecuteFunctions()