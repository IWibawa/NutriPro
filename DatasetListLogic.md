
#### **__init__**
- Initializes the DatasetListLogic class
- 	def __init__(self, parent, meal_plan_manager):
		super().__init__(parent)

		self.meal_plan_manager = meal_plan_manager

		try:
			self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')
			print("Dataset loaded successfully.")
			print("Columns in the dataset:", self.food_data.columns.tolist())
			print("First few rows of the dataset:")
			print(self.food_data.head())
		except Exception as e:
			print(f"Error loading dataset: {e}")
			wx.MessageBox(f"Error loading dataset: {e}", "Error", wx.OK | wx.ICON_ERROR)
			self.food_data = pd.DataFrame()

		self.comparison_f
		self.search_button.Bind(wx.EVT_BUTTON, self.on_search)
		self.apply_filters.Bind(wx.EVT_BUTTON, self.on_apply_filters)
		self.generate_comparison_chart.Bind(wx.EVT_BUTTON, self.on_generate_chart)
		self.clear_comparison.Bind(wx.EVT_BUTTON, self.on_clear_comparison)
		self.add_to_meal_plan.Bind(wx.EVT_BUTTON, self.on_add_to_meal_plan)
		self.go_to_meal_plan.Bind(wx.EVT_BUTTON, self.on_go_to_meal_plan)
		self.back_to_main_menu1.Bind(wx.EVT_BUTTON, self.on_back_to_main_menu)
		self.add_to_comaprison_table.Bind(wx.EVT_BUTTON, self.on_add_to_comparison)

        self.initialize_grid_controls()
        self.display_results(self.food_data)
		
