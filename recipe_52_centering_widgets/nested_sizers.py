import wx

class MainFrame(wx.Frame):
    """"""


    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Center the Button")
        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        btn = wx.Button(panel, label="Centered")
        main_sizer.AddStretchSpacer()
        main_sizer.Add(btn, 0, wx.CENTER)
        main_sizer.AddStretchSpacer()

        panel.SetSizer(main_sizer)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()