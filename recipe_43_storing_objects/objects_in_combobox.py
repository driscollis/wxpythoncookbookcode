import wx


class Car:
    """"""

    def __init__(self, id, model, make, year):
        """Constructor"""
        self.id = id
        self.model = model
        self.make = make
        self.year = year


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Tutorial")

        panel = wx.Panel(self, wx.ID_ANY)

        cars = [Car(0, "Ford", "F-150", "2008"),
                Car(1, "Chevrolet", "Camaro", "2010"),
                Car(2, "Nissan", "370Z", "2005")]

        sampleList = []
        self.cb = wx.ComboBox(panel,
                              size=wx.DefaultSize,
                              choices=sampleList)
        self.widgetMaker(self.cb, cars)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cb, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

    def widgetMaker(self, widget, objects):
        """"""
        for obj in objects:
            widget.Append(obj.make, obj)
        widget.Bind(wx.EVT_COMBOBOX, self.onSelect)

    def onSelect(self, event):
        """"""
        print("You selected: " + self.cb.GetStringSelection())
        obj = self.cb.GetClientData(self.cb.GetSelection())
        text = """
        The object's attributes are:
        %s  %s    %s  %s

        """ % (obj.id, obj.make, obj.model, obj.year)
        print(text)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()