# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class FoodSearchDialog
###########################################################################

class FoodSearchDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Select Food", pos=wx.DefaultPosition,
                           size=wx.Size(511, 401), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.search_label = wx.StaticText(self, wx.ID_ANY, u"Search for Food:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_label.Wrap(0)
        bSizer12.Add(self.search_label, 0, wx.ALL, 5)

        self.search_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_input.SetMaxLength(0)
        bSizer12.Add(self.search_input, 0, wx.ALL, 5)

        self.search_button = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_button.SetDefault()
        self.search_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.search_button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer12.Add(self.search_button, 0, wx.ALL, 5)

        self.food_list = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 400), 0)

        # Grid
        self.food_list.CreateGrid(5, 5)
        self.food_list.EnableEditing(True)
        self.food_list.EnableGridLines(True)
        self.food_list.EnableDragGridSize(False)
        self.food_list.SetMargins(0, 0)

        # Columns
        self.food_list.EnableDragColMove(False)
        self.food_list.EnableDragColSize(True)
        self.food_list.SetColLabelSize(30)
        self.food_list.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.food_list.EnableDragRowSize(True)
        self.food_list.SetRowLabelSize(80)
        self.food_list.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.food_list.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer12.Add(self.food_list, 0, wx.ALL, 5)

        self.add_food_button = wx.Button(self, wx.ID_ANY, u"Select Food", wx.DefaultPosition, wx.DefaultSize, 0)
        self.add_food_button.SetDefault()
        self.add_food_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.add_food_button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer12.Add(self.add_food_button, 0, wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

    def __del__(self):
        pass


