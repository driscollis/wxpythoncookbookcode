import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        btn = wx.Button(self, label="Press Me")
        btn.Bind(wx.EVT_BUTTON, self.HandlerOne)
        btn.Bind(wx.EVT_BUTTON, self.HandlerTwo)

    def HandlerOne(self, event):
        """"""
        print("handler one fired!")
        event.Skip()

    def HandlerTwo(self, event):
        """"""
        print("handler two fired!")
        event.Skip()


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test")
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()