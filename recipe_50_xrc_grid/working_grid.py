import wx
import wx.grid
from wx import xrc


class MyApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource("grid.xrc")

        frame = self.res.LoadFrame(None, 'MyFrame')
        panel = xrc.XRCCTRL(frame, "MyPanel")
        grid = xrc.XRCCTRL(panel, "MyGrid")
        print(type(grid))
        grid.CreateGrid(25, 6)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1, wx.EXPAND|wx.ALL, 5)

        panel.SetSizer(sizer)

        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()