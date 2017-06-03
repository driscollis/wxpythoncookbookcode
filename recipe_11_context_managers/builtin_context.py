import time
import wx


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.frame = parent

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        dlg_btn = wx.Button(self, label='Open ColorDialog')
        dlg_btn.Bind(wx.EVT_BUTTON, self.onOpenColorDialog)
        main_sizer.Add(dlg_btn, 0, wx.ALL|wx.CENTER)

        busy_btn = wx.Button(self, label='Open BusyInfo')
        busy_btn.Bind(wx.EVT_BUTTON, self.onOpenBusyInfo)
        main_sizer.Add(busy_btn,0, wx.ALL|wx.CENTER)

        self.SetSizer(main_sizer)

    def onOpenColorDialog(self, event):
        """
        Creates and opens the wx.ColourDialog
        """
        with wx.ColourDialog(self) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                data = dlg.GetColourData()
                color = str(data.GetColour().Get())
                print 'You selected: %s\n' % color

    def onOpenBusyInfo(self, event):
        """
        Creates and opens an instance of BusyInfo
        """
        msg = 'This app is busy right now!'
        self.frame.Hide()
        with wx.BusyInfo(msg) as busy:
            time.sleep(5)
        self.frame.Show()


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title='Context Managers')
        panel = MyPanel(self)

        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()