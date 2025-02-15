class Animation:
    def __init__(self, Frames, Delay):
        self.Frames = Frames
        self.Delay = Delay
        self.Time = 0
        self.CurrentFrame = 0
        
    def Update(self, Delta):
        self.Time += Delta

        if self.Time >= self.Delay:
            self.Time = 0
            self.CurrentFrame = (self.CurrentFrame + 1) % len(self.Frames)
            
    def GetCurrentFrame(self):
        return self.Frames[self.CurrentFrame]
