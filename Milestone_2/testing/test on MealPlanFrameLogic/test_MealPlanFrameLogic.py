import pytest
import wx
import pandas as pd
from unittest import mock
from MealPlanFrameLogic import MealPlanFrameLogic

@pytest.fixture(scope='module')
def setup_app():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Test Frame")
    sizer = wx.BoxSizer(wx.VERTICAL)
    frame.SetSizer(sizer)

    meal_plan_manager = mock.Mock()
    meal_plan_manager.get_meal_plan.return_value = {
        'Monday': {'Breakfast': [{'name': 'Oatmeal', 'calories': 150, 'protein': 5, 'carbs': 27, 'fat': 3}]},
        'Tuesday': {'Breakfast': [{'name': 'Pancakes', 'calories': 200, 'protein': 6, 'carbs': 35, 'fat': 8}]},
        'Wednesday': {'Breakfast': [{'name': 'Eggs', 'calories': 140, 'protein': 12, 'carbs': 1, 'fat': 10}]},
        'Thursday': {'Breakfast': [{'name': 'Fruit Salad', 'calories': 120, 'protein': 2, 'carbs': 30, 'fat': 0}]},
        'Friday': {'Breakfast': [{'name': 'Yogurt', 'calories': 100, 'protein': 8, 'carbs': 15, 'fat': 3}]},
        'Saturday': {'Breakfast': [{'name': 'Smoothie', 'calories': 180, 'protein': 5, 'carbs': 35, 'fat': 2}]},
        'Sunday': {'Breakfast': [{'name': 'Toast', 'calories': 80, 'protein': 3, 'carbs': 15, 'fat': 1}]},
    }

    meal_plan_logic = MealPlanFrameLogic(frame, meal_plan_manager)

    yield meal_plan_logic

    app.Destroy()

def test_initialize_grid(setup_app):
    app = setup_app
    app.initialize_grid()
    assert app.meal_plan_list.GetNumberCols() == 7
    assert app.meal_plan_list.GetColLabelValue(0) == "Day"

def test_on_day_selected(setup_app, mocker):
    app = setup_app
    mocker.patch.object(app, 'update_meal_plan_display')
    app.day_choice.SetSelection(1)
    app.on_day_selected(None)
    app.update_meal_plan_display.assert_called_once()

def test_toggle_view(setup_app):
    app = setup_app
    assert app.current_view == 'daily'
    app.toggle_view(None)
    assert app.current_view == 'weekly'
    app.toggle_view(None)
    assert app.current_view == 'daily'

def test_update_meal_plan_display(setup_app):
    app = setup_app
    app.update_meal_plan_display()
    assert app.meal_plan_list.GetNumberRows() > 0

def test_update_nutrient_summary(setup_app):
    app = setup_app
    app.update_nutrient_summary()
    assert app.nutrient_summary.GetLabel()

def test_on_generate_random_meal_plan(setup_app):
    app = setup_app
    app.on_generate_random_meal_plan(None)
    assert app.meal_plan_manager.clear_meal_plan.called

def test_generate_balanced_meal(setup_app):
    app = setup_app
    selected_foods = app.generate_balanced_meal()
    assert isinstance(selected_foods, list)

def test_on_add_food(setup_app, mocker):
    app = setup_app
    mock_dialog = mocker.patch('FoodSearchDialogLogic.FoodSearchDialogLogic', autospec=True)
    dialog_instance = mock_dialog.return_value
    dialog_instance.get_selected_food.return_value = {'name': 'Chicken', 'calories': 200}

    app.on_add_food(None)
    assert app.meal_plan_manager.add_food.called

def test_on_remove_food(setup_app):
    app = setup_app
    app.meal_plan_list.AppendRows(1)
    app.meal_plan_list.SetCellValue(0, 0, 'Monday')
    app.meal_plan_list.SetCellValue(0, 1, 'Breakfast')
    app.meal_plan_list.SetCellValue(0, 2, 'Chicken')

    app.on_remove_food(None)
    assert app.meal_plan_manager.remove_food.called

def test_on_clear_meal_plan(setup_app):
    app = setup_app
    app.on_clear_meal_plan(None)
    assert app.meal_plan_manager.clear_meal_plan.called

def test_on_go_to_data_list(setup_app, mocker):
    app = setup_app
    mock_app = mocker.patch('wx.GetApp')
    mock_app().show_dataset_list = mocker.Mock()

    app.on_go_to_data_list(None)
    mock_app().show_dataset_list.assert_called_once()

def test_on_back_to_main_menu(setup_app, mocker):
    app = setup_app
    mock_app = mocker.patch('wx.GetApp')
    mock_app().main_frame.Show = mocker.Mock()

    app.on_back_to_main_menu(None)
    mock_app().main_frame.Show.assert_called_once()
