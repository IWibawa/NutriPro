#### **__init__**
- Initializes the MealPlanFrameLogic class
-	def __init__(self, parent, meal_plan_manager):
		super().__init__(parent)

		self.meal_plan_manager = meal_plan_manager
		self.current_view = 'daily'

		self.food_dataset = pd.read_csv('Food_Nutrition_Dataset.csv')  # Load dataset into a DataFrame

		self.day_choice.SetItems(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
		self.day_choice.SetSelection(0)

		self.initialize_grid()
		self.adjust_layout()

		self.day_choice.Bind(wx.EVT_CHOICE, self.on_day_selected)
		self.weekly_view_button.Bind(wx.EVT_BUTTON, self.toggle_view)
		self.generate_meal_plan_button1.Bind(wx.EVT_BUTTON, self.on_generate_random_meal_plan)
		self.add_food_button.Bind(wx.EVT_BUTTON, self.on_add_food)
		self.change_food_button.Bind(wx.EVT_BUTTON, self.on_change_food)
		self.remove_food_button.Bind(wx.EVT_BUTTON, self.on_remove_food)
		self.clear_meal_plan_button.Bind(wx.EVT_BUTTON, self.on_clear_meal_plan)
		self.back_to_main_menu.Bind(wx.EVT_BUTTON, self.on_back_to_main_menu)
		self.go_to_data_list.Bind(wx.EVT_BUTTON, self.on_go_to_data_list)

		self.update_meal_plan_display()

		self.SetSize((650, 600))

#### **Initialize Grid**
- Sets up the initial state of the grid control
-	def initialize_grid(self):
		self.meal_plan_list.ClearGrid()

		if self.meal_plan_list.GetNumberCols() > 0:
			self.meal_plan_list.DeleteCols(0, self.meal_plan_list.GetNumberCols())

		self.meal_plan_list.AppendCols(7)

		column_labels = ["Day", "Meal", "Food", "Calories", "Protein (g)", "Carbs (g)", "Fat (g)"]
		for col, label in enumerate(column_labels):
			self.meal_plan_list.SetColLabelValue(col, label)

		self.meal_plan_list.SetMinSize((600, 400))

		self.meal_plan_list.EnableScrolling(True, True)

		self.meal_plan_list.AutoSizeColumns()
		self.meal_plan_list.AutoSizeRows()

#### **Adjust Layout**
- Adjusts the layout of the frame
-	def adjust_layout(self):
		main_sizer = self.GetSizer()

		for item in main_sizer.GetChildren():
			if item.GetWindow() == self.meal_plan_list:
				item.SetProportion(1)
				item.SetFlag(wx.EXPAND | wx.ALL)
				break

		self.Layout()

#### **On Day Selected**
- Handles the event when a day is selected
-	def on_day_selected(self, event):
		self.update_meal_plan_display()

#### **Toggle View**
- Switches between daily and weekly view
-	def toggle_view(self, event):
		self.current_view = 'weekly' if self.current_view == 'daily' else 'daily'
		self.weekly_view_button.SetLabel(
			"Switch to Daily View" if self.current_view == 'weekly' else "Switch to Weekly View")
		self.update_meal_plan_display()

#### **Update Meal Plan Display**
- Updates the displayed meal plan based on the current view
-	def update_meal_plan_display(self):
		self.meal_plan_list.ClearGrid()
		if self.meal_plan_list.GetNumberRows() > 0:
			self.meal_plan_list.DeleteRows(0, self.meal_plan_list.GetNumberRows())
		meal_plan = self.meal_plan_manager.get_meal_plan()
		if self.current_view == 'daily':
			day = self.day_choice.GetStringSelection()
			self.display_day(day, meal_plan[day])
		else:
			for day in meal_plan:
				self.display_day(day, meal_plan[day])
		self.update_nutrient_summary()
		self.meal_plan_list.AutoSizeColumns()

#### **Display Day**
- Displays the meal plan for a specific day
-	def display_day(self, day, day_plan):
		for meal, foods in day_plan.items():
			for food in foods:
				row = self.meal_plan_list.GetNumberRows()
				self.meal_plan_list.AppendRows(1)
				self.meal_plan_list.SetCellValue(row, 0, day)
				self.meal_plan_list.SetCellValue(row, 1, meal)
				self.meal_plan_list.SetCellValue(row, 2, food['name'])
				self.meal_plan_list.SetCellValue(row, 3, str(food['calories']))
				self.meal_plan_list.SetCellValue(row, 4, str(food['protein']))
				self.meal_plan_list.SetCellValue(row, 5, str(food['carbs']))
				self.meal_plan_list.SetCellValue(row, 6, str(food['fat']))

		self.meal_plan_list.SetColSize(0, 100)  # Day column
		self.meal_plan_list.SetColSize(1, 80)  # Meal column
		self.meal_plan_list.SetColSize(2, 200)  # Food column
		for i in range(3, 7):
			self.meal_plan_list.SetColSize(i, 80)  # Nutrient columns

#### **Update Nutrient Summary**
- Calculates and displays the total nutrients for the current view
-	def update_nutrient_summary(self):
		meal_plan = self.meal_plan_manager.get_meal_plan()
		if self.current_view == 'daily':
			day = self.day_choice.GetStringSelection()
			total_calories = sum(float(food['calories']) for meal in meal_plan[day].values() for food in meal)
			total_protein = sum(float(food['protein']) for meal in meal_plan[day].values() for food in meal)
			total_carbs = sum(float(food['carbs']) for meal in meal_plan[day].values() for food in meal)
			total_fat = sum(float(food['fat']) for meal in meal_plan[day].values() for food in meal)
		else:
			total_calories = sum(
				float(food['calories']) for day in meal_plan.values() for meal in day.values() for food in meal)
			total_protein = sum(
				float(food['protein']) for day in meal_plan.values() for meal in day.values() for food in meal)
			total_carbs = sum(
				float(food['carbs']) for day in meal_plan.values() for meal in day.values() for food in meal)
			total_fat = sum(float(food['fat']) for day in meal_plan.values() for meal in day.values() for food in meal)

		summary = f"Total for the {'week' if self.current_view == 'weekly' else 'day'}: "
		summary += f"Calories: {total_calories:.0f}, Protein: {total_protein:.1f}g, Carbs: {total_carbs:.1f}g, Fat: {total_fat:.1f}g"
		self.nutrient_summary.SetLabel(summary)

#### **Generate Random Meal Plan**
- Generates a random well-balanced meal plan for the entire week
-	def on_generate_random_meal_plan(self, event):
		days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		meals = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
		self.meal_plan_manager.clear_meal_plan()
		for day in days:
			for meal in meals:
				selected_foods = self.generate_balanced_meal()
				for food in selected_foods:
					self.meal_plan_manager.add_food(day, meal, food)
		self.update_meal_plan_display()

#### **Generate Balanced Meal**
- Selects a random set of food items from the dataset that form a balanced meal
-	def generate_balanced_meal(self):
		calorie_target = 600
		protein_target = 30
		carb_target = 50
		fat_target = 20
		selected_foods = []
		total_calories, total_protein, total_carbs, total_fat = 0, 0, 0, 0
		keywords = ['cooked', 'baked', 'grilled', 'roasted', 'fried', 'stewed', 'braised']
		potential_foods = self.food_dataset[
			self.food_dataset['food'].str.contains('|'.join(keywords), case=False, na=False)
		]
		if potential_foods.empty:
			print("No cooked meals found in the dataset.")
			return selected_foods
		while total_calories < calorie_target:
			food = potential_foods.sample().iloc[0]
			total_calories += food['Caloric Value']
			total_protein += food['Protein']
			total_carbs += food['Carbohydrates']
			total_fat += food['Fat']

			selected_foods.append({
				'name': food['food'],
				'calories': food['Caloric Value'],
				'protein': food['Protein'],
				'carbs': food['Carbohydrates'],
				'fat': food['Fat']
			})
			if total_calories >= calorie_target and total_protein >= protein_target:
				break

		return selected_foods

#### **Add Food**
- Handles adding a food item to the meal plan
-	def on_add_food(self, event):
		dialog = FoodSearchDialogLogic(self)
		if dialog.ShowModal() == wx.ID_OK:
			food = dialog.get_selected_food()
			if food:
				day = self.day_choice.GetStringSelection()
				meal_dialog = wx.SingleChoiceDialog(self, "Choose a meal", "Add to Meal",
													['Breakfast', 'Lunch', 'Dinner', 'Snack'])
				if meal_dialog.ShowModal() == wx.ID_OK:
					meal = meal_dialog.GetStringSelection()
					self.meal_plan_manager.add_food(day, meal, food)
					self.update_meal_plan_display()
				meal_dialog.Destroy()
		dialog.Destroy()

#### **Change Food**
- Handles changing a food item in the meal plan
-	def on_change_food(self, event):
		row = self.meal_plan_list.GetGridCursorRow()
		if row != -1:
			day = self.meal_plan_list.GetCellValue(row, 0)
			meal = self.meal_plan_list.GetCellValue(row, 1)
			food_name = self.meal_plan_list.GetCellValue(row, 2)

			dialog = FoodSearchDialogLogic(self)
			if dialog.ShowModal() == wx.ID_OK:
				new_food = dialog.get_selected_food()
				if new_food:
					self.meal_plan_manager.change_food(day, meal, food_name, new_food)
					self.update_meal_plan_display()
			dialog.Destroy()

#### **Remove Food**
- Handles removing a food item from the meal plan
-	def on_remove_food(self, event):
		row = self.meal_plan_list.GetGridCursorRow()
		if row != -1:
			day = self.meal_plan_list.GetCellValue(row, 0)
			meal = self.meal_plan_list.GetCellValue(row, 1)
			food_name = self.meal_plan_list.GetCellValue(row, 2)
			self.meal_plan_manager.remove_food(day, meal, food_name)
			self.update_meal_plan_display()

#### **Clear Meal Plan**
- Clears the entire meal plan
-	def on_clear_meal_plan(self, event):
		self.meal_plan_manager.clear_meal_plan()
		self.update_meal_plan_display()

#### **Go to Data List**
- Navigates to the dataset list view
-	def on_go_to_data_list(self, event):
		self.Hide()
		wx.GetApp().show_dataset_list()

#### **Back to Main Menu**
- Returns to the main menu of the application
-	def on_back_to_main_menu(self, event):
		self.Hide()
		wx.GetApp().main_frame.Show()