import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Custom Image')

        self.panel = wx.Panel(self, wx.ID_ANY)

        ico = wx.Icon('py.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()