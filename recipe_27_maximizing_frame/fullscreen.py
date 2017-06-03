import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.Bind(wx.EVT_KEY_DOWN, self.onKey)

    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test FullScreen")
        panel = MyPanel(self)
        self.ShowFullScreen(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()