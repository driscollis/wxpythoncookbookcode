import logging
import wx


class ExceptionLogging(object):

    def __init__(self, fn):
        self.fn = fn

        # create logging instance
        self.log = logging.getLogger("wxErrors")
        self.log.setLevel(logging.INFO)

        # create a logging file handler / formatter
        log_fh = logging.FileHandler("error.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
        log_fh.setFormatter(formatter)
        self.log.addHandler(log_fh)

    def __call__(self, evt):
        try:
            self.fn(self, evt)
        except Exception as e:
            self.log.exception("Exception")


class Panel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label="Raise Exception")
        btn.Bind(wx.EVT_BUTTON, self.onExcept)

    @ExceptionLogging
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
        panel = Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    app.MainLoop()