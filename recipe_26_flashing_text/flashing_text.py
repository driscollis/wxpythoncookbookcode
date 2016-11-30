import random
import time
import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.label = "I flash a LOT!"
        self.flashingText = wx.StaticText(self, label=self.label)
        self.flashingText.SetFont(self.font)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1000)

    def update(self, event):
        """"""
        colors = ["blue", "green", "red", "yellow"]
        self.flashingText.SetLabel(self.label)
        self.flashingText.SetForegroundColour(random.choice(colors))


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Flashing text!")
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()