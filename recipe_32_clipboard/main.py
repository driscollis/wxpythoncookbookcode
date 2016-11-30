import wx


class ClipboardPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        lbl = wx.StaticText(self, label="Enter text to copy to clipboard:")
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        copyBtn = wx.Button(self, label="Copy")
        copyBtn.Bind(wx.EVT_BUTTON, self.onCopy)
        copyFlushBtn = wx.Button(self, label="Copy and Flush")
        copyFlushBtn.Bind(wx.EVT_BUTTON, self.onCopyAndFlush)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.text, 1, wx.EXPAND)
        sizer.Add(copyBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(copyFlushBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)

    def onCopy(self, event):
        """"""
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(self.text.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

    def onCopyAndFlush(self, event):
        """
        Copy to the clipboard and close the application
        """
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(self.text.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Flush()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

        self.GetParent().Close()


class ClipboardFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Clipboard Tutorial")
        panel = ClipboardPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = ClipboardFrame()
    app.MainLoop()