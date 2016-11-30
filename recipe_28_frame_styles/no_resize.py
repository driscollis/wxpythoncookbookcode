import wx


class NoResizeFrame(wx.Frame):
    """
    This frame cannot be resized. It can only be minimized
    and closed
    """

    def __init__(self):
        """Constructor"""
        no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                                                wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self, None, title="No Resize", style=no_resize)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = NoResizeFrame()
    app.MainLoop()
