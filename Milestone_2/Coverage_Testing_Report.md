# Coverage Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git](https://github.com/XXXX/XXXXX.git%5D(https://github.com/IWibawa))

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

You should perform statement coverage testing and branch coverage testing. For each type, provide a description and an analysis explaining how you evaluated the coverage.

## 1. **Test Summary**
list all tested functions related to the five required features, for example:

| **Tested Functions**                                                                                 |
|------------------------------------------------------------------------------------------------------|
|1. FoodItem Class                                                                                     |
| Tested Functions: __init__(self, name, calories, protein, carbohydrates, fats, vitamins, minerals)   |
|                   get_nutrient_value(self, nutrient)                                                 |
|                                                                                                      |
|2. NutritionalDatabase Class                                                                          |
| Tested Functions:  __init__(self)                                                                    |
|                    load_data(self, file_path)                                                        |
|                    search_food(self, query)                                                          |
|                    apply_filters(self, filters)                                                      |
|                                                                                                      |
| 3. NutritionChart Class                                                                              |
| Tested Functions: __init__(self, chart_type, data)                                                   |
|                    render(self)                                                                      |
|                                                                                                      |
| 4. ComparisonResult Class                                                                            |
| Tested Functions: __init__(self, food_items)                                                         |
|                   get_comparison_data(self, nutrient)                                                |
|                                                                                                      |
|5. MealPlan Class                                                                                     |
| Tested Functions; __init__(self)                                                                     |
|                   dd_food_to_meal(self, day, meal, food_item)                                        |
|                    calculate_daily_summary(self, day)                                                |
|                    get_weekly_overview(self)                                                         |
|------------------------------------------------------------------------------------------------------|

---

## 2. **Statement Coverage Test**

### 2.1 Description

To achieve 100% statement coverage in the test_all_functions.py file, I designed the test cases to ensure that every line of code in each function is executed at least once during the testing process. Here’s a detailed explanation of the approach:

1. Identify All Functions and Their Statements
    - List all the functions that need to be tested.
    - Break down each function into individual statements to ensure every line is covered.
2. Create Comprehensive Test Cases
    - For each function, create test cases that cover all possible execution paths, including edge cases and typical use cases.
3. Use Assertions to Verify Outcomes
    - Use assertions to check that the function outputs match the expected results.
    - Ensure that all branches (if-else conditions) and loops are executed.
4. Handle Exceptions and Errors
    - Include test cases that trigger exceptions or errors to ensure that error handling code is also covered.

Function 1: FoodItem Class __init__ Method
    Statements: Initialize attributes.
Function 2: get_nutrient_value Method
    Statements: Retrieve nutrient value using getattr.
Function 3: NutritionalDatabase Class load_data Method
    Statements: Open file, read data, create FoodItem instances, append to list.
Function 4: search_food Method
    Statements: Search for food items by name.
Function 5: NutritionChart Class render Method
    Statements: Check chart type, call appropriate rendering method.    
By systematically designing test cases to cover all possible execution paths, including normal operations, edge cases, and error handling, we can ensure that every statement in the code is executed at least once, achieving 100% statement coverage.

### 2.2 Testing Results
You can use the following command to run the statement coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![statement_coverage](./https://github.com/IWibawa/NutriPro/edit/main/Milestone_2/Coverage_Testing_Report.md)

## 3. **Branch Coverage Test**

### 3.1 Description

To achieve 100% branch coverage in the test_all_functions.py file, I designed the test cases to ensure that every possible branch (i.e., each possible path through the code, including all if-else conditions) is executed at least once. Here’s a detailed explanation of the approach:

1. Identify All Branches
    - List all the conditional statements (if-else) in each function.
    - Ensure that each condition and its corresponding branches are covered.
2. Create Comprehensive Test Cases
    - For each function, create test cases that cover all possible branches, including edge cases and typical use cases.
3. Use Assertions to Verify Outcomes
    - Use assertions to check that the function outputs match the expected results for each branch.
4. Handle Exceptions and Errors
    - Include test cases that trigger exceptions or errors to ensure that error handling code is also covered.
  
Function 1: Designing Test Cases for FoodItem Class (get_nutrient_value Method)
    Branches: Check if the nutrient exists in the attributes.
Function 2: Designing Test Cases for NutritionalDatabase Class (load_data Method)
    Branches: File opening, reading data, creating FoodItem instances.
Function 3: search_food Method
    Branches: Check if the query matches any food item names.
Function 4: Designing Test Cases for NutritionChart Class render Method
    Branches: Check chart type and call appropriate rendering method.
Function 5: Designing Test Cases for ComparisonResult Class (get_comparison_data Method)
    Branches: Generate comparison data for each nutrient.
    
### 3.2 Testing Results
You can use the following command to run the branch coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-branch --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![alt text](./https://github.com/IWibawa/NutriPro/blob/main/Milestone_2/testing/test%20on%20main/Branch_Test_Results.png?raw=true)
