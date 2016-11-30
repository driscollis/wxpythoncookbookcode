import wx
import time

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Timer Tutorial 1",
                          size=(500,500))

        panel = wx.Panel(self, wx.ID_ANY)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        self.toggleBtn = wx.Button(panel, wx.ID_ANY, "Start")
        self.toggleBtn.Bind(wx.EVT_BUTTON, self.onToggle)

    def onToggle(self, event):
        if self.timer.IsRunning():
            self.timer.Stop()
            self.toggleBtn.SetLabel("Start")
            print("timer stopped!")
        else:
            print("starting timer...")
            self.timer.Start(1000)
            self.toggleBtn.SetLabel("Stop")

    def update(self, event):
        print("\nupdated: ", time.ctime())


# Run the program
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyForm().Show()
    app.MainLoop()