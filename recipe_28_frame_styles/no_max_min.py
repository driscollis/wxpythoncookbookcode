import wx


class NoMaxMinFrame(wx.Frame):
    """
    This frame does not have maximize or minimize buttons
    """

    def __init__(self):
        """Constructor"""
        no_caption = (wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION
                      | wx.CLOSE_BOX | wx.CLIP_CHILDREN
                      | wx.FRAME_NO_TASKBAR)
        wx.Frame.__init__(self, None, title="No Max/Min", style=no_caption)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = NoMaxMinFrame()
    app.MainLoop()