## **FoodSearchDialogLogic**

#### **__init__**
- Initializes the FoodSearchDialogLogic class
	```python
	def __init__(self, parent):
		super().__init__(parent)
		
		self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')
		self.selected_food = None
		self.search_button.Bind(wx.EVT_BUTTON, self.on_search)
		self.add_food_button.Bind(wx.EVT_BUTTON, self.on_select_food)
		self.initialize_grid()
		self.adjust_layout()
		self.SetSize((800, 600))
	```

#### **Initialize Grid**
- Sets up the initial state of the grid control
	```python
	def initialize_grid(self):
		self.food_list.ClearGrid()
		if self.food_list.GetNumberCols() > 0:
		   self.food_list.DeleteCols(0, self.food_list.GetNumberCols())
		
		self.food_list.AppendCols(5)
		column_labels = self.food_data.columns[:5].tolist()
		
		for col, label in enumerate(column_labels):
		   self.food_list.SetColLabelValue(col, label)
		   
		self.food_list.SetMinSize((600, 400))
		self.food_list.EnableScrolling(True, True)
		self.food_list.AutoSizeColumns()
		self.food_list.AutoSizeRows()
	```

#### **Adjust Layout**
- Adjusts the layout of the dialog
	```python
	def adjust_layout(self):
		main_sizer = self.GetSizer()
		for item in main_sizer.GetChildren():
		   if item.GetWindow() == self.food_list:
			  item.SetProportion(1)
			  item.SetFlag(wx.EXPAND | wx.ALL)
			  break
		
		self.Layout()
	```

#### **Search**
- Performs a search based on user input
	```python
	def on_search(self, event):
		query = self.search_input.GetValue().lower()
		results = self.food_data[self.food_data.iloc[:, 0].str.lower().str.contains(query)]
		self.display_results(results)
	```

#### **Display Results**
- Shows the search results in the grid
	```python
	def display_results(self, results):
		self.food_list.ClearGrid()
		if self.food_list.GetNumberRows() > 0:
		   self.food_list.DeleteRows(0, self.food_list.GetNumberRows())
	
		self.food_list.AppendRows(len(results))
	
		for row_idx, (_, row) in enumerate(results.iterrows()):
		   for col_idx in range(5):
			  self.food_list.SetCellValue(row_idx, col_idx, str(row.iloc[col_idx]))
	
		self.food_list.AutoSizeColumns()
	```

#### **Select Food**
- Handles the selection of a food item from the grid
	```python
	def on_select_food(self, event):
		selected_row = self.food_list.GetGridCursorRow()
		if selected_row != -1:
		   self.selected_food = {
			  'name': self.food_list.GetCellValue(selected_row, 0),
			  'calories': float(self.food_list.GetCellValue(selected_row, 1)),
			  'protein': float(self.food_list.GetCellValue(selected_row, 2)),
			  'carbs': float(self.food_list.GetCellValue(selected_row, 3)),
			  'fat': float(self.food_list.GetCellValue(selected_row, 4))
		   }
		   self.EndModal(wx.ID_OK)
	```

#### **Get Selected Food**
- Returns the selected food item
	```python
	def get_selected_food(self):
		return self.selected_food
	```