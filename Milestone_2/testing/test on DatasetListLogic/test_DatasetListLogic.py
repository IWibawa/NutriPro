import pytest
import wx
import pandas as pd
import matplotlib.pyplot as plt

from DatasetListLogic import DatasetListLogic


@pytest.fixture(scope='module')
def setup_app():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Test Frame")
    meal_plan_manager = None
    dataset_logic = DatasetListLogic(frame, meal_plan_manager)

    yield dataset_logic

    app.Destroy()  


def test_initialize_grid_controls(setup_app):
    app = setup_app
    app.initialize_grid_controls()

    assert app.food_list.GetNumberCols() == len(app.food_data.columns)
    assert app.comparison_list.GetNumberCols() == 5


def test_display_results(setup_app):
    app = setup_app
    mock_data = pd.DataFrame({
        'Name': ['Apple', 'Banana'],
        'Calories': [52, 89],
        'Protein': [0.3, 1.1],
        'Carbs': [14, 22.8],
        'Fat': [0.2, 0.3]
    })

    app.display_results(mock_data)

    assert app.food_list.GetCellValue(0, 0) == 'Apple'
    assert app.food_list.GetCellValue(1, 0) == 'Banana'


def test_on_search(setup_app, mocker):
    app = setup_app
    mocker.patch.object(app, 'display_results')

    app.search_input.SetValue('Apple')
    app.on_search(None)

    app.display_results.assert_called_once()


def test_on_apply_filters(setup_app):
    app = setup_app
    app.food_data = pd.DataFrame({
        'Name': ['Chicken', 'Tofu', 'Pasta'],
        'Protein': [30, 8, 5],
        'Carbohydrate': [0, 2, 25],
        'Fat': [5, 3, 1]
    })

    app.filter_protein.SetValue(True)
    app.on_apply_filters(None)

    assert app.food_list.GetCellValue(0, 0) == 'Chicken'


def test_on_add_to_comparison(setup_app):
    app = setup_app
    app.food_data = pd.DataFrame({
        'Name': ['Chicken'],
        'Calories': [200],
        'Protein': [30],
        'Carbs': [0],
        'Fat': [5]
    })
    app.display_results(app.food_data)

    app.food_list.SetGridCursor(0, 0)
    wx.CallAfter(app.on_add_to_comparison, None)
    wx.Yield()

    assert app.comparison_list.GetCellValue(0, 0) == 'Chicken'


def test_get_non_empty_rows(setup_app):
    app = setup_app
    app.comparison_list.AppendRows(3)
    app.comparison_list.SetCellValue(0, 0, 'Chicken')
    app.comparison_list.SetCellValue(1, 0, '')
    app.comparison_list.SetCellValue(2, 0, 'Apple')

    non_empty_rows = app.get_non_empty_rows()

    assert non_empty_rows == [0, 2]


def test_on_clear_comparison(setup_app):
    app = setup_app

    app.comparison_list.AppendRows(2)
    app.comparison_list.SetCellValue(0, 0, 'Chicken')
    app.comparison_list.SetCellValue(1, 0, 'Apple')

    wx.CallAfter(app.on_clear_comparison, None)
    wx.Yield()

    assert app.comparison_list.GetNumberRows() == 0


def test_on_generate_chart(setup_app, mocker):
    app = setup_app
    app.comparison_list.AppendRows(2)
    app.comparison_list.SetCellValue(0, 0, 'Chicken')
    app.comparison_list.SetCellValue(0, 1, '200')
    app.comparison_list.SetCellValue(0, 2, '30')
    app.comparison_list.SetCellValue(0, 3, '0')
    app.comparison_list.SetCellValue(0, 4, '5')

    mocker.patch('matplotlib.pyplot.show')

    app.on_generate_chart(None)

    plt.show.assert_called_once()


def test_get_food_from_grid(setup_app):
    app = setup_app
    app.food_data = pd.DataFrame({
        'Name': ['Chicken'],
        'Calories': [200],
        'Protein': [30],
        'Carbs': [0],
        'Fat': [5]
    })
    app.display_results(app.food_data)

    app.food_list.SetCellValue(0, 0, 'Chicken')
    app.food_list.SetCellValue(0, 1, '200')
    app.food_list.SetCellValue(0, 8, '30')
    app.food_list.SetCellValue(0, 6, '0')
    app.food_list.SetCellValue(0, 2, '5')

    food = app.get_food_from_grid(0)

    assert food['name'] == 'Chicken'
    assert food['calories'] == 200
    assert food['protein'] == 30
    assert food['carbs'] == 0
    assert food['fat'] == 5


def test_on_add_to_meal_plan(setup_app, mocker):
    app = setup_app

    mock_meal_plan_manager = mocker.Mock()
    app.meal_plan_manager = mock_meal_plan_manager

    app.food_data = pd.DataFrame({
        'Name': ['Chicken'],
        'Calories': [200],
        'Protein': [30],
        'Carbs': [0],
        'Fat': [5]
    })
    app.display_results(app.food_data)

    app.food_list.SetGridCursor(0, 0)
    wx.CallAfter(app.on_add_to_meal_plan, None)
    wx.Yield()

    mock_meal_plan_manager.add_food.assert_called_once()


def test_get_selected_meal(setup_app):
    app = setup_app
    app.meal_plan_breakfast.SetValue(True)
    assert app.get_selected_meal() == "Breakfast"

    app.meal_plan_lunch.SetValue(True)
    assert app.get_selected_meal() == "Lunch"

    app.meal_plan_dinner.SetValue(True)
    assert app.get_selected_meal() == "Dinner"

    app.meal_plan_snack.SetValue(True)
    assert app.get_selected_meal() == "Snack"


def test_on_go_to_meal_plan(setup_app, mocker):
    app = setup_app

    mock_app = mocker.patch('wx.GetApp')
    mock_app().show_meal_plan = mocker.Mock()

    wx.CallAfter(app.on_go_to_meal_plan, None)
    wx.Yield()

    mock_app().show_meal_plan.assert_called_once()


def test_on_back_to_main_menu(setup_app, mocker):
    app = setup_app
    mock_main_frame = mocker.Mock()
    wx.App.main_frame = mock_main_frame

    wx.CallAfter(app.on_back_to_main_menu, None)
    wx.Yield()

    mock_main_frame.Show.assert_called_once()
