# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
| **Tested Functions**                                                                   | **Test Functions**                               |
|----------------------------------------------------------------------------------------|--------------------------------------------------|
| 1. FoodItem Class                                                                      |                                                  |
| __init__(self, name, calories, protein, carbohydrates, fats, vitamins, minerals)       | test_food_item_initialization()                  |
| get_nutrient_value(self, nutrient)                                                     | test_get_nutrient_value()                        |
| 2. NutritionalDatabase Class                                                           |                                                  |
| __init__(self)                                                                         | test_nutritional_database_initialization()       |
| load_data(self, file_path)                                                             | test_load_data()                                 |
| search_food(self, query)                                                               | test_search_food()                               |
| apply_filters(self, filters)                                                           | test_apply_filters()                             |
| 3. NutritionChart Class                                                                |                                                  |
| __init__(self, chart_type, data)	                                                     | test_nutrition_chart_initialization()            |
| render(self)	                                                                         | test_render_bar_chart()                          |  
|                                                                                        | test_render_pie_chart()                          |
|                                                                                        | test_render_unsupported_chart()                  |
| 4. ComparisonResult Class                                                              |                                                  |
| __init__(self, food_items)	                                                           | test_comparison_result_initialization()          |
| get_comparison_data(self, nutrient)	                                                   | test_get_comparison_data()                       |
| 5. MealPlan Class                                                                      |                                                  |
| __init__(self)	                                                                       | test_meal_plan_initialization()                  |
| add_food_to_meal(self, day, meal, food_item)                                           | test_add_food_to_meal()                          |
| calculate_daily_summary(self, day)	                                                   | test_calculate_daily_summary()                   |
| get_weekly_overview(self)                                                              | test_get_weekly_overview()                       |
|
---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - test_food_item_initialization()
  - test_get_nutrient_value()
- **Tested Function/Module**
  - __init__(self, name, calories, protein, carbohydrates, fats, vitamins, minerals)
  - get_nutrient_value(self, nutrient) 
- **Description**
  - The FoodItem class is designed to represent a single food item with all its nutritional information. It includes attributes such as name, calories, protein, carbohydrates, fats, vitamins, and minerals. The __init__ method initializes these attributes, while the get_nutrient_value method retrieves the value of a specified nutrient.
    
- **1) Valid Input and Expected Output**
- Purpose: To verify that the __init__ method correctly initializes the attributes of the FoodItem class.

| **Valid Input**                 | **Expected Output**            |
|---------------------------------|--------------------------------|
| `name = "Apple"                 | name == "Apple"                |
| calories = 95                   | calories == 95                 |
| protein = 0.5                   | protein == 0.5                 |
| carbohydrates = 25              | carbohydrates == 25            |
| fats = 0.3                      | fats == 0.3                    |
| vitamins = {"Vitamin C": 8.4}   | vitamins == {"Vitamin C": 8.4} |
| minerals = {"Potassium": 195}   | minerals == {"Potassium": 195} |
| `...`                                                            |

- **1) Code for the Test Function**
```python
def test_food_item_initialization():
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    assert apple.name == "Apple"
    assert apple.calories == 95
    assert apple.protein == 0.5
    assert apple.carbohydrates == 25
    assert apple.fats == 0.3
    assert apple.vitamins == {"Vitamin C": 8.4}
    assert apple.minerals == {"Potassium": 195}
```
- **2) Invalid Input and Expected Output**
- Purpose: To verify that the get_nutrient_value method correctly retrieves the value of a specified nutrient.
  
| **Invalid Input**             | **Expected Output**                      |
|-------------------------------|------------------------------------------|
| nutrient = "calories"         | get_nutrient_value("calories") == 95     |
| nutrient = "protein"          | get_nutrient_value("protein") == 0.5     |
| nutrient = "nonexistent"      | get_nutrient_value("nonexistent") == None|
| `...`                                                                    |

- **2) Code for the Test Function**
```python
def test_get_nutrient_value():
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    assert apple.get_nutrient_value("calories") == 95
    assert apple.get_nutrient_value("protein") == 0.5
    assert apple.get_nutrient_value("nonexistent") is None
