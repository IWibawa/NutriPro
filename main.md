#### **__init__**
- Initializes the MealPlanManager with an empty meal plan and food dataset
-	def __init__(self, food_dataset):
		self.meal_plan = {day: {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []} for day in
						  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
		self.food_dataset = food_dataset

#### **Add Food**
- Adds a food item to a specific day and meal
-	def add_food(self, day, meal, food):
		self.meal_plan[day][meal].append(food)

#### **Get Meal Plan**
- Returns the current meal plan
-	def get_meal_plan(self):
		return self.meal_plan

#### **Change Food**
- Replaces a food item in the meal plan with a new one
-	def change_food(self, day, meal, old_food_name, new_food):
		for i, food in enumerate(self.meal_plan[day][meal]):
			if food['name'] == old_food_name:
				self.meal_plan[day][meal][i] = new_food
				break

#### **Remove Food**
- Removes a food item from the meal plan
-	def remove_food(self, day, meal, food_name):
		self.meal_plan[day][meal] = [food for food in self.meal_plan[day][meal] if food['name'] != food_name]

#### **Clear Meal Plan**
- Clears the entire meal plan
-	def clear_meal_plan(self):
		for day in self.meal_plan:
			for meal in self.meal_plan[day]:
				self.meal_plan[day][meal] = []

#### **Clear Meal Plan for Day**
- Clears the meal plan for a specific day
-	def clear_meal_plan_for_day(self, day):
		self.meal_plan[day] = {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []}


### **MainApp**

#### **OnInit**
- Initializes the main application window and binds events
-	def OnInit(self):
		self.food_dataset = pd.read_csv('Food_Nutrition_Dataset.csv')
		self.meal_plan_manager = MealPlanManager(self.food_dataset)
		self.main_frame = MainFrame(None)
		self.main_frame.search_comparison_button.Bind(wx.EVT_BUTTON, self.on_search_compare)
		self.main_frame.meal_plan_button.Bind(wx.EVT_BUTTON, self.on_meal_plan)
		self.main_frame.exit_button.Bind(wx.EVT_BUTTON, self.on_exit)
		self.main_frame.Show()
		self.dataset_list = None
		self.meal_plan_frame = None

		return True

#### **On Search Compare**
- Event handler for the search and compare button
-	def on_search_compare(self, event):
		self.show_dataset_list()

#### **Show Dataset List**
- Displays the dataset list window
-	def show_dataset_list(self):
		if self.dataset_list is None:
			self.dataset_list = DatasetListLogic(self.main_frame, self.meal_plan_manager)
		self.dataset_list.Show()
		self.main_frame.Hide()
		if self.meal_plan_frame:
			self.meal_plan_frame.Hide()

#### **On Meal Plan**
- Event handler for the meal plan button
-	def on_meal_plan(self, event):
		self.show_meal_plan()

#### **Show Meal Plan**
- Displays the meal plan window
-	def show_meal_plan(self):
		if self.meal_plan_frame is None:
			self.meal_plan_frame = MealPlanFrameLogic(self.main_frame, self.meal_plan_manager)
		self.meal_plan_frame.Show()
		self.main_frame.Hide()
		if self.dataset_list:
			self.dataset_list.Hide()

#### **On Exit**
- Event handler for the exit button
-	def on_exit(self, event):
		self.main_frame.Close()