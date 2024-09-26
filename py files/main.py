import wx
import warnings
import pandas as pd  # To handle the dataset

from MainFrame import MainFrame
from DatasetListLogic import DatasetListLogic
from MealPlanFrameLogic import MealPlanFrameLogic

warnings.filterwarnings("ignore", category=wx.wxPyDeprecationWarning)

class MealPlanManager:
    def __init__(self, food_dataset):
        self.meal_plan = {day: {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []} for day in
                          ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
        self.food_dataset = food_dataset

    def add_food(self, day, meal, food):
        self.meal_plan[day][meal].append(food)

    def get_meal_plan(self):
        return self.meal_plan

    def change_food(self, day, meal, old_food_name, new_food):
        for i, food in enumerate(self.meal_plan[day][meal]):
            if food['name'] == old_food_name:
                self.meal_plan[day][meal][i] = new_food
                break

    def remove_food(self, day, meal, food_name):
        self.meal_plan[day][meal] = [food for food in self.meal_plan[day][meal] if food['name'] != food_name]

    def clear_meal_plan(self):
        for day in self.meal_plan:
            for meal in self.meal_plan[day]:
                self.meal_plan[day][meal] = []

    def clear_meal_plan_for_day(self, day):
        """ Clear the meal plan for a specific day (used in random meal generation) """
        self.meal_plan[day] = {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []}


class MainApp(wx.App):
    def OnInit(self):
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

    def on_search_compare(self, event):
        self.show_dataset_list()

    def show_dataset_list(self):
        if self.dataset_list is None:
            self.dataset_list = DatasetListLogic(self.main_frame, self.meal_plan_manager)
        self.dataset_list.Show()
        self.main_frame.Hide()
        if self.meal_plan_frame:
            self.meal_plan_frame.Hide()

    def on_meal_plan(self, event):
        self.show_meal_plan()

    def show_meal_plan(self):
        if self.meal_plan_frame is None:
            self.meal_plan_frame = MealPlanFrameLogic(self.main_frame, self.meal_plan_manager)
        self.meal_plan_frame.Show()
        self.main_frame.Hide()
        if self.dataset_list:
            self.dataset_list.Hide()

    def on_exit(self, event):
        self.main_frame.Close()


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
