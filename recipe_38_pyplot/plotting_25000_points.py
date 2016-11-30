import numpy as _Numeric
import wx
from wx.lib.plot import PlotCanvas, PlotGraphics, PolyLine, PolyMarker


def drawLinePlot():
    # 25,000 point line
    data1 = _Numeric.arange(5e5,1e6,10)
    data1.shape = (25000, 2)
    line1 = PolyLine(data1, legend='Wide Line', colour='green', width=5)

    # A few more points...
    markers2 = PolyMarker(data1, legend='Square', colour='blue',
                          marker='square')
    return PlotGraphics([line1, markers2], "25,000 Points", "Value X", "")


class MyGraph(wx.Frame):


    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          'It Looks Like a Line Graph!')

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)

        # create the widgets
        self.canvas = PlotCanvas(panel)
        self.canvas.Draw(drawLinePlot())
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
        toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Show Legend")
        toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)

        # layout the widgets
        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 5)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 5)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)


    def onToggleGrid(self, event):
        """"""
        self.canvas.SetEnableGrid(event.IsChecked())


    def onToggleLegend(self, event):
        """"""
        self.canvas.SetEnableLegend(event.IsChecked())

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyGraph()
    frame.Show()
    app.MainLoop()