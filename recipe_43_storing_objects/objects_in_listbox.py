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
        wx.Frame.__init__(self, None, title="ListBox Obj Tutorial")

        panel = wx.Panel(self, wx.ID_ANY)

        ford = Car(0, "Ford", "F-150", "2008")
        chevy = Car(1, "Chevrolet", "Camaro", "2010")
        nissan = Car(2, "Nissan", "370Z", "2005")

        sampleList = []
        lb = wx.ListBox(panel,
                        size=wx.DefaultSize,
                        choices=sampleList)
        self.lb = lb
        lb.Append(ford.make, ford)
        lb.Append(chevy.make, chevy)
        lb.Append(nissan.make, nissan)
        lb.Bind(wx.EVT_LISTBOX, self.onSelect)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lb, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

    def onSelect(self, event):
        """"""
        selection = self.lb.GetStringSelection()
        if selection:
            print("You selected: " + selection)
            obj = self.lb.GetClientData(self.lb.GetSelection())
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