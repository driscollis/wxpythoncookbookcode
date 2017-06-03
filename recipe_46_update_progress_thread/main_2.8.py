# This code works with wxPython 2.8.12 and Python 2

import time
import wx

from threading import Thread
from wx.lib.pubsub import Publisher


class TestThread(Thread):
    """Test Worker Thread Class."""

    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()    # start the thread

    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(20):
            time.sleep(1)
            wx.CallAfter(Publisher().sendMessage, "update", "")


class MyProgressDialog(wx.Dialog):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Progress")
        self.count = 0

        self.progress = wx.Gauge(self, range=20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.progress, 0, wx.EXPAND)
        self.SetSizer(sizer)

        # create a pubsub listener
        Publisher().subscribe(self.updateProgress, "update")

    def updateProgress(self, msg):
        """
        Update the progress bar
        """
        self.count += 1

        if self.count >= 20:
            self.Destroy()

        self.progress.SetValue(self.count)


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Progress Bar Tutorial")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.btn = btn = wx.Button(panel, label="Start Thread")
        btn.Bind(wx.EVT_BUTTON, self.onButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    def onButton(self, event):
        """
        Runs the thread
        """
        btn = event.GetEventObject()
        btn.Disable()

        TestThread()
        dlg = MyProgressDialog()
        dlg.ShowModal()

        btn.Enable()

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()