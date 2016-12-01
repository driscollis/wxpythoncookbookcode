import wx
from wx import xrc

class MyApp(wx.App):
    def OnInit(self):
        res = xrc.XmlResource("login.xrc")

        frame = res.LoadFrame(None, 'mainFrame')

        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()