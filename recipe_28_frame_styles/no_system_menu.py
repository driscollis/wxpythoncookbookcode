import wx


class NoSystemMenuFrame(wx.Frame):
    """
    There is no system menu, which means the title bar is there, but
    no buttons and no menu when clicking the top left hand corner
    of the frame
    """

    def __init__(self):
        """Constructor"""
        no_sys_menu = wx.CAPTION
        wx.Frame.__init__(self, None, title="No System Menu",
                          style=no_sys_menu)
        panel = wx.Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = NoSystemMenuFrame()
    app.MainLoop()