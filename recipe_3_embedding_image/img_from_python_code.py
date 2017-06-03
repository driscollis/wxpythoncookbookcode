import wx
import my_icon

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Python Image Title')

        self.panel = wx.Panel(self, wx.ID_ANY)

        ico = my_icon.PyEmbeddedImage(my_icon.py)
        self.SetIcon(ico.data.GetIcon())


# Run the program
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()