```
### Test Case 2:
- **Test Function/Module**
- test_nutritional_database_initialization()       
- test_load_data()                                 
- test_search_food()                               
- test_apply_filters()                         

- **Tested Function/Module**
  -  __init__(self) 
  - load_data(self, file_path)
  - search_food(self, query)
  - apply_filters(self, filters)

- **Description**
The NutritionalDatabase class manages a database of food items. It includes methods for initializing the database, loading data from a file, searching for food items, and applying filters to the food items.

- **1) Valid Input and Expected Output**  
- Purpose: To verify that the __init__ method correctly initializes the NutritionalDatabase class.
| **Valid Input**   | **Expected Output** |
|-------------------|---------------------|
|  None             |food_items == []     |
|  `...`                                  |

- **1) Code for the Test Function**
def test_nutritional_database_initialization():
    db = NutritionalDatabase()
    assert db.food_items == []

- **2) Invalid Input and Expected Output**
- Purpose: To verify that the load_data method correctly loads food items from a file.
| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| file_path = 'test_data.csv'   | len(food_items) > 0 |
              
- **2) Code for the Test Function**
def test_load_data():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    assert len(db.food_items) > 0

- **3) Invalid Input and Expected Output**
- Purpose: To verify that the search_food method correctly searches for food items by name.
| **Invalid Input**  | **Expected Output** |
|--------------------|---------------------|
|  query = 'apple'   | len(results) > 0    |


- **3) Code for the Test Function**
def test_search_food():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    results = db.search_food('apple')
    assert len(results) > 0

- **4) Invalid Input and Expected Output**
- Purpose: To verify that the apply_filters method correctly filters food items based on nutritional values.
| **Invalid Input**             | **Expected Output**                          |
|-------------------------------|----------------------------------------------|
|  filters = {'calories': 100}  | all(food.calories <= 100 for food in results)|
|                                 `...`                                        |

- **4) Code for the Test Function**

def test_apply_filters():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    filters = {'calories': 100}
    results = db.apply_filters(filters)
    assert all(food.calories <= 100 for food in results)

### Test Case 3:
- **Test Function/Module**
  - test_nutrition_chart_initialization()  
  - test_render_bar_chart()                          
  - test_render_pie_chart()                    
  - test_render_unsupported_chart()    
- **Tested Function/Module**
  - __init__(self, chart_type, data)
  - render(self)	 
- **Description**
  - The NutritionChart class is designed to visualize nutritional data. It includes attributes such as chart_type and data. The __init__ method initializes these attributes, while the render method generates the appropriate chart based on the chart_type.
    
- **1) Valid Input and Expected Output**  
- Purpose: To verify that the __init__ method correctly initializes the attributes of the NutritionChart class.
| **Valid Input**                        | **Expected Output**                     |
|----------------------------------------|-----------------------------------------|
| chart_type = 'bar'                     | chart_type == 'bar'                     |
| data = {'Calories': 95, 'Protein': 0.5}| data == {'Calories': 95, 'Protein': 0.5}|
|                                                              `...`               |

- **1) Code for the Test Function**
def test_nutrition_chart_initialization():
    data = {'Calories': 95, 'Protein': 0.5}
    chart = NutritionChart('bar', data)
    assert chart.chart_type == 'bar'
    assert chart.data == data

- **2) Invalid Input and Expected Output**
- Purpose: To verify that the render method correctly generates a bar chart.
| **Invalid Input**                      | **Expected Output**       |
|----------------------------------------|---------------------------|
| chart_type = 'bar'                     | A bar chart is displayed  |
| data = {'Calories': 95, 'Protein': 0.5}| without errors            |
| `...`                                                              |

- **2) Code for the Test Function**

def test_render_bar_chart():
    data = {'Calories': 95, 'Protein': 0.5}
    chart = NutritionChart('bar', data)
    chart.render()  # This should display a bar chart without errors

- **3) Invalid Input and Expected Output**
- Purpose: To verify that the render method handles unsupported chart types correctly.
| **Invalid Input**                       | **Expected Output**    |
|-----------------------------------------|------------------------|
| chart_type = 'unsupported'              | A message “Unsupported |
| data = {'Calories': 95, 'Protein': 0.5} | chart type” is printed.| 
|                      `...`                                       |

- **3) Code for the Test Function**
def test_render_unsupported_chart():
    data = {'Calories': 95, 'Protein': 0.5}
    chart = NutritionChart('unsupported', data)
    chart.render()  # This should print "Unsupported chart type"

- **4) Invalid Input and Expected Output**
- Purpose: To verify that the render method correctly generates a pie chart.
  
| **Invalid Input**                      | **Expected Output**                          |
|----------------------------------------|----------------------------------------------|
| chart_type = 'pie'                     | A pie chart is displayed without errors.     |
| data = {'Calories': 95, 'Protein': 0.5}|                                              |
|                                 `...`                                                 |

- **4) Code for the Test Function**

def test_render_pie_chart():
    data = {'Calories': 95, 'Protein': 0.5}
    chart = NutritionChart('pie', data)
    chart.render()  # This should display a pie chart without errors

### Test Case 4:
- **Test Function/Module**
  - test_comparison_result_initialization() 
  -  test_get_comparison_data()  
- **Tested Function/Module**
  - __init__(self, food_items)
  - get_comparison_data(self, nutrient)	 
- **Description**
  - The ComparisonResult class is designed to represent the result of a food comparison. It includes attributes such as food_items (a list of compared FoodItem objects) and comparison_data (nutritional data for comparison). The __init__ method initializes these attributes, while the get_comparison_data method retrieves the comparison data for a specified nutrient.

- **1) Valid Input and Expected Output**  
- The ComparisonResult class is designed to represent the result of a food comparison. It includes attributes such as food_items (a list of compared FoodItem objects) and comparison_data (nutritional data for comparison). The __init__ method initializes these attributes, while the get_comparison_data method retrieves the comparison data for a specified nutrient.
| **Valid Input**                                                                | **Expected Output**                                                   |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| food_items = [FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4},          |food_items == [FoodItem("Apple", 95, 0.5, 25, 0.3,                     |
| comparison_data is correctly generated for each nutrient.                      |{"Vitamin C": 8.4}, {"Potassium": 195}), FoodItem                      |
| {"Potassium": 195}), FoodItem("Banana", 105, 1.3, 27, 0.3, {"Vitamin C": 10.3},|("Banana", 105, 1.3, 27, 0.3,{"Vitamin C": 10.3}, {"Potassium": 422})] |
|{"Potassium": 422})]                                                            |                                                                       |
|                                                                                                                                    `...`               |

- **1) Code for the Test Function**
```python
def test_comparison_result_initialization():
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    banana = FoodItem("Banana", 105, 1.3, 27, 0.3, {"Vitamin C": 10.3}, {"Potassium": 422})
    comparison = ComparisonResult([apple, banana])
    assert comparison.food_items == [apple, banana]
    assert 'calories' in comparison.comparison_data
    assert comparison.comparison_data['calories'] == {'Apple': 95, 'Banana': 105}
