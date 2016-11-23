# wxPython Classic Edition

import wx
import wx.wizard


class WizardPage(wx.wizard.PyWizardPage):

    def __init__(self, parent, title):
        wx.wizard.PyWizardPage.__init__(self, parent)
        self.next = None
        self.prev = None
        self.initializeUI(title)

    def initializeUI(self, title):
        # create grid layout manager
        self.sizer = wx.GridBagSizer()
        self.SetSizerAndFit(self.sizer)

    def addWidget(self, widget, pos, span):
        self.sizer.Add(widget, pos, span, wx.EXPAND)

    # getters and setters
    def SetPrev(self, prev):
        self.prev = prev

    def SetNext(self, next):
        self.next = next

    def GetPrev(self):
        return self.prev

    def GetNext(self):
        return self.next


class MyWizard(wx.wizard.Wizard):
    """"""

    def __init__(self):
        """Constructor"""
        wx.wizard.Wizard.__init__(self, None,
                                  title="Disable Next")
        self.SetPageSize((500, 350))

        mypage1 = self.create_page1()

        forward_btn = self.FindWindowById(wx.ID_FORWARD)
        forward_btn.Disable()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)
        self.timer.Start(1)

        self.RunWizard(mypage1)

    def create_page1(self):
        page1 = WizardPage(self, "Page 1")
        d = wx.StaticText(page1, label="test")
        page1.addWidget(d, (2, 1), (1,5))

        self.text1 = wx.TextCtrl(page1)
        page1.addWidget(self.text1, (3,1), (1,5))

        self.text2 = wx.TextCtrl(page1)
        page1.addWidget(self.text2, (4,1), (1,5))

        page2 = WizardPage(self, "Page 2")
        page2.SetName("page2")
        self.text3 = wx.TextCtrl(page2)
        self.Bind(wx.wizard.EVT_WIZARD_PAGE_CHANGED, self.onPageChanged)
        page3 = WizardPage(self, "Page 3")

        # Set links
        page2.SetPrev(page1)
        page1.SetNext(page2)
        page3.SetPrev(page2)
        page2.SetNext(page3)

        return page1

    def onPageChanged(self, event):
        """"""
        page = event.GetPage()

        if page.GetName() == "page2":
            self.text3.SetValue(self.text2.GetValue())

    def onUpdate(self, event):
        """
        Enables the Next button if both text controls have values
        """
        value_one = self.text1.GetValue()
        value_two = self.text2.GetValue()
        if value_one and value_two:
            forward_btn = self.FindWindowById(wx.ID_FORWARD)
            forward_btn.Enable()
            self.timer.Stop()


def main():
    """"""
    wizard = MyWizard()


if __name__ == "__main__":
    app = wx.App(False)
    main()
    app.MainLoop()