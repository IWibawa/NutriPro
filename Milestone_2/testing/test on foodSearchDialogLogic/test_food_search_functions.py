import pytest
import wx
import pandas as pd
from FoodSearchDialogLogic import FoodSearchDialogLogic


# Create a fixture to manage wx.App
@pytest.fixture(scope="module")
def app():
    app = wx.App(False)
    yield app
    app.Destroy()


# Fixture for the dialog
@pytest.fixture
def food_search_dialog(app):
    dialog = FoodSearchDialogLogic(None)
    dialog.initialize_grid()  # Ensure grid is initialized in the fixture
    return dialog


def test_initialize_grid(food_search_dialog):
    food_search_dialog.initialize_grid()
    assert food_search_dialog.food_list.GetNumberCols() == 5
    assert food_search_dialog.food_list.GetColLabelValue(0).lower() == 'food'


def test_adjust_layout(food_search_dialog):
    food_search_dialog.adjust_layout()
    sizer = food_search_dialog.GetSizer()
    assert sizer is not None


def test_on_search(food_search_dialog, mocker):
    # Mocking the input value and display_results
    mocker.patch.object(food_search_dialog.search_input, 'GetValue', return_value='apple')
    mocker.patch.object(food_search_dialog, 'display_results')

    food_search_dialog.on_search(None)

    # Ensure display_results was called
    food_search_dialog.display_results.assert_called_once()


def test_display_results(food_search_dialog):
    # Sample data
    results = pd.DataFrame({
        'Food': ['Apple', 'Banana'],
        'Calories': [52, 96],
        'Protein': [0.3, 1.3],
        'Carbs': [14, 27],
        'Fat': [0.2, 0.3]
    })

    food_search_dialog.display_results(results)

    # Check if rows are populated
    assert food_search_dialog.food_list.GetNumberRows() == 2
    assert food_search_dialog.food_list.GetCellValue(0, 0) == 'Apple'
    assert food_search_dialog.food_list.GetCellValue(1, 0) == 'Banana'


def test_on_select_food(food_search_dialog, mocker):
    # Mocking grid selection
    mocker.patch.object(food_search_dialog.food_list, 'GetGridCursorRow', return_value=0)
    mocker.patch.object(food_search_dialog.food_list, 'GetCellValue', side_effect=['Apple', '52', '0.3', '14', '0.2'])

    food_search_dialog.on_select_food(None)

    # Validate the selected food details
    assert food_search_dialog.selected_food['name'] == 'Apple'
    assert food_search_dialog.selected_food['calories'] == 52.0
    assert food_search_dialog.selected_food['protein'] == 0.3
    assert food_search_dialog.selected_food['carbs'] == 14.0
    assert food_search_dialog.selected_food['fat'] == 0.2


def test_get_selected_food(food_search_dialog):
    # Set selected_food manually
    food_search_dialog.selected_food = {
        'name': 'Banana',
        'calories': 96.0,
        'protein': 1.3,
        'carbs': 27.0,
        'fat': 0.3
    }

    selected_food = food_search_dialog.get_selected_food()

    # Validate the selected food details
    assert selected_food['name'] == 'Banana'
    assert selected_food['calories'] == 96.0
    assert selected_food['protein'] == 1.3
    assert selected_food['carbs'] == 27.0
    assert selected_food['fat'] == 0.3
