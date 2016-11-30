import wx


class PanelOne(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        msg = "This panel will self-destruct in 10 seconds"
        self.countdown = wx.StaticText(self, label=msg)


class PanelTwo(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        txt = wx.StaticText(self, label="Panel Two")


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Panel Smacker")
        self.panelOne = PanelOne(self)
        self.time2die = 10

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1000)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelOne, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def update(self, event):
        """"""
        if self.time2die < 0:
            self.panelOne.Destroy()
            self.panelTwo = PanelTwo(self)
            self.sizer.Add(self.panelTwo, 1, wx.EXPAND)
            self.Layout()
            self.timer.Stop()
        else:
            msg = "This panel will self-destruct in %s seconds" % self.time2die
            self.panelOne.countdown.SetLabel(msg)
        self.time2die -= 1


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()