import wx


class NoCaptionFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        no_caption = (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER 
                      | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        wx.Frame.__init__(self, None, title="No Caption", style=no_caption)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = NoCaptionFrame()
    app.MainLoop()