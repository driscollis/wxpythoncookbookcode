import random
import wx


class TabPanel(wx.Panel):
    """
    The panel class to derive the tabs of the Notebook from
    """

    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

        btn = wx.Button(self, label="Press Me")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)


class DemoNotebook(wx.Notebook):
    """
    Our Notebook class
    """

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)

        tabOne = TabPanel(self)
        self.AddPage(tabOne, "Tab 1")

        tabTwo = TabPanel(self)
        self.AddPage(tabTwo, "Tab 2")


class DemoPanel(wx.Panel):
    """
    The main panel used by the frame
    """

    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        notebook = DemoNotebook(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)


class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Notebook Tutorial",
                          size=(600,400)
                          )
        panel = DemoPanel(self)

        self.Layout()

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = DemoFrame()
    app.MainLoop()