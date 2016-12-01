import random
import wx
from wx.lib.buttons import GenButton


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sizer = wx.WrapSizer()
        for letter in text:
            btn = GenButton(self, label=letter)
            r = random.randint(128, 255)
            g = random.randint(128, 255)
            b = random.randint(128, 255)
            btn.SetBackgroundColour(wx.Colour(r,g,b))
            btn.Refresh()
            sizer.Add(btn, 0, wx.ALL, 5)

        self.SetSizer(sizer)


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="WrapSizers", size=(400,500))
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()