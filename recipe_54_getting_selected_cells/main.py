import wx
import wx.grid as gridlib


class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.currentlySelectedCell = (0, 0)

        self.myGrid = gridlib.Grid(self)
        self.myGrid.CreateGrid(12, 8)
        self.myGrid.Bind(gridlib.EVT_GRID_SELECT_CELL, self.onSingleSelect)
        self.myGrid.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.onDragSelection)

        selectBtn = wx.Button(self, label="Get Selected Cells")
        selectBtn.Bind(wx.EVT_BUTTON, self.onGetSelection)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.myGrid, 1, wx.EXPAND)
        sizer.Add(selectBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)

    def onDragSelection(self, event):
        """
        Gets the cells that are selected by holding the left
        mouse button down and dragging
        """
        if self.myGrid.GetSelectionBlockTopLeft():
            top_left = self.myGrid.GetSelectionBlockTopLeft()[0]
            bottom_right = self.myGrid.GetSelectionBlockBottomRight()[0]
            self.printSelectedCells(top_left, bottom_right)

    def onGetSelection(self, event):
        """
        Get whatever cells are currently selected
        """
        cells = self.myGrid.GetSelectedCells()
        if not cells:
            if self.myGrid.GetSelectionBlockTopLeft():
                top_left = self.myGrid.GetSelectionBlockTopLeft()[0]
                bottom_right = self.myGrid.GetSelectionBlockBottomRight()[0]
                self.printSelectedCells(top_left, bottom_right)
            else:
                print(self.currentlySelectedCell)
        else:
            print(cells)

    def onSingleSelect(self, event):
        """
        Get the selection of a single cell by clicking or
        moving the selection with the arrow keys
        """
        print("You selected Row %s, Col %s" % (event.GetRow(),
                                               event.GetCol()))
        self.currentlySelectedCell = (event.GetRow(),
                                      event.GetCol())
        event.Skip()

    def printSelectedCells(self, top_left, bottom_right):
        """
        Based on code from
        http://ginstrom.com/scribbles/2008/09/07/getting-the-selected-cells-from-a-wxpython-grid/
        """
        cells = []

        rows_start = top_left[0]
        rows_end = bottom_right[0]

        cols_start = top_left[1]
        cols_end = bottom_right[1]

        rows = range(rows_start, rows_end+1)
        cols = range(cols_start, cols_end+1)

        cells.extend([(row, col)
                      for row in rows
                      for col in cols])

        print("You selected the following cells: ", cells)

        for cell in cells:
            row, col = cell
            print(self.myGrid.GetCellValue(row, col))


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Single Cell Selection")
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()