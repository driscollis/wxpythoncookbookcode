import re
import urllib
import urllib2
import wx

class ArsShortener(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          'wxArsShortener', size=(300,70))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        self.txt = wx.TextCtrl(panel, wx.ID_ANY, "", size=(300, -1))
        self.txt.Bind(wx.EVT_TEXT, self.onTextChange)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txt, 0, wx.EXPAND, 5)
        panel.SetSizer(sizer)

    def onTextChange(self, event):
        """"""
        text = self.txt.GetValue()
        textLength = len(text)
        if re.match("^https?://[^ ]+", text) and textLength > 20:
            apiURL = "http://is.gd/api.php?" + urllib.urlencode(dict(longURL=text))
            shortened_URL = urllib2.urlopen(apiURL).read()
            self.txt.SetValue(shortened_URL)

if __name__ == '__main__':
    app = wx.App(False)
    frame = ArsShortener()
    frame.Show()
    app.MainLoop()