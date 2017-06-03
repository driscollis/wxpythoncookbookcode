import controller
import os
import sys
import wx
from wx.lib.buttons import GenBitmapTextButton

appPath = os.path.abspath(os.path.dirname(os.path.join(sys.argv[0])))


class CloseBtn(GenBitmapTextButton):
    """
    Creates a reusable close button with a bitmap
    """

    def __init__(self, parent, label="Close"):
        """Constructor"""
        font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD)
        img = wx.Bitmap(r"%s/images/cancel.png" % appPath)
        GenBitmapTextButton.__init__(self, parent, wx.ID_CLOSE, img,
                                     label=label, size=(110, 50))
        self.SetFont(font)
        
        
class PreferencesDialog(wx.Dialog):
    """
    Creates and displays a preferences dialog that allows the user to
    change some settings.
    """

    def __init__(self):
        """
        Initialize the dialog
        """
        wx.Dialog.__init__(self, None, wx.ID_ANY, 'Preferences', size=(550,400))
        appPath = controller.appPath

        # Create widgets
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        serverLbl = wx.StaticText(self, label="Update Server:")
        self.serverTxt = wx.TextCtrl(self)
        self.serverTxt.Disable()

        usernameLbl = wx.StaticText(self, label="Username:")
        self.usernameTxt = wx.TextCtrl(self)
        self.usernameTxt.Disable()

        passwordLbl = wx.StaticText(self, label="Password:")
        self.passwordTxt = wx.TextCtrl(self,
                                       style=wx.TE_PASSWORD)
        self.passwordTxt.Disable()

        updateLbl = wx.StaticText(self, label="Update Interval:")
        self.updateTxt = wx.TextCtrl(self)
        minutesLbl = wx.StaticText(self, label="minutes")

        agencyLbl = wx.StaticText(self, label="Agency Filter:")
        choices = ["Include all agencies except",
                   "Exclude all agencies except"]
        self.agencyCbo = wx.ComboBox(
            self, value="Include all agencies except",
            choices=choices,
            style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.agencyCbo.SetFont(font)
        self.filterTxt = wx.TextCtrl(self, wx.ID_ANY, "")

        img = wx.Bitmap(r"%s/images/filesave.png" % appPath)
        saveBtn = GenBitmapTextButton(
            self, wx.ID_ANY, img, "Save", size=(110, 50))
        saveBtn.Bind(wx.EVT_BUTTON, self.savePreferences)
        cancelBtn = CloseBtn(self, label="Cancel")
        cancelBtn.Bind(wx.EVT_BUTTON, self.onCancel)

        # Set the widgets font
        widgets = [serverLbl, usernameLbl, passwordLbl,
                   updateLbl, agencyLbl, minutesLbl,
                   self.serverTxt, self.usernameTxt,
                   self.passwordTxt, self.updateTxt,
                   self.agencyCbo, self.filterTxt, saveBtn,
                   cancelBtn]
        for widget in widgets:
            widget.SetFont(font)

        # layout widgets
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        updateSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        prefSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        prefSizer.AddGrowableCol(1)

        prefSizer.Add(serverLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        prefSizer.Add(self.serverTxt, 0, wx.EXPAND)
        prefSizer.Add(usernameLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        prefSizer.Add(self.usernameTxt, 0, wx.EXPAND)
        prefSizer.Add(passwordLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        prefSizer.Add(self.passwordTxt, 0, wx.EXPAND)
        prefSizer.Add(updateLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        updateSizer.Add(self.updateTxt, 0, wx.RIGHT, 5)
        updateSizer.Add(minutesLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        prefSizer.Add(updateSizer)
        prefSizer.Add(agencyLbl, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        prefSizer.Add(self.agencyCbo, 0, wx.EXPAND)
        prefSizer.Add((20,20))
        prefSizer.Add(self.filterTxt, 0, wx.EXPAND)

        mainSizer.Add(prefSizer, 0, wx.EXPAND|wx.ALL, 5)
        btnSizer.Add(saveBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        self.SetSizer(mainSizer)

        # load preferences
        self.loadPreferences()
        
    def loadPreferences(self):
        """
        Load the preferences and fill the text controls
        """
        config = controller.get_config()
        updateServer = config['update server']
        username = config['username']
        password = config['password']
        interval = config['update interval']
        agencyFilter = config['agency filter']
        filters = config['filters']
    
        self.serverTxt.SetValue(updateServer)
        self.usernameTxt.SetValue(username)
        self.passwordTxt.SetValue(password)
        self.updateTxt.SetValue(interval)
        self.agencyCbo.SetValue(agencyFilter)
        self.filterTxt.SetValue(filters)
    
    
    def onCancel(self, event):
        """
        Closes the dialog
        """
        self.EndModal(0)
    
    
    def savePreferences(self, event):
        """
        Save the preferences
        """
        config = controller.get_config()
    
        config['update interval'] = self.updateTxt.GetValue()
        config['agency filter'] = str(self.agencyCbo.GetValue())
        data = self.filterTxt.GetValue()
        if "," in data:
            filters = [i.strip() for i in data.split(',')]
        elif " " in data:
            filters = [i.strip() for i in data.split(' ')]
        else:
            filters = [data]
        text = ""
        for f in filters:
            text += " " + f
        text = text.strip()
        config['filters'] = text
        config.write()
    
        dlg = wx.MessageDialog(
            self, "Preferences Saved!", 'Information',
            wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.EndModal(0)
            
if __name__ == "__main__":
    app = wx.App(False)
    dlg = PreferencesDialog()
    dlg.ShowModal()
    dlg.Destroy()
