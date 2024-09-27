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
## Class MealPlanFrame
###########################################################################

class MealPlanFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Meal Plan", pos=wx.DefaultPosition,
                          size=wx.Size(800, 720), style=wx.DEFAULT_FRAME_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(153, 180, 209))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Meal Plan Overview"), wx.HORIZONTAL)

        self.select_day_label = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Select Day:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.select_day_label.Wrap(0)
        sbSizer5.Add(self.select_day_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        day_choiceChoices = []
        self.day_choice = wx.Choice(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    day_choiceChoices, 0)
        self.day_choice.SetSelection(0)
        sbSizer5.Add(self.day_choice, 0, wx.ALL, 5)

        self.weekly_view_button = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Switch to Weekly View",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekly_view_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.weekly_view_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        sbSizer5.Add(self.weekly_view_button, 0, wx.ALL, 5)

        self.generate_meal_plan_button1 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Generate Meal Plan",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.generate_meal_plan_button1.SetForegroundColour(wx.Colour(244, 247, 252))
        self.generate_meal_plan_button1.SetBackgroundColour(wx.Colour(0, 120, 215))

        sbSizer5.Add(self.generate_meal_plan_button1, 0, wx.ALL, 5)

        bSizer9.Add(sbSizer5, 0, wx.EXPAND, 5)

        self.meal_plan_list = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 400), 0)

        # Grid
        self.meal_plan_list.CreateGrid(5, 5)
        self.meal_plan_list.EnableEditing(True)
        self.meal_plan_list.EnableGridLines(True)
        self.meal_plan_list.EnableDragGridSize(False)
        self.meal_plan_list.SetMargins(0, 0)

        # Columns
        self.meal_plan_list.EnableDragColMove(False)
        self.meal_plan_list.EnableDragColSize(True)
        self.meal_plan_list.SetColLabelSize(30)
        self.meal_plan_list.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.meal_plan_list.EnableDragRowSize(True)
        self.meal_plan_list.SetRowLabelSize(80)
        self.meal_plan_list.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.meal_plan_list.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer9.Add(self.meal_plan_list, 0, wx.ALL, 5)

        self.nutrient_summary = wx.StaticText(self, wx.ID_ANY,
                                              u"Total for the day: Calories: 0, Protein: 0g, Carbs: 0g, Fat: 0g",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.nutrient_summary.Wrap(0)
        bSizer9.Add(self.nutrient_summary, 0, wx.EXPAND | wx.ALL, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.add_food_button = wx.Button(self, wx.ID_ANY, u"Add Food", wx.DefaultPosition, wx.DefaultSize, 0)
        self.add_food_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.add_food_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer10.Add(self.add_food_button, 1, wx.ALL, 5)

        self.change_food_button = wx.Button(self, wx.ID_ANY, u"Change Food", wx.DefaultPosition, wx.DefaultSize, 0)
        self.change_food_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.change_food_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer10.Add(self.change_food_button, 1, wx.ALL, 5)

        self.remove_food_button = wx.Button(self, wx.ID_ANY, u"Remove Food", wx.DefaultPosition, wx.DefaultSize, 0)
        self.remove_food_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.remove_food_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer10.Add(self.remove_food_button, 1, wx.ALL, 5)

        self.clear_meal_plan_button = wx.Button(self, wx.ID_ANY, u"Clear Meal Plan", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.clear_meal_plan_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.clear_meal_plan_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer10.Add(self.clear_meal_plan_button, 1, wx.ALL, 5)

        bSizer9.Add(bSizer10, 0, wx.EXPAND | wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.back_to_main_menu = wx.Button(self, wx.ID_ANY, u"Back to Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.back_to_main_menu.SetForegroundColour(wx.Colour(244, 247, 252))
        self.back_to_main_menu.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer12.Add(self.back_to_main_menu, 1, wx.ALL | wx.EXPAND, 5)

        self.go_to_data_list = wx.Button(self, wx.ID_ANY, u"Go to Data List", wx.DefaultPosition, wx.DefaultSize, 0)
        self.go_to_data_list.SetForegroundColour(wx.Colour(244, 247, 252))
        self.go_to_data_list.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer12.Add(self.go_to_data_list, 1, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(bSizer12, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

    def __del__(self):
        pass