```
- **2) Invalid Input and Expected Output**
- Purpose: To verify that the get_comparison_data method correctly retrieves the comparison data for a specified nutrient.
| **Invalid Input**             | **Expected Output**                                               |
|-------------------------------|-------------------------------------------------------------------|
| nutrient = 'calories'         | get_comparison_data('calories') == {'Apple': 95, 'Banana': 105}`  |
| nutrient = 'protein'          | get_comparison_data('protein') == {'Apple': 0.5, 'Banana': 1.3}   |
| nutrient = 'nonexistent'      | get_comparison_data('nonexistent') == {}                          |
| `...`                                                                                             |

- **2) Code for the Test Function**

def test_get_comparison_data():
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    banana = FoodItem("Banana", 105, 1.3, 27, 0.3, {"Vitamin C": 10.3}, {"Potassium": 422})
    comparison = ComparisonResult([apple, banana])
    assert comparison.get_comparison_data('calories') == {'Apple': 95, 'Banana': 105}
    assert comparison.get_comparison_data('protein') == {'Apple': 0.5, 'Banana': 1.3}
    assert comparison.get_comparison_data('nonexistent') == {}



### Test Case 5:
- **Test Function/Module**
  - test_meal_plan_initialization() 
  - test_add_food_to_meal()                 
  - test_calculate_daily_summary() 
  - test_get_weekly_overview() 
