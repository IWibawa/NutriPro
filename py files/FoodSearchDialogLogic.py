import wx
import pandas as pd
from FoodSearchDialog import FoodSearchDialog


class FoodSearchDialogLogic(FoodSearchDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')
        self.selected_food = None

        self.search_button.Bind(wx.EVT_BUTTON, self.on_search)
        self.add_food_button.Bind(wx.EVT_BUTTON, self.on_select_food)

        self.initialize_list_control()

    def initialize_list_control(self):
        self.food_list.DeleteAllColumns()
        for i, column in enumerate(self.food_data.columns[:5]):  # Display first 5 columns
            self.food_list.InsertColumn(i, column)

    def on_search(self, event):
        query = self.search_input.GetValue().lower()
        # Use the first column (assumed to be the food name) for searching
        results = self.food_data[self.food_data.iloc[:, 0].str.lower().str.contains(query)]
        self.display_results(results)

    def display_results(self, results):
        self.food_list.DeleteAllItems()
        for index, row in results.iterrows():
            pos = self.food_list.InsertItem(index, str(row.iloc[0]))
            for col in range(1, 5):  # Display first 5 columns
                self.food_list.SetItem(pos, col, str(row.iloc[col]))

    def on_select_food(self, event):
        selected_item = self.food_list.GetFirstSelected()
        if selected_item != -1:
            self.selected_food = {
                'name': self.food_list.GetItemText(selected_item, 0),
                'calories': float(self.food_list.GetItemText(selected_item, 1)),
                'protein': float(self.food_list.GetItemText(selected_item, 2)),
                'carbs': float(self.food_list.GetItemText(selected_item, 3)),
                'fat': float(self.food_list.GetItemText(selected_item, 4))
            }
            self.EndModal(wx.ID_OK)

    def get_selected_food(self):
        return self.selected_food


# This allows the file to be run standalone for testing
if __name__ == '__main__':
    app = wx.App(False)
    dialog = FoodSearchDialogLogic(None)
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print(dialog.get_selected_food())
    dialog.Destroy()
    app.MainLoop()