import sys
import wx
import snapshotPrinter

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Screenshot Tutorial")

        panel = wx.Panel(self)
        screenshotBtn = wx.Button(panel, label="Take Screenshot")
        screenshotBtn.Bind(wx.EVT_BUTTON, self.onTakeScreenShot)
        printBtn = wx.Button(panel, label="Print Screenshot")
        printBtn.Bind(wx.EVT_BUTTON, self.onPrint)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(screenshotBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(printBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    def onTakeScreenShot(self, event):
        """
        Takes a screenshot of the screen at give pos & size (rect).

        Method based on a script by Andrea Gavana
        """
        print('Taking screenshot...')
        rect = self.GetRect()

        # adjust widths for Linux (figured out by John Torres
        # http://article.gmane.org/gmane.comp.python.wxpython/67327)
        if sys.platform == 'linux2':
            client_x, client_y = self.ClientToScreen((0, 0))
            border_width = client_x - rect.x
            title_bar_height = client_y - rect.y
            rect.width += (border_width * 2)
            rect.height += title_bar_height + border_width

        # Create a DC for the whole screen area
        dcScreen = wx.ScreenDC()

        # Create a Bitmap that will hold the screenshot image later on
        # Note that the Bitmap must have a size big enough to hold the screenshot
        # -1 means using the current default colour depth
        bmp = wx.EmptyBitmap(rect.width, rect.height)

        #Create a memory DC that will be used for actually taking the screenshot
        memDC = wx.MemoryDC()

        # Tell the memory DC to use our Bitmap
        # all drawing action on the memory DC will go to the Bitmap now
        memDC.SelectObject(bmp)

        # Blit (in this case copy) the actual screen on the memory DC
        # and thus the Bitmap
        memDC.Blit( 0, # Copy to this X coordinate
                    0, # Copy to this Y coordinate
                    rect.width, # Copy this width
                    rect.height, # Copy this height
                    dcScreen, # Where to copy from
                    rect.x, # What's the X offset in the original DC?
                    rect.y  # What's the Y offset in the original DC?
                    )

        # Select the Bitmap out of the memory DC by selecting a new
        # uninitialized Bitmap
        memDC.SelectObject(wx.NullBitmap)

        img = bmp.ConvertToImage()
        fileName = "myImage.png"
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)
        print('...saving as png!')

    def onPrint(self, event):
        """
        Send screenshot to the printer
        """
        printer = snapshotPrinter.SnapshotPrinter()
        printer.sendToPrinter()

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
