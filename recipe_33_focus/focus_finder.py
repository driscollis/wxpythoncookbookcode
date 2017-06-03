import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Focus Finder")

        panel = wx.Panel(self, wx.ID_ANY)
        panel.Bind(wx.EVT_SET_FOCUS, self.onFocus)
        txt = wx.StaticText(
            panel, label="This label cannot receive focus")

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer)
        self.timer.Start(1000)

    def onFocus(self, event):
        print("panel received focus!")

    def onTimer(self, evt):
        print('Focused window:', wx.Window.FindFocus())


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()