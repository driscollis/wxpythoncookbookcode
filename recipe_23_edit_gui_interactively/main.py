# main.py
import testApp
import wx


class ReloaderPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.testFrame = None

        showAppBtn = wx.Button(self, label="Show App")
        showAppBtn.Bind(wx.EVT_BUTTON, self.onShowApp)

        reloadBtn = wx.Button(self, label="Reload")
        reloadBtn.Bind(wx.EVT_BUTTON, self.onReload)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(showAppBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(reloadBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(mainSizer)

    def onReload(self, event):
        """
        Reload the code!
        """
        if self.testFrame:
            self.testFrame.Close()
            try:
                reload(testApp)
            except NameError:
                # reload doesn't exist in Python 3. 
                # Use importlib.reload in Python 3.4+ 
                # or imp.reload in Python 3.0 - 3.3
                import importlib
                importlib.reload(testApp)
            self.showApp()
        else:
            self.testFrame = None

    def onShowApp(self, event):
        """
        Call the showApp() method
        """
        self.showApp()

    def showApp(self):
        """
        Show the application we want to edit dynamically
        """
        self.testFrame = testApp.TestFrame()


class ReloaderFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Reloader")
        panel = ReloaderPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = ReloaderFrame()
    app.MainLoop()