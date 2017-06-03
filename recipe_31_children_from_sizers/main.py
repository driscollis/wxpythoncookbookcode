import wx


class MyApp(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        title = 'Get Children from Sizer'
        wx.Frame.__init__(self, None, title=title)
        panel = wx.Panel(self)

        lbl = wx.StaticText(panel, label="I'm a label!")
        txt = wx.TextCtrl(panel, value="blah blah")
        btn = wx.Button(panel, label="Clear")
        btn.Bind(wx.EVT_BUTTON, self.onClear)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(lbl, 0, wx.ALL, 5)
        self.sizer.Add(txt, 0, wx.ALL, 5)
        self.sizer.Add(btn, 0, wx.ALL, 5)

        panel.SetSizer(self.sizer)

    def onClear(self, event):
        """
        Button event handler for clearing TextCtrl widgets
        """
        children = self.sizer.GetChildren()

        for child in children:
            widget = child.GetWindow()
            print widget
            if isinstance(widget, wx.TextCtrl):
                widget.Clear()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyApp()
    frame.Show()
    app.MainLoop()