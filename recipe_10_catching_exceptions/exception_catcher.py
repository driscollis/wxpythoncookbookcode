import sys
import traceback
import wx
import wx.lib.agw.genericmessagedialog as GMD


class Panel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label="Raise Exception")
        btn.Bind(wx.EVT_BUTTON, self.onExcept)

    def onExcept(self, event):
        """
        Raise an error
        """
        1/0


class Frame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Exceptions")
        sys.excepthook = MyExceptionHook
        panel = Panel(self)
        self.Show()


class ExceptionDialog(GMD.GenericMessageDialog):
    """
    The dialog to show an exception
    """

    def __init__(self, msg):
        """Constructor"""
        GMD.GenericMessageDialog.__init__(self, None, msg, "Exception!",
                                          wx.OK|wx.ICON_ERROR)


def MyExceptionHook(etype, value, trace):
    """
    Handler for all unhandled exceptions.

    :param `etype`: the exception type (`SyntaxError`, `ZeroDivisionError`, etc...);
    :type `etype`: `Exception`
    :param string `value`: the exception error message;
    :param string `trace`: the traceback header, if any (otherwise, it prints the
     standard Python header: ``Traceback (most recent call last)``.
    """
    frame = wx.GetApp().GetTopWindow()
    tmp = traceback.format_exception(etype, value, trace)
    exception = "".join(tmp)

    dlg = ExceptionDialog(exception)
    dlg.ShowModal()
    dlg.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    app.MainLoop()