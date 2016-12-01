import wx


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Center the Button")
        panel = wx.Panel(self)

        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        btn = wx.Button(panel, label="Centered")
        h_sizer.Add(btn, 0, wx.CENTER)

        main_sizer.Add((0,0), 1, wx.EXPAND)
        main_sizer.Add(h_sizer, 0, wx.CENTER)
        main_sizer.Add((0,0), 1, wx.EXPAND)

        panel.SetSizer(main_sizer)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()