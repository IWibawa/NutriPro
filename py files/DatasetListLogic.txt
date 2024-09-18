import wx
import pandas as pd
import matplotlib.pyplot as plt
from DatasetList import DatassetList


class DatasetListLogic(DatassetList):
    def __init__(self, parent, meal_plan_manager):
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

        self.comparison_foods = []

        # Bind events
        self.search_button.Bind(wx.EVT_BUTTON, self.on_search)
        self.apply_filters.Bind(wx.EVT_BUTTON, self.on_apply_filters)
        self.generate_comparison_chart.Bind(wx.EVT_BUTTON, self.on_generate_chart)
        self.clear_comparison.Bind(wx.EVT_BUTTON, self.on_clear_comparison)
        self.add_to_meal_plan.Bind(wx.EVT_BUTTON, self.on_add_to_meal_plan)
        self.food_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_food_selected)
        self.go_to_meal_plan.Bind(wx.EVT_BUTTON, self.on_go_to_meal_plan)
        self.back_to_main_menu1.Bind(wx.EVT_BUTTON, self.on_back_to_main_menu)

        self.initialize_list_controls()
        self.display_results(self.food_data)

    def initialize_list_controls(self):
        # Initialize food_list
        for i, column in enumerate(self.food_data.columns):
            self.food_list.InsertColumn(i, column)

        # Initialize comparison_list
        self.comparison_list.InsertColumn(0, "Food")
        self.comparison_list.InsertColumn(1, "Calories")
        self.comparison_list.InsertColumn(2, "Protein")
        self.comparison_list.InsertColumn(3, "Carbs")
        self.comparison_list.InsertColumn(4, "Fat")

    def on_search(self, event):
        query = self.search_input.GetValue().lower()
        results = self.food_data[self.food_data.iloc[:, 0].str.lower().str.contains(query)]
        self.display_results(results)

    def on_apply_filters(self, event):
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

    def display_results(self, results):
        self.food_list.DeleteAllItems()
        for index, row in results.iterrows():
            pos = self.food_list.InsertItem(index, str(row.iloc[0]))
            for col, value in enumerate(row[1:], start=1):
                self.food_list.SetItem(pos, col, str(value))

    def on_food_selected(self, event):
        if self.comparison_list.GetItemCount() < 3:
            index = event.GetIndex()
            food = self.food_list.GetItemText(index, 0)
            calories = self.food_list.GetItemText(index, 1)
            protein = self.food_list.GetItemText(index, 2)
            carbs = self.food_list.GetItemText(index, 3)
            fat = self.food_list.GetItemText(index, 4)

            pos = self.comparison_list.InsertItem(self.comparison_list.GetItemCount(), food)
            self.comparison_list.SetItem(pos, 1, calories)
            self.comparison_list.SetItem(pos, 2, protein)
            self.comparison_list.SetItem(pos, 3, carbs)
            self.comparison_list.SetItem(pos, 4, fat)

    def on_generate_chart(self, event):
        if self.comparison_list.GetItemCount() == 0:
            return

        data = []
        for i in range(self.comparison_list.GetItemCount()):
            food = self.comparison_list.GetItemText(i, 0)
            calories = float(self.comparison_list.GetItemText(i, 1))
            protein = float(self.comparison_list.GetItemText(i, 2))
            carbs = float(self.comparison_list.GetItemText(i, 3))
            fat = float(self.comparison_list.GetItemText(i, 4))
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

    def on_clear_comparison(self, event):
        self.comparison_list.DeleteAllItems()

    def on_add_to_meal_plan(self, event):
        selected_index = self.food_list.GetFirstSelected()
        if selected_index != -1:
            food = self.get_food_from_list(selected_index)
            meal = self.get_selected_meal()
            day = "Monday"  # You might want to add a day selection option
            self.meal_plan_manager.add_food(day, meal, food)
            wx.MessageBox(f"Added {food['name']} to {meal} on {day}", "Food Added", wx.OK | wx.ICON_INFORMATION)

    def get_food_from_list(self, index):
        return {
            'name': self.food_list.GetItemText(index, 0),
            'calories': float(self.food_list.GetItemText(index, 1)),
            'protein': float(self.food_list.GetItemText(index, 2)),
            'carbs': float(self.food_list.GetItemText(index, 3)),
            'fat': float(self.food_list.GetItemText(index, 4))
        }

    def get_selected_meal(self):
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

    def on_go_to_meal_plan(self, event):
        self.Hide()
        wx.GetApp().show_meal_plan()

    def on_back_to_main_menu(self, event):
        self.Hide()
        wx.GetApp().main_frame.Show()


# This allows the file to be run standalone for testing
if __name__ == '__main__':
    app = wx.App(False)
    frame = DatasetListLogic(None, MealPlanManager())
    frame.Show(True)
    app.MainLoop()