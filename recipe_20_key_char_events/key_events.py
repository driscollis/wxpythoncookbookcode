import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Key Press Tutorial")

        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.Button(panel, label="OK")

        btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print(keycode)
        if keycode == wx.WXK_SPACE:
            print("you pressed the spacebar!")
        event.Skip()


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyForm()
    frame.Show()
    app.MainLoop()