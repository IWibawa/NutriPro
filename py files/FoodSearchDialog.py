# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FoodSearchDialog
###########################################################################

class FoodSearchDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select Food", pos = wx.DefaultPosition, size = wx.Size( 511,401 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.search_label = wx.StaticText( self, wx.ID_ANY, u"Search for Food:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_label.Wrap( 0 )
		bSizer12.Add( self.search_label, 0, wx.ALL, 5 )
		
		self.search_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_input.SetMaxLength( 0 ) 
		bSizer12.Add( self.search_input, 0, wx.ALL, 5 )
		
		self.search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_button.SetDefault() 
		self.search_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.search_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer12.Add( self.search_button, 0, wx.ALL, 5 )
		
		self.food_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,150 ), wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer12.Add( self.food_list, 0, wx.ALL, 5 )
		
		self.add_food_button = wx.Button( self, wx.ID_ANY, u"Select Food", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_food_button.SetDefault() 
		self.add_food_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.add_food_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer12.Add( self.add_food_button, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
	
	def __del__( self ):
		pass
	

