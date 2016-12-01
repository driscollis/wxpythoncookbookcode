# notebookXrcDemo.py
import wx
from wx import xrc

class MyApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource("notebook.xrc")

        self.frame = self.res.LoadFrame(None, 'DemoFrame')

        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()