import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


class SingleInstanceFrame(wx.Frame):
    """"""

    instance = None
    init = 0

    def __new__(self, *args, **kwargs):
        """"""
        if self.instance is None:
            self.instance = wx.Frame.__new__(self)
        elif not self.instance:
            self.instance = wx.Frame.__new__(self)

        return self.instance

    def __init__(self):
        """Constructor"""
        print(id(self))
        if self.init:
            return
        self.init = 1

        wx.Frame.__init__(self, None, title="Single Instance Frame")
        panel = MyPanel(self)
        self.Show()


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main Frame")
        panel = MyPanel(self)
        btn = wx.Button(panel, label="Open Frame")
        btn.Bind(wx.EVT_BUTTON, self.open_frame)
        self.Show()

    def open_frame(self, event):
        frame = SingleInstanceFrame()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()