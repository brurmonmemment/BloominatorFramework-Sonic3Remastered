import Engine.Source.Subsystems.Common.EventManager as EventManager
import Engine.Source.Subsystems.Common.VideoInterface as VideoInterface
import Engine.Source.Subsystems.SubsystemAbstractor as SAL
from Engine.Source.Enums.Common.Subsystems import SUBSYSTEMS

def Run():
    SAL.SetAIOSubsystem(SUBSYSTEMS.AIO.SDL3)
    if VideoInterface.Init():
        EventManager.Running = True

    EventManager.SetupCap()

    while EventManager.Running:
        EventManager.ProcessEvents()
        if not EventManager.Running: # do it early so we dont have to wait another frame
            break

        if EventManager.FrameTickOver():
            EventManager.UpdateTicks()

            VideoInterface.UpdateScreen()