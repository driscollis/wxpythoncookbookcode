import wx
from wx import xrc
import wx.lib.platebtn as platebtn


class MyApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource("notebook.xrc")

        frame = self.res.LoadFrame(None, 'DemoFrame')
        panel = xrc.XRCCTRL(frame, "DemoPanel")
        notebook = xrc.XRCCTRL(panel, "DemoNotebook")

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn = platebtn.PlateButton(panel, label="Test",
                                   style=platebtn.PB_STYLE_DEFAULT)
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn)
        panel.SetSizer(sizer)

        frame.Show()
        return True


    def onButton(self, event):
        """"""
        print("You pressed the button!")


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()