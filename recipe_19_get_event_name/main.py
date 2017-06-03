import wx
import wx.grid


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Tutorial")

        self.eventDict = {}
        evt_names = [x for x in dir(wx) if x.startswith("EVT_")]
        for name in evt_names:
            evt = getattr(wx, name)
            if isinstance(evt, wx.PyEventBinder):
                self.eventDict[evt.typeId] = name

        grid_evt_names = [x for x in dir(wx.grid) if x.startswith("EVT_")]
        for name in grid_evt_names:
            evt = getattr(wx.grid, name)
            if isinstance(evt, wx.PyEventBinder):
                self.eventDict[evt.typeId] = name

        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.Button(panel, wx.ID_ANY, "Get POS")

        btn.Bind(wx.EVT_BUTTON, self.onEvent)
        panel.Bind(wx.EVT_LEFT_DCLICK, self.onEvent)
        panel.Bind(wx.EVT_RIGHT_DOWN, self.onEvent)

    def onEvent(self, event):
        """
        Print out what event was fired
        """
        evt_id = event.GetEventType()
        print(self.eventDict[evt_id])


if __name__ == "__main__":
    app = wx.App(redirect=True)
    frame = MyForm().Show()
    app.MainLoop()