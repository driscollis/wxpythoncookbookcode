import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Focus Tutorial 1")


        panel = wx.Panel(self)
        panel.Bind(wx.EVT_SET_FOCUS, self.onFocus)

    def onFocus(self, event):
        print("panel received focus!")

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()