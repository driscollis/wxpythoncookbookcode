import wx
import dark_mode


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.defaultColor = self.GetBackgroundColour()

        rows = [("Ford", "Taurus", "1996", "Blue"),
                ("Nissan", "370Z", "2010", "Green"),
                ("Porche", "911", "2009", "Red")
                ]
        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.list_ctrl.InsertColumn(0, "Make")
        self.list_ctrl.InsertColumn(1, "Model")
        self.list_ctrl.InsertColumn(2, "Year")
        self.list_ctrl.InsertColumn(3, "Color")

        index = 0
        for row in rows:
            self.list_ctrl.InsertStringItem(index, row[0])
            self.list_ctrl.SetStringItem(index, 1, row[1])
            self.list_ctrl.SetStringItem(index, 2, row[2])
            self.list_ctrl.SetStringItem(index, 3, row[3])
            if index % 2:
                self.list_ctrl.SetItemBackgroundColour(index, "white")
            else:
                self.list_ctrl.SetItemBackgroundColour(index, "yellow")
            index += 1

        btn = wx.ToggleButton(self, label="Toggle Dark")
        btn.Bind(wx.EVT_TOGGLEBUTTON, self.onToggleDark)
        normalBtn = wx.Button(self, label="Test")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        sizer.Add(normalBtn, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def onToggleDark(self, event):
        """"""
        dark_mode.darkMode(self, self.defaultColor)


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None,
                          title="MvP ListCtrl Dark Mode Demo",
                          size=(400, 400))
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()