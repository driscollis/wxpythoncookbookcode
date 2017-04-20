import wx
import wx.adv
import wx.html
from wx.lib.wordwrap import wordwrap


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='The About Box')

        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        # Create buttons
        aboutBtn = wx.Button(self.panel, wx.ID_ANY, "Open wx.AboutBox")
        self.Bind(wx.EVT_BUTTON, self.onAboutDlg, aboutBtn)
        aboutHtmlBtn = wx.Button(self.panel, wx.ID_ANY, "Open HtmlAboutBox")
        self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutHtmlBtn)

        closeBtn = wx.Button(self.panel, wx.ID_ANY, "Close")
        self.Bind(wx.EVT_BUTTON, self.onClose, closeBtn)

        # Create Sizers
        topSizer = wx.BoxSizer(wx.VERTICAL)

        # Add widgets to sizers
        topSizer.Add(aboutBtn, 0, wx.ALL|wx.CENTER, 5)
        topSizer.Add(aboutHtmlBtn, 0, wx.ALL|wx.CENTER, 5)
        topSizer.Add(closeBtn, 0, wx.ALL|wx.CENTER, 5)

        # Create the menu
        self.createMenu()
        self.statusBar = self.CreateStatusBar()

        self.panel.SetSizer(topSizer)
        self.SetSizeHints(250,300,500,400)
        self.Fit()
        self.Refresh()

    def createMenu(self):
        """ Create the application's menu """
        menubar = wx.MenuBar()

        # Create the file menu
        fileMenu = wx.Menu()

        # Append the close item
        # Append takes an id, the text label, and a string
        # to display in the statusbar when the item is selected
        close_menu_item = fileMenu.Append(wx.NewId(),
                                          "&Close",
                                          "Closes the application")
        # Bind an event to the menu item
        self.Bind(wx.EVT_MENU, self.onClose, close_menu_item)
        # Add the fileMenu to the menu bar
        menubar.Append(fileMenu, "&File")

        # Create the help menu
        helpMenu = wx.Menu()
        about_menu_item = helpMenu.Append(wx.NewId(),
                                          "&About",
                                          "Opens the About Box")
        self.Bind(wx.EVT_MENU, self.onAboutDlg, about_menu_item)
        menubar.Append(helpMenu, "&Help")

        # Add the menu bar to the frame
        self.SetMenuBar(menubar)

    def onAboutHtmlDlg(self, event):
        aboutDlg = AboutDlg(None)
        aboutDlg.Show()

    def onAboutDlg(self, event):
        info = wx.adv.AboutDialogInfo()
        info.Name = "My About Box"
        info.Version = "0.0.1 Beta"
        info.Copyright = "(C) 2008 Python Geeks Everywhere"
        info.Description = wordwrap(
            "This is an example application that shows how to create "
            "different kinds of About Boxes using wxPython!",
            350, wx.ClientDC(self.panel))
        info.WebSite = ("http://www.pythonlibrary.org", "My Home Page")
        info.Developers = ["Mike Driscoll"]
        info.License = wordwrap("Completely and totally open source!", 500,
                                wx.ClientDC(self.panel))
        # Show the wx.AboutBox
        wx.adv.AboutBox(info)

    def onClose(self, event):
        self.Close()


class AboutDlg(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400,400))

        html = wxHTML(self)

        html.SetPage(
            ''

            "<h2>About the About Tutorial</h2>"

            "<p>This about box is for demo purposes only. It was created in June 2006"

            "by Mike Driscoll.</p>"

            "<p><b>Software used in making this demo:</h3></p>"

            '<p><b><a href="http://www.python.org">Python 2.4</a></b></p>'

            '<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>'
        )

class wxHTML(wx.html.HtmlWindow):

    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


# Run the program
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()