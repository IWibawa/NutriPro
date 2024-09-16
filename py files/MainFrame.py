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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Main Menu", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.main_title = wx.StaticText( self, wx.ID_ANY, u"NutriPro", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.main_title.Wrap( 0 )
		self.main_title.SetFont( wx.Font( 24, 72, 90, 92, False, "Times New Roman" ) )
		
		bSizer11.Add( self.main_title, 0, wx.ALL, 5 )
		
		self.search_comparison_button = wx.Button( self, wx.ID_ANY, u"Search  Compare Foods", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_comparison_button.SetDefault() 
		self.search_comparison_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.search_comparison_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer11.Add( self.search_comparison_button, 0, wx.ALL, 5 )
		
		self.meal_plan_button = wx.Button( self, wx.ID_ANY, u"Meal Plan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.meal_plan_button.SetDefault() 
		self.meal_plan_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.meal_plan_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer11.Add( self.meal_plan_button, 0, wx.ALL, 5 )
		
		self.exit_button = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exit_button.SetDefault() 
		self.exit_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.exit_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer11.Add( self.exit_button, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
	
	def __del__( self ):
		pass
	

