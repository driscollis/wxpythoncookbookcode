import wx

class Fader(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Fader Example')
        self.amount = 5
        self.delta = 5
        panel = wx.Panel(self, wx.ID_ANY)

        self.SetTransparent(self.amount)

        # Fader Timer
        self.timer = wx.Timer(self, wx.ID_ANY)
        self.timer.Start(60)
        self.Bind(wx.EVT_TIMER, self.AlphaCycle)

    def AlphaCycle(self, evt):
        """
        Fade the frame in and out
        """
        self.amount += self.delta
        if self.amount >= 255:
            self.delta = -self.delta
            self.amount = 255
        if self.amount <= 0:
            self.amount = 0
            self.delta = 5
        self.SetTransparent(self.amount)

if __name__ == '__main__':
    app = wx.App(False)
    frm = Fader()
    frm.Show()
    app.MainLoop()