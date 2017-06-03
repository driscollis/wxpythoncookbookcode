import wx 


class DefaultFrame(wx.Frame):
    """
    The default frame
    """

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Default Frame",
                          style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = DefaultFrame()
    app.MainLoop()