import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Losing Focus")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        txt = wx.TextCtrl(panel, value="")
        txt.Bind(wx.EVT_SET_FOCUS, self.onFocus)
        txt.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
        btn = wx.Button(panel, wx.ID_ANY, "Test")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txt, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

    def onFocus(self, event):
        print("widget received focus!")

    def onKillFocus(self, event):
        print("widget lost focus!")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()