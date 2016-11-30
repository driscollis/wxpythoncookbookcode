import wx


class DefaultFrame(wx.Frame):
    """
    The default frame
    """

    def __init__(self):
        """Constructor"""
        default = (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
                   | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
                   | wx.CLIP_CHILDREN)
        wx.Frame.__init__(self, None, title="Default Frame", style=default)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = DefaultFrame()
    app.MainLoop()