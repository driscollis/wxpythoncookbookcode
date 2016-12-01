# twoBtns_xrc_subclass_v2.py

from twoBtns_xrc_v2 import xrcMainFrame
import wx


class XrcFrameSubClass(xrcMainFrame):
    """"""

    def __init__(self):
        """Constructor"""
        xrcMainFrame.__init__(self, parent=None)
        self.Show()

    def OnButton_okBtn(self, event):
        """"""
        print "You pressed the OK button!"

    def OnButton_cancelBtn(self, event):
        """"""
        print "You pressed the Cancel button!"


if __name__ == "__main__":
    app = wx.App(False)
    frame = XrcFrameSubClass()
    app.MainLoop()