- **Tested Function/Module**
  - __init__(self)
  - add_food_to_meal(self, day, meal, food_item)
  - calculate_daily_summary(self, day)
  - get_weekly_overview(self) 
- **Description**
  - The MealPlan class represents a weekly meal plan with daily breakdowns. It includes attributes such as weekly_plan (structured meal data) and daily_summaries (nutritional summaries). The __init__ method initializes these attributes, while the add_food_to_meal method adds food items to specific meals on specific days. The calculate_daily_summary method calculates the nutritional summary for a day, and the get_weekly_overview method provides a summary of the nutritional data for the entire week.

- **1) Valid Input and Expected Output**  
- Purpose: To verify that the __init__ method correctly initializes the attributes of the MealPlan class.
| **Valid Input**  | **Expected Output**                                                     |
|------------------|-------------------------------------------------------------------------|
| None             | weekly_plan is initialized with empty lists for each meal on each day.  |
|                  | daily_summaries is initialized with empty dictionaries for each day.    |
|                                                                        `...`               |

- **1) Code for the Test Function**

def test_meal_plan_initialization():
    meal_plan = MealPlan()
    assert 'Monday' in meal_plan.weekly_plan
    assert 'breakfast' in meal_plan.weekly_plan['Monday']
    assert meal_plan.weekly_plan['Monday']['breakfast'] == []
    assert meal_plan.daily_summaries['Monday'] == {}

- **2) Invalid Input and Expected Output**
- Purpose: To verify that the add_food_to_meal method correctly adds food items to specific meals on specific days.
| **Invalid Input**                                 | **Expected Output**   |
|---------------------------------------------------|-----------------------|
| day = 'Monday'                                    |The food item is added |
| meal = 'breakfast'                                | to the specified meal |
| food_item = FoodItem("Apple", 95, 0.5, 25, 0.3,   | on the specified day. |
| {"Vitamin C": 8.4}, {"Potassium": 195})           |                       |
|                                                                           |
- **2) Code for the Test Function**
```python
def test_add_food_to_meal():
    meal_plan = MealPlan()
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    meal_plan.add_food_to_meal('Monday', 'breakfast', apple)
    assert meal_plan.weekly_plan['Monday']['breakfast'] == [apple]
```
- **3) Invalid Input and Expected Output**
- Purpose: To verify that the calculate_daily_summary method correctly calculates the nutritional summary for a day.
| **Invalid Input**                                 | **Expected Output**   |
|---------------------------------------------------|-----------------------|
| day = 'Monday'                                    |The daily summary for  |
| meal = 'breakfast'                                | the specified day is  |
| food_item = FoodItem("Apple", 95, 0.5, 25, 0.3,   | correctly calculated. |
| {"Vitamin C": 8.4}, {"Potassium": 195})           |                       |
|                                                                           |
- **3) Code for the Test Function**
```python
def test_calculate_daily_summary():
    meal_plan = MealPlan()
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    meal_plan.add_food_to_meal('Monday', 'breakfast', apple)
    summary = meal_plan.daily_summaries['Monday']
    assert summary['calories'] == 95
    assert summary['protein'] == 0.5
    assert summary['carbohydrates'] == 25
    assert summary['fats'] == 0.3

```
- **4) Invalid Input and Expected Output**
- Purpose: To verify that the get_weekly_overview method correctly provides a summary of the nutritional data for the entire week.
| **Invalid Input**                                 | **Expected Output**         |
|---------------------------------------------------|-----------------------------|
| food_item = FoodItem("Apple", 95, 0.5, 25, 0.3,   |The weekly overview correctly|
| {"Vitamin C": 8.4}, {"Potassium": 195})           |summarizes the nutritional   |
|                                                   | data for each day.          |
|                                                                                 |
- **) Code for the Test Function**
```python
def test_get_weekly_overview():
    meal_plan = MealPlan()
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3, {"Vitamin C": 8.4}, {"Potassium": 195})
    meal_plan.add_food_to_meal('Monday', 'breakfast', apple)
    overview = meal_plan.get_weekly_overview()
    assert 'Monday' in overview
    assert overview['Monday']['calories'] == 95
    assert overview['Monday']['protein'] == 0.5
    assert overview['Monday']['carbohydrates'] == 25
    assert overview['Monday']['fats'] == 0.3
```
## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
