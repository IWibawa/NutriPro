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
```
- **2) Invalid Input and Expected Output**
- Purpose: To verify that the load_data method correctly loads food items from a file.
| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| file_path = 'test_data.csv'   | len(food_items) > 0 |
|                                 `...`               |

- **2) Code for the Test Function**
```python
def test_load_data():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    assert len(db.food_items) > 0
```
- **3) Invalid Input and Expected Output**
- Purpose: To verify that the search_food method correctly searches for food items by name.
| **Invalid Input**  | **Expected Output** |
|--------------------|---------------------|
|  query = 'apple'   | len(results) > 0    |
|                      `...`               |

- **3) Code for the Test Function**
def test_search_food():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    results = db.search_food('apple')
    assert len(results) > 0
```
- *4) Invalid Input and Expected Output**
- Purpose: To verify that the apply_filters method correctly filters food items based on nutritional values.
| **Invalid Input**             | **Expected Output**                          |
|-------------------------------|----------------------------------------------|
|  filters = {'calories': 100}  | all(food.calories <= 100 for food in results)|
|                                 `...`                                        |

- **) Code for the Test Function**
```python
def test_apply_filters():
    db = NutritionalDatabase()
    db.load_data('test_data.csv')
    filters = {'calories': 100}
    results = db.apply_filters(filters)
    assert all(food.calories <= 100 for food in results)
```
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
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 4:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```


### Test Case 5:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:

add more test cases if necessary.

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
