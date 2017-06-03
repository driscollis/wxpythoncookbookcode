# notebookXrcDemo2.py
import wx
from wx import xrc

class MyApp(wx.App):
    def OnInit(self):
        res = xrc.XmlResource("notebook2.xrc")
        frame = res.LoadFrame(None, "DemoFrame")
        panel = xrc.XRCCTRL(frame, "DemoPanel")
        notebook = xrc.XRCCTRL(panel, "DemoNotebook")

        # load another xrc file
        res = xrc.XmlResource("panelOne.xrc")
        tabOne = res.LoadPanel(notebook, "panelOne")
        notebook.AddPage(tabOne, "TabOne")

        # load the last xrc file
        res = xrc.XmlResource("panelTwo.xrc")
        tabTwo = res.LoadPanel(notebook, "panelTwo")
        notebook.AddPage(tabTwo, "tabTwo")

        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()