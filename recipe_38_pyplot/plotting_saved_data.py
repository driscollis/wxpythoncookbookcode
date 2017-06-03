import wx
from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics

class MyGraph(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          'Plotting File Data')

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.canvas = PlotCanvas(panel)
        self.canvas.Draw(self.createPlotGraphics())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        panel.SetSizer(sizer)

    def readFile(self):
        """
        Reads the hard-coded file
        """
        # normally you would want to pass a file path in, NOT hard code it!
        with open("data.txt") as fobj:
            # skip the first two lines of text in the file
            data = fobj.readlines()[2:-1]

        temps = []
        for line in data:
            parts = line.split(",")
            date = parts[0].split("-")
            day = date[2]
            points = [(day, parts[3]), (day, parts[1])]
            temps.append(points)
        return temps

    def createPlotGraphics(self):
        """
        Create the plot's graphics
        """
        temps = self.readFile()
        lines = []
        for temp in temps:
            tempInt = int(temp[1][1])
            if tempInt < 60:
                color = "blue"
            elif tempInt >=60 and tempInt <= 75:
                color = "orange"
            else:
                color = "red"
            lines.append(PolyLine(temp, colour=color, width=10))

        return PlotGraphics(lines, "Bar Graph of Temperatures",
                            "Days", "Temperatures")

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyGraph()
    frame.Show()
    app.MainLoop()