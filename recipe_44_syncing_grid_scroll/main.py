import wx
import wx.grid as gridlib


class ScrollSync(object):
    def __init__(self, panel1, panel2):
        self.panel1 = panel1
        self.panel2 = panel2
        self.panel1.grid.Bind(wx.EVT_SCROLLWIN, self.onScrollWin1)
        self.panel2.grid.Bind(wx.EVT_SCROLLWIN, self.onScrollWin2)

    def onScrollWin1(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.panel2.grid.Scroll(event.Position, -1)
        else:
            self.panel2.grid.Scroll(-1, event.Position)
        event.Skip()

    def onScrollWin2(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.panel1.grid.Scroll(event.Position, -1)
        else:
            self.panel1.grid.Scroll(-1, event.Position)
        event.Skip()


class GridPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.grid = gridlib.Grid(self, style=wx.BORDER_SUNKEN)
        self.grid.CreateGrid(25,8)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.SetSizer(sizer)


class MainPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


        split = wx.SplitterWindow(self)

        panelOne = GridPanel(split)
        panelTwo = GridPanel(split)
        ScrollSync(panelOne, panelTwo)

        split.SplitVertically(panelOne, panelTwo)
        split.SetSashGravity(0.5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(split, 1, wx.EXPAND)
        self.SetSizer(sizer)


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Sync Grids",
                          size=(800,400))
        panel = MainPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()