# testApp.py
import wx


class TestPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        btn = wx.Button(self, label='Test')


class TestFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test program")
        panel = TestPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = TestFrame()
    app.MainLoop()