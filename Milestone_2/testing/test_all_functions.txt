import pytest
from all_functions import (
    load_food_dataset, create_empty_meal_plan, generate_meal_plan_string,
    add_food, remove_food, change_food, clear_meal_plan, clear_meal_plan_for_day
)

# Test for load_food_dataset
def test_load_food_dataset():
    file_path = "Food_Nutrition_Dataset.csv"
    dataset = load_food_dataset(file_path)
    assert dataset is not None, "Dataset should load properly if the file exists."

    non_existing_file = "non_existing_file.csv"
    dataset = load_food_dataset(non_existing_file)
    assert dataset is None, "Function should return None for non-existent files."

# Test for create_empty_meal_plan
def test_create_empty_meal_plan():
    meal_plan = create_empty_meal_plan()
    assert len(meal_plan) == 7, "Meal plan should have 7 days."
    for day in meal_plan:
        assert set(meal_plan[day].keys()) == {'Breakfast', 'Lunch', 'Dinner', 'Snack'}, "Each day should have 4 meals."

# Test for generate_meal_plan_string
def test_generate_meal_plan_string():
    sample_meal_plan = {
        'Monday': {
            'Breakfast': [{'name': 'Egg'}],
            'Lunch': [{'name': 'Salad'}],
            'Dinner': [{'name': 'Steak'}],
            'Snack': [{'name': 'Apple'}]
        },
        'Tuesday': {
            'Breakfast': [{'name': 'Pancake'}],
            'Lunch': [],
            'Dinner': [],
            'Snack': []
        }
    }
    result = generate_meal_plan_string(sample_meal_plan)
    expected = (
        "Monday:\n"
        "  Breakfast: Egg\n"
        "  Lunch: Salad\n"
        "  Dinner: Steak\n"
        "  Snack: Apple\n"
        "Tuesday:\n"
        "  Breakfast: Pancake\n"
        "  Lunch: \n"
        "  Dinner: \n"
        "  Snack: \n"
    )
    assert result == expected, "Generated meal plan string should match expected format."

# New Test: Test for an empty meal plan
def test_generate_meal_plan_string_empty():
    empty_meal_plan = create_empty_meal_plan()
    result = generate_meal_plan_string(empty_meal_plan)
    expected = (
        "Monday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Tuesday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Wednesday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Thursday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Friday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Saturday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
        "Sunday:\n  Breakfast: \n  Lunch: \n  Dinner: \n  Snack: \n"
    )
    assert result == expected, "Empty meal plan should generate an empty string for each meal."

# Test for add_food
def test_add_food():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    assert meal_plan['Monday']['Breakfast'] == [food_item], "Food item should be added to Monday breakfast."

# Test for remove_food
def test_remove_food():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    remove_food(meal_plan, 'Monday', 'Breakfast', 'Oatmeal')
    assert meal_plan['Monday']['Breakfast'] == [], "Food item should be removed from Monday breakfast."

# New Test: Test removing non-existent food
def test_remove_non_existent_food():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    remove_food(meal_plan, 'Monday', 'Breakfast', 'Pancakes')  # Trying to remove non-existent food
    assert meal_plan['Monday']['Breakfast'] == [food_item], "Removing non-existent food should not change the meal plan."

# Test for change_food
def test_change_food():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    new_food_item = {'name': 'Pancakes'}
    change_food(meal_plan, 'Monday', 'Breakfast', 'Oatmeal', new_food_item)
    assert meal_plan['Monday']['Breakfast'][0]['name'] == 'Pancakes', "Oatmeal should be replaced with Pancakes."

# New Test: Test changing non-existent food
def test_change_non_existent_food():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    change_food(meal_plan, 'Monday', 'Breakfast', 'Pancakes', {'name': 'Waffles'})  # Trying to change non-existent food
    assert meal_plan['Monday']['Breakfast'] == [food_item], "Changing non-existent food should not affect the meal plan."

# New Test: Test changing in an empty meal
def test_change_food_empty_meal():
    meal_plan = create_empty_meal_plan()
    change_food(meal_plan, 'Monday', 'Breakfast', 'Oatmeal', {'name': 'Pancakes'})  # Change in empty meal
    assert meal_plan['Monday']['Breakfast'] == [], "Changing in an empty meal should not add any food."

# Test for clear_meal_plan
def test_clear_meal_plan():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    cleared_plan = clear_meal_plan()
    assert all(len(cleared_plan[day][meal]) == 0 for day in cleared_plan for meal in cleared_plan[day]), "Meal plan should be cleared."

# Test for clear_meal_plan_for_day
def test_clear_meal_plan_for_day():
    meal_plan = create_empty_meal_plan()
    food_item = {'name': 'Oatmeal'}
    add_food(meal_plan, 'Monday', 'Breakfast', food_item)
    clear_meal_plan_for_day(meal_plan, 'Monday')
    assert all(len(meal_plan['Monday'][meal]) == 0 for meal in meal_plan['Monday']), "Monday's meals should be cleared."

# New Test: Test clearing an already empty day
def test_clear_empty_day():
    meal_plan = create_empty_meal_plan()
    clear_meal_plan_for_day(meal_plan, 'Monday')  # Clear an already empty day
    assert all(len(meal_plan['Monday'][meal]) == 0 for meal in meal_plan['Monday']), "Clearing an empty day should not cause errors."
