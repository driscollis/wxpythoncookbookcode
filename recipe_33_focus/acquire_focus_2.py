import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Focus Tutorial 1a")

        panel = wx.Panel(self)
        panel.Bind(wx.EVT_SET_FOCUS, self.onFocus)
        txt = wx.TextCtrl(panel, wx.ID_ANY, "")

    def onFocus(self, event):
        print("panel received focus!")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()