import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Background Reset Tutorial")

        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.txt = wx.TextCtrl(self.panel)
        self.txt.SetBackgroundColour("Yellow")

        blueBtn = wx.Button(self.panel, 
                            label="Change Background Color")
        blueBtn.Bind(wx.EVT_BUTTON, self.onChangeBackground)
        resetBtn = wx.Button(self.panel, label="Reset")
        resetBtn.Bind(wx.EVT_BUTTON, self.onReset)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(blueBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(resetBtn, 0, wx.ALL|wx.CENTER, 5)

        topSizer.Add(self.txt, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.CENTER)
        self.panel.SetSizer(topSizer)

    def onChangeBackground(self, event):
        """
        Change the background color of the panel
        """
        self.panel.SetBackgroundColour("Blue")
        self.panel.Refresh()

    def onReset(self, event):
        """
        Reset the color of the panel to the default color
        """
        self.panel.SetBackgroundColour(wx.NullColour)
        self.txt.SetBackgroundColour(wx.NullColour)
        self.panel.Refresh()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()