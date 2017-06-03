import wx


class NoCloseFrame(wx.Frame):
    """
    This frame has no close box and the close menu is disabled
    """

    def __init__(self):
        """Constructor"""
        no_close = (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
                    | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN)
        wx.Frame.__init__(self, None, title="No Close", style=no_close)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = NoCloseFrame()
    app.MainLoop()