class Sprite:
    def __init__(self, ID, Layer, Image, Position=(0, 0), Animation=None, Visible=True):
        self.ID        = ID
        self.Layer     = Layer
        self.Image     = Image
        self.Position  = Position
        self.Animation = Animation
        self.Visible   = Visible
        self.Active    = True

    def SetPos(self, Position):
        self.Position = Position

    def ToggleVis(self):
        self.Visible = not self.Visible

    def Unload(self):
        self.Active = False

    def Destroy(self):
        self.Image.Destroy()
        self.Unload()

    def Update(self):
        if self.Animation:
            self.Animation.Update()