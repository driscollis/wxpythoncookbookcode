import wx
import os
import time


class MyListCtrl(wx.ListCtrl):

    def __init__(self, parent, id):
        wx.ListCtrl.__init__(self, parent, id,
                             style=wx.LC_REPORT)

        files = os.listdir('.')

        self.InsertColumn(0, 'Name')
        self.InsertColumn(1, 'Ext')
        self.InsertColumn(2, 'Size',
                          wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(3, 'Modified')

        self.SetColumnWidth(0, 220)
        self.SetColumnWidth(1, 70)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 420)

        j = 0
        for i in files:
            (name, ext) = os.path.splitext(i)

            size = os.path.getsize(i)
            sec = os.path.getmtime(i)
            self.InsertStringItem(j, "{}{}".format(name, ext))
            self.SetStringItem(j, 1, ext)
            self.SetStringItem(j, 2, str(size) + ' B')
            self.SetStringItem(
                j, 3, time.strftime('%Y-%m-%d %H:%M',
                                    time.localtime(sec)))

            if os.path.isdir(i):
                self.SetItemImage(j, 1)
            elif 'py' in ext:
                self.SetItemImage(j, 2)
            elif 'jpg' in ext:
                self.SetItemImage(j, 3)
            elif 'pdf' in ext:
                self.SetItemImage(j, 4)
            else:
                self.SetItemImage(j, 0)

            if (j % 2) == 0:
                self.SetItemBackgroundColour(j, 'light blue')
            j = j + 1


class DnDFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='DnD Files')
        panel = wx.Panel(self)

        p1 = MyListCtrl(panel, -1)
        p1.Bind(wx.EVT_LIST_BEGIN_DRAG, self.onDrag)
        sizer = wx.BoxSizer()
        sizer.Add(p1, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.Center()
        self.Show(True)


    def onDrag(self, event):
        """"""
        data = wx.FileDataObject()
        obj = event.GetEventObject()
        id = event.GetIndex()
        filename = obj.GetItem(id).GetText()
        dirname = os.path.dirname(os.path.abspath(
            os.listdir(".")[0]))
        fullpath = os.path.join(dirname, filename)

        data.AddFile(fullpath)

        dropSource = wx.DropSource(obj)
        dropSource.SetData(data)
        result = dropSource.DoDragDrop()
        print(fullpath)

if __name__ == '__main__':
    app = wx.App(False)
    frame = DnDFrame()
    app.MainLoop()