import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent)


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """"""
        wx.Frame.__init__(self, None, title="Test Maximize")
        panel = MyPanel(self)
        self.Show()
        self.Maximize(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()