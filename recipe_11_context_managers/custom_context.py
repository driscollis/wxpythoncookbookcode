import os
import wx


class ContextFileDialog(wx.FileDialog):
    """"""

    def __enter__(self):
        """"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Destroy()


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label='Open File')
        btn.Bind(wx.EVT_BUTTON, self.onOpenFile)

    def onOpenFile(self, event):
        """"""
        wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
        kwargs = {'message':"Choose a file",
                  'defaultDir':os.path.dirname(os.path.abspath( __file__ )),
                  'defaultFile':"",
                  'wildcard':wildcard,
                  'style':wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
                  }
        with ContextFileDialog(self, **kwargs) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                print "You chose the following file(s):"
                for path in paths:
                    print path


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title='wxPython Contexts')
        panel = MyPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()