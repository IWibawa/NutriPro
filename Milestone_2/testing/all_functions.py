import pandas as pd

#  Load CSV File
def load_food_dataset(file_path):
    try:
        food_dataset = pd.read_csv(file_path)
        return food_dataset
    except FileNotFoundError:
        return None

#  Create a new empty table (meal plan table structure)
def create_empty_meal_plan():
    return {
        day: {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []}
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    }

#  Generate a meal plan string
def generate_meal_plan_string(meal_plan):
    meal_plan_str = ""
    for day, meals in meal_plan.items():
        meal_plan_str += f"{day}:\n"
        for meal, foods in meals.items():
            meal_plan_str += f"  {meal}: {', '.join([food['name'] for food in foods])}\n"
    return meal_plan_str

#  Add food to the meal plan
def add_food(meal_plan, day, meal, food):
    meal_plan[day][meal].append(food)

#  Remove food from the meal plan
def remove_food(meal_plan, day, meal, food_name):
    meal_plan[day][meal] = [food for food in meal_plan[day][meal] if food['name'] != food_name]

#  Change food in the meal plan
def change_food(meal_plan, day, meal, old_food_name, new_food):
    for i, food in enumerate(meal_plan[day][meal]):
        if food['name'] == old_food_name:
            meal_plan[day][meal][i] = new_food
            break

#  Clear the entire meal plan
def clear_meal_plan():
    return create_empty_meal_plan()

#  Clear meal plan for a specific day
def clear_meal_plan_for_day(meal_plan, day):
    meal_plan[day] = {'Breakfast': [], 'Lunch': [], 'Dinner': [], 'Snack': []}

