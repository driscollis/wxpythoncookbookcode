# create a background image on a wxPython panel
# and show a button on top of the image

import wx

class Panel1(wx.Panel):
    """class Panel1 creates a panel with an image on it, inherits wx.Panel"""
    def __init__(self, parent, id):
        # create the panel
        wx.Panel.__init__(self, parent, id)
        try:
            # pick an image file you have in the working
            # folder you can load .jpg  .png  .bmp  or
            # .gif files
            image_file = 'big_cat.jpg'
            bmp1 = wx.Image(
                image_file,
                wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel
            # coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(
                self, -1, bmp1, (0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(),
                                  bmp1.GetHeight())
            parent.SetTitle(str1)
        except IOError:
            print("Image file %s not found" % imageFile)
            raise SystemExit

        # button goes on the image --> self.bitmap1 is the
        # parent
        self.button1 = wx.Button(
            self.bitmap1, label='Button1',
            pos=(8, 8))

app = wx.App(False)

# create a window/frame, no parent, -1 is default ID
# change the size of the frame to fit the backgound images
frame1 = wx.Frame(None, -1, "An image on a panel",
                  size=(350, 400))

# create the class instance
panel1 = Panel1(frame1, -1)
frame1.Show(True)
app.MainLoop()