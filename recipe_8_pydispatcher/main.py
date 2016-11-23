import wx
from pydispatch import dispatcher


class OtherFrame(wx.Frame):
    """"""


    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Secondary Frame")
        panel = wx.Panel(self)

        msg = "Enter a Message to send to the main frame"
        instructions = wx.StaticText(panel, label=msg)
        self.msgTxt = wx.TextCtrl(panel, value="")
        closeBtn = wx.Button(panel, label="Send and Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.onSendAndClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL|wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msgTxt, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        panel.SetSizer(sizer)


    def onSendAndClose(self, event):
        """
        Send a message and close frame
        """
        msg = self.msgTxt.GetValue()
        dispatcher.send("panelListener", message=msg)
        dispatcher.send("panelListener", message="test2", arg2="2nd argument!")
        self.Close()


class MyPanel(wx.Panel):
    """"""


    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        dispatcher.connect(self.myListener, signal="panelListener",
                           sender=dispatcher.Any)

        btn = wx.Button(self, label="Open Frame")
        btn.Bind(wx.EVT_BUTTON, self.onOpenFrame)


    def myListener(self, message, arg2=None):
        """
        Listener function
        """
        print("Received the following message: " + message)
        if arg2:
            print("Received another arguments: " + str(arg2))


    def onOpenFrame(self, event):
        """
        Opens secondary frame
        """
        frame = OtherFrame()
        frame.Show()


class MyFrame(wx.Frame):
    """"""


    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="PyDispatcher Tutorial")
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()