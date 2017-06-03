import custTray
import wx


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Minimize to Tray")
        panel = wx.Panel(self)
        self.tbIcon = custTray.CustomTaskBarIcon(self)

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.Show()

    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

    def onMinimize(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        if self.IsIconized():
            self.Hide()


def main():
    """"""
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

if __name__ == "__main__":
    main()