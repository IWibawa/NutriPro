import wx
import wx.grid
import pandas as pd
from FoodSearchDialog import FoodSearchDialog


class FoodSearchDialogLogic(FoodSearchDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.food_data = pd.read_csv('Food_Nutrition_Dataset.csv')
        self.selected_food = None

        self.search_button.Bind(wx.EVT_BUTTON, self.on_search)
        self.add_food_button.Bind(wx.EVT_BUTTON, self.on_select_food)

        self.initialize_grid()
        self.adjust_layout()

        # Set initial size
        self.SetSize((800, 600))

    def initialize_grid(self):
        # Clear existing grid
        self.food_list.ClearGrid()

        # If there are existing columns, delete them
        if self.food_list.GetNumberCols() > 0:
            self.food_list.DeleteCols(0, self.food_list.GetNumberCols())

        # Add the required number of columns
        self.food_list.AppendCols(5)

        # Set column labels
        column_labels = self.food_data.columns[:5].tolist()
        for col, label in enumerate(column_labels):
            self.food_list.SetColLabelValue(col, label)

        # Set minimum size for the grid
        self.food_list.SetMinSize((600, 400))

        # Enable scrolling
        self.food_list.EnableScrolling(True, True)

        # Enable auto-sizing of rows and columns
        self.food_list.AutoSizeColumns()
        self.food_list.AutoSizeRows()

    def adjust_layout(self):
        # Get the main sizer
        main_sizer = self.GetSizer()

        # Find the sizer item containing the grid and set it to expand
        for item in main_sizer.GetChildren():
            if item.GetWindow() == self.food_list:
                item.SetProportion(1)
                item.SetFlag(wx.EXPAND | wx.ALL)
                break

        # Force the dialog to adjust its layout
        self.Layout()

    def on_search(self, event):
        query = self.search_input.GetValue().lower()
        # Use the first column (assumed to be the food name) for searching
        results = self.food_data[self.food_data.iloc[:, 0].str.lower().str.contains(query)]
        self.display_results(results)

    def display_results(self, results):
        self.food_list.ClearGrid()
        if self.food_list.GetNumberRows() > 0:
            self.food_list.DeleteRows(0, self.food_list.GetNumberRows())

        self.food_list.AppendRows(len(results))

        for row_idx, (_, row) in enumerate(results.iterrows()):
            for col_idx in range(5):
                self.food_list.SetCellValue(row_idx, col_idx, str(row.iloc[col_idx]))

        # Adjust column widths
        self.food_list.AutoSizeColumns()

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

    def get_selected_food(self):
        return self.selected_food


# This allows the file to be run standalone for testing
if __name__ == '__main__':
    app = wx.App(False)
    dialog = FoodSearchDialogLogic(None)
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        selected_food = dialog.get_selected_food()
        print("Selected food:", selected_food)
    dialog.Destroy()
    app.MainLoop()