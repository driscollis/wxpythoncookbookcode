import time
import wx

from threading import Thread

# Define notification event for thread completion
EVT_RESULT_ID = wx.NewId()

def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data


class TestThread(Thread):
    """Test Worker Thread Class."""

    def __init__(self, wxObject):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.wxObject = wxObject
        self.start()    # start the thread

    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(6):
            time.sleep(10)
            amtOfTime = (i + 1) * 10
            wx.PostEvent(self.wxObject, ResultEvent(amtOfTime))
        time.sleep(5)
        wx.PostEvent(self.wxObject, ResultEvent("Thread finished!"))


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.displayLbl = wx.StaticText(panel, label="Amount of time since thread started goes here")
        self.btn = btn = wx.Button(panel, label="Start Thread")

        btn.Bind(wx.EVT_BUTTON, self.onButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.displayLbl, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        # Set up event handler for any worker thread results
        EVT_RESULT(self, self.updateDisplay)

    def onButton(self, event):
        """
        Runs the thread
        """
        TestThread(self)
        self.displayLbl.SetLabel("Thread started!")
        btn = event.GetEventObject()
        btn.Disable()

    def updateDisplay(self, msg):
        """
        Receives data from thread and updates the display
        """
        t = msg.data
        if isinstance(t, int):
            self.displayLbl.SetLabel("Time since thread started: %s seconds" % t)
        else:
            self.displayLbl.SetLabel("%s" % t)
            self.btn.Enable()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()