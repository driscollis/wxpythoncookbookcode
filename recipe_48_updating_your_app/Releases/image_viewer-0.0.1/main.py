import os
import wx
from wx.lib.softwareupdate import SoftwareUpdate


class PhotoCtrl(wx.App, SoftwareUpdate):
    """
    The Photo Viewer App Class
    """

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

        BASEURL = "http://127.0.0.1:8000"
        self.InitUpdates(BASEURL,
                         BASEURL + "/" + 'ChangeLog.txt')
        self.SetAppDisplayName('Image Viewer')
        self.CheckForUpdate()

        self.frame = wx.Frame(None, title='Photo Control')

        self.panel = wx.Panel(self.frame)

        self.PhotoMaxSize = 500

        self.createWidgets()
        self.frame.Show()

    def createWidgets(self):
        instructions = 'Browse for an image'
        img = wx.Image(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                         wx.Bitmap(img))

        instructLbl = wx.StaticText(self.panel, label=instructions)
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)

        self.panel.Layout()

    def onBrowse(self, event):
        """
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

    def onView(self):
        """
        Attempts to load the image and display it
        """
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()
        self.mainSizer.Fit(self.frame)


if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()