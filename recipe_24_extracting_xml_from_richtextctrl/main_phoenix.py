import wx
import wx.richtext

from io import BytesIO


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Richtext Test')

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.rt = wx.richtext.RichTextCtrl(self)
        self.rt.SetMinSize((300,200))

        save_button = wx.Button(self, label="Save")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.rt, 1, wx.EXPAND|wx.ALL, 6)
        sizer.Add(save_button, 0, wx.EXPAND|wx.ALL, 6)

        self.SetSizer(sizer)
        self.Show()

    def on_save(self, event):
        out = BytesIO()
        handler = wx.richtext.RichTextXMLHandler()
        rt_buffer = self.rt.GetBuffer()
        handler.SaveFile(rt_buffer, out)
        self.xml_content = out.getvalue()
        print(self.xml_content)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()