import wx


class MainPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        for num in range(4):
            label = "Button %s" % num
            btn = wx.Button(self, label=label)
            sizer.Add(btn, 0, wx.ALL, 5)
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("big_cat.jpg")
        dc.DrawBitmap(bmp, 0, 0)


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, size=(600,450))
        panel = MainPanel(self)
        self.Center()


class Main(wx.App):
    """"""

    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()


if __name__ == "__main__":
    app = Main()
    app.MainLoop()