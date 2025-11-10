import Subsystems.Common.EventManager as EventManager
import Subsystems.Common.VideoInterface as VideoInterface
import Subsystems.SubsystemAbstractor as SAL
from Common.Files.Settings import UpdateVideoSettingsFromIni
from Enums.Common.Subsystems import SUBSYSTEMS

def Run():
    UpdateVideoSettingsFromIni()
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

    VideoInterface.Quit()