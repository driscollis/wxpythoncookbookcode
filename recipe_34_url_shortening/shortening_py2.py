import re
import urllib
import urllib2
import wx

bitlyFlag = True
tinyURLFlag = True

try:
    import bitly
except ImportError:
    bitlyFlag = False

try:
    import tinyurl
except ImportError:
    tinyURLFlag = False


class MainPanel(wx.Panel):
    """
    """

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.frame = parent

        # create the widgets
        self.createLayout()

    def createLayout(self):
        """
        Create widgets and lay them out
        """
        choices = ["is.gd"]
        if bitlyFlag:
            choices.append("bit.ly")
        if tinyURLFlag:
            choices.append("tinyURL")
        choices.sort()

        # create the widgets
        self.URLCbo = wx.ComboBox(self, wx.ID_ANY, "is.gd",
                                  choices=choices,
                                  size=wx.DefaultSize,
                                  style=wx.CB_DROPDOWN)
        self.inputURLTxt = wx.TextCtrl(self, value="Paste long URL here")
        self.inputURLTxt.Bind(wx.EVT_SET_FOCUS, self.onFocus)
        self.outputURLTxt = wx.TextCtrl(self, style=wx.TE_READONLY)

        shortenBtn = wx.Button(self, label="Shorten URL")
        shortenBtn.Bind(wx.EVT_BUTTON, self.onShorten)
        copyBtn = wx.Button(self, label="Copy to Clipboard")
        copyBtn.Bind(wx.EVT_BUTTON, self.onCopy)

        # create the sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        # layout the widgets
        mainSizer.Add(self.URLCbo, 0, wx.ALL, 5)
        mainSizer.Add(self.inputURLTxt, 0,
                      wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.outputURLTxt, 0,
                      wx.ALL|wx.EXPAND, 5)
        btnSizer.Add(shortenBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(copyBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(mainSizer)

    def onCopy(self, event):
        """
        Copies data to the clipboard or displays an error
        dialog if the clipboard is inaccessible.
        """
        text = self.outputURLTxt.GetValue()
        self.do = wx.TextDataObject()
        self.do.SetText(text)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.do)
            wx.TheClipboard.Close()
            status = "Copied %s to clipboard" % text
            self.frame.statusbar.SetStatusText(status)
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

    def onFocus(self, event):
        """
        When control is given the focus, it is cleared
        """
        self.inputURLTxt.SetValue("")

    def onShorten(self, event):
        """
        Shortens a URL using the service specified.
        Then sets the text control to the new URL.
        """
        text = self.inputURLTxt.GetValue()
        textLength = len(text)

        if re.match("^https?://[^ ]+", text) and textLength > 20:
            pass
        else:
            wx.MessageBox("URL is already tiny!", "Error")
            return

        URL = self.URLCbo.GetValue()
        if URL == "is.gd":
            self.shortenWithIsGd(text)
        elif URL == "bit.ly":
            self.shortenWithBitly(text)
        elif URL == "tinyurl":
            self.shortenWithTinyURL(text)

    def shortenWithBitly(self, text):
        """
        Shortens the URL in the text control using bit.ly

        Requires a bit.ly account and API key
        """
        bitly.API_LOGIN = "username"
        bitly.API_KEY = "api_key"
        URL = bitly.shorten(text)
        self.outputURLTxt.SetValue(URL)

    def shortenWithIsGd(self, text):
        """
        Shortens the URL with is.gd using URLlib and URLlib2
        """

        apiURL = "http://is.gd/api.php?" + urllib.urlencode(dict(longURL=text))
        shortURL = urllib2.urlopen(apiURL).read()
        self.outputURLTxt.SetValue(shortURL)

    def shortenWithTinyURL(self, text):
        """
        Shortens the URL with tinyURL
        """
        print "in tinyurl"
        URL = tinyurl.create_one(text)
        self.outputURLTxt.SetValue(URL)


class URLFrame(wx.Frame):
    """
    wx.Frame class
    """

    def __init__(self):
        """Constructor"""
        title = "URL Shortener"
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          title=title, size=(650, 220))
        panel = MainPanel(self)
        self.statusbar = self.CreateStatusBar()
        self.SetMinSize((650, 220))


if __name__ == "__main__":
    app = wx.App(False)
    frame = URLFrame()
    frame.Show()
    app.MainLoop()