#### **Initialize Grid Controls**
- Sets up the initial state of the grid controls
-   def initialize_grid_controls(se
        self.food_list.ClearGrid()
        if self.food_list.GetNumberCols() > 0:
            self.food_list.DeleteCols(0, self.food_list.GetNumberCols())
        self.food_list.AppendCols(len(self.food_data.columns))
        for i, column in enumerate(self.food_data.columns):
            self.food_list.SetColLabelValue(i, col
        self.comparison_list.ClearGrid()
        if self.comparison_list.GetNumberCols() > 0:
            self.comparison_list.DeleteCols(0, self.comparison_list.GetNumberCols())
        self.comparison_list.AppendCols(5)
        self.comparison_list.SetColLabelValue(0, "Food")
        self.comparison_list.SetColLabelValue(1, "Calories")
        self.comparison_list.SetColLabelValue(2, "Protein")
        self.comparison_list.SetColLabelValue(3, "Carbs")
        self.comparison_list.SetColLabelValue(4, "Fat")
		
#### **Display Results**
- Shows the filtered or searched results in the grid
-   def display_results(self, results):
        self.food_list.ClearGrid()
        if self.food_list.GetNumberRows() > 0:
            self.food_list.DeleteRows(0, self.food_list.GetNumberRows())
        self.food_list.AppendRows(len(results))

        for row_idx, (_, row) in enumerate(results.iterrows()):
            for col_idx, value in enumerate(row):
                self.food_list.SetCellValue(row_idx, col_idx, str(valu
        for col in range(self.food_list.GetNumberCols()):
            self.food_list.AutoSizeColumn(col)
			
#### **Search**
- Performs a search based on user input
-   def on_search(self, event):
		query = self.search_input.GetValue().lower()
		results = self.food_data[self.food_data.iloc[:, 0].str.lower().str.contains(query)]
		self.display_results(results)
		
#### **Apply Filters**
 - Applies selected filters to the dataset
 -  def on_apply_filters(self, event):
        filtered_data = self.food_data.copy()

        protein_col = self.food_data.columns[self.food_data.columns.str.contains('Protein', case=False)][0]
        carbs_col = self.food_data.columns[self.food_data.columns.str.contains('Carbohydrate', case=False)][0]
        fat_col = self.food_data.columns[self.food_data.columns.str.contains('Fat', case=False)][0]

        if self.filter_protein.GetValue():
            filtered_data = filtered_data[filtered_data[protein_col] > 20]
        if self.filter_carbs.GetValue():
            filtered_data = filtered_data[filtered_data[carbs_col] < 20]
        if self.filter_fat.GetValue():
            filtered_data = filtered_data[filtered_data[fat_col] < 5]

        self.display_results(filtered_data)
		
#### **Add to Comparison**
 - Adds a selected food item to the comparison table
 -  def on_add_to_comparison(self, event):
        selected_row = self.food_list.GetGridCursorRow()
        if selected_row != -1:
            food = self.get_food_from_grid(selected_row)
            if food:
                # Debug information
                print(f"Current rows in comparison table: {self.comparison_list.GetNumberRows()}")
                print(f"Current non-empty rows: {self.get_non_empty_rows()}")

                # Check if there's space in the comparison table
                non_empty_rows = self.get_non_empty_rows()
                if len(non_empty_rows) < 5:
                    new_row = len(non_empty_rows)
                    if new_row >= self.comparison_list.GetNumberRows():
                        self.comparison_list.AppendRows(1)
                    
                    self.comparison_list.SetCellValue(new_row, 0, food['name'])
                    self.comparison_list.SetCellValue(new_row, 1, str(food['calories']))
                    self.comparison_list.SetCellValue(new_row, 2, str(food['protein']))
                    self.comparison_list.SetCellValue(new_row, 3, str(food['carbs']))
                    self.comparison_list.SetCellValue(new_row, 4, str(food['fat']))

                    self.comparison_list.AutoSize()
                    wx.MessageBox(f"Added {food['name']} to comparison table", "Food Added", wx.OK | wx.ICON_INFORMATION)
                else:
                    wx.MessageBox("Comparison table is full. Remove some items to add more.", "Table Full", wx.OK | wx.ICON_WARNING)
        else:
            wx.MessageBox("Please select a food item from the list.", "No Selection", wx.OK | wx.ICON_INFORMATION)
			
#### **Get Non-Empty Rows**
- Returns a list of indices of non-empty rows in the comparison table
-	def get_non_empty_rows(self):
		non_empty_rows = []
		for row in range(self.comparison_list.GetNumberRows()):
			if self.comparison_list.GetCellValue(row, 0):
				non_empty_rows.append(row)
		return non_empty_rows

#### **Get Food from Grid**
- Retrieves food information from a selected grid row
-   def get_food_from_grid(self, row):
        return {
            'name': self.food_list.GetCellValue(row, 0),
            'calories': float(self.food_list.GetCellValue(row, 1)),
            'protein': float(self.food_list.GetCellValue(row, 8)),  # Assuming protein is in column 8
            'carbs': float(self.food_list.GetCellValue(row, 6)),  # Assuming carbs is in column 6
            'fat': float(self.food_list.GetCellValue(row, 2))  # Assuming fat is in column 2
        }
		
#### **Generate Chart**
- Creates and displays a comparison chart of selected foods
-   def on_generate_chart(self, event):
        if self.comparison_list.GetNumberRows() == 0:
            wx.MessageBox("Please add items to the comparison table first.", "Empty Comparison",
                          wx.OK | wx.ICON_INFORMATION)
            return

        data = []
        for i in range(self.comparison_list.GetNumberRows()):
            food = self.comparison_list.GetCellValue(i, 0)
            calories = self.comparison_list.GetCellValue(i, 1)
            protein = self.comparison_list.GetCellValue(i, 2)
            carbs = self.comparison_list.GetCellValue(i, 3)
            fat = self.comparison_list.GetCellValue(i, 4)

            try:
                calories = float(calories) if calories else 0
                protein = float(protein) if protein else 0
                carbs = float(carbs) if carbs else 0
                fat = float(fat) if fat else 0
            except ValueError:
                wx.MessageBox(f"Invalid data for {food}. Please check the values.", "Data Error", wx.OK | wx.ICON_ERROR)
                return

            data.append([food, calories, protein, carbs, fat])

        df = pd.DataFrame(data, columns=['Food', 'Calories', 'Protein', 'Carbs', 'Fat'])
        df.set_index('Food', inplace=True)

        ax = df.plot(kind='bar', figsize=(10, 6))
        plt.title('Nutrient Comparison')
        plt.xlabel('Food')
        plt.ylabel('Amount')
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()
		
#### **Clear Comparison**
- Removes all items from the comparison table
-   def on_clear_comparison(self, event):
        self.comparison_list.ClearGrid()
        if self.comparison_list.GetNumberRows() > 0:
            self.comparison_list.DeleteRows(0, self.comparison_list.GetNumberRows())
			
#### **Add to Meal Plan**
- Adds a selected food item to the meal plan
-   def on_add_to_meal_plan(self, event):
        selected_row = self.food_list.GetGridCursorRow()
        if selected_row != -1:
            food = self.get_food_from_grid(selected_row)
            meal = self.get_selected_meal()
            day = "Monday"  # You might want to add a day selection option
            self.meal_plan_manager.add_food(day, meal, food)
            wx.MessageBox(f"Added {food['name']} to {meal} on {day}", "Food Added", wx.OK | wx.ICON_INFORMATION)
			
#### **Get Selected Meal**
- Determines which meal type is currently selected
-   def get_selected_meal(self):
        if self.meal_plan_breakfast.GetValue():
            return "Breakfast"
        elif self.meal_plan_lunch.GetValue():
            return "Lunch"
        elif self.meal_plan_dinner.GetValue():
            return "Dinner"
        elif self.meal_plan_snack.GetValue():
            return "Snack"
        else:
            return "Breakfast"  # Default to breakfast if nothing is selected
			
#### **Go to Meal Plan**
- Navigates to the meal plan view
-   def on_go_to_meal_plan(self, event):
        self.Hide()
        wx.GetApp().show_meal_plan()

#### **Back to Main Menu**
- Returns to the main menu of the application
-   def on_back_to_main_menu(self, event):
        self.Hide()
        wx.GetApp().main_frame.Show()