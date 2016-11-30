import wx
import time

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Timer Tutorial 2")

        panel = wx.Panel(self, wx.ID_ANY)

        self.timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer2 = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.update, self.timer2)

        self.toggleBtn = wx.Button(panel, wx.ID_ANY, "Start Timer 1")
        self.toggleBtn.Bind(wx.EVT_BUTTON, self.onStartTimer)
        self.toggleBtn2 = wx.Button(panel, wx.ID_ANY, "Start Timer 2")
        self.toggleBtn2.Bind(wx.EVT_BUTTON, self.onStartTimer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.toggleBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.toggleBtn2, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        # Each value in the following dict is formatted as follows:
        # (timerNum, timerObj, secs between timer events)
        self.objDict = {self.toggleBtn: (1, self.timer, 1000),
                        self.toggleBtn2: (2, self.timer2, 3000)}

    def onStartTimer(self, event):
        btn = event.GetEventObject()
        timerNum, timer, secs = self.objDict[btn]
        if timer.IsRunning():
            timer.Stop()
            btn.SetLabel("Start Timer %s" % timerNum)
            print("timer %s stopped!" % timerNum)
        else:
            print("starting timer %s..." % timerNum)
            timer.Start(secs)
            btn.SetLabel("Stop Timer %s" % timerNum)

    def update(self, event):
        timerId = event.GetId()
        if timerId == self.timer.GetId():
            print("\ntimer 1 updated: ", time.ctime())
        else:
            print ("\ntimer 2 updated: ", time.ctime())


# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()