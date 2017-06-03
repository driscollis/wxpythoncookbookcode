# twoBtns_xrc_subclass.py

import twoBtns_xrc
import wx


class XrcFrameSubClass(twoBtns_xrc.xrcMainFrame):
    """"""

    def __init__(self):
        """Constructor"""
        twoBtns_xrc.xrcMainFrame.__init__(self, parent=None)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = XrcFrameSubClass()
    app.MainLoop()