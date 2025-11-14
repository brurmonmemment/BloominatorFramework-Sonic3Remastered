# ======================== #
# Imports                  #
# ======================== #
from Enums.Common.Subsystems import SUBSYSTEMS
import Subsystems.SubsystemAbstractor as SAL
SAL.SetAIOSubsystem(SUBSYSTEMS.AIO.SDL3)
from Subsystems.Common.EventManager import EventManager, FPSCap
from Subsystems.Common.VideoInterface import VideoInterface
from Common.Files.Settings import *

def Run():
    UpdateVideoSettingsFromIni()
    EM = EventManager()
    FPS = FPSCap()
    VI = VideoInterface()
    if VI:
        EM.Running = True
    while EM.IsRunning:
        EM.PollEvents()

        if not EM.IsRunning: # do it early so we dont have to wait another frame
            break

        if FPS.FrameTickOver():
            FPS.UpdateTicks()

            # VI.UpdateScreen()

    VI.Quit()
    FlushVideoSettingsToIni()