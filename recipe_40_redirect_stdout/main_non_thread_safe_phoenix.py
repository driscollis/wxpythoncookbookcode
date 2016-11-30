# wxPython Phoenix

import sys
import wx

class MyCustomTextCtrl(wx.TextCtrl):

    def __init__(self, *args, **kwargs):
        """
        Initial the text control
        """
        wx.TextCtrl.__init__(self, *args, **kwargs)

    def write(self, text):
        self.WriteText(text)


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None,
                          title="wxPython Redirect Tutorial")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL
        log = MyCustomTextCtrl(panel, wx.ID_ANY, size=(300,100),
                               style=style)
        btn = wx.Button(panel, wx.ID_ANY, 'Push me!')
        self.Bind(wx.EVT_BUTTON, self.onButton, btn)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        # redirect text here
        sys.stdout = log

    def onButton(self, event):
        print("You pressed the button!")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()