# Executive Summary

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

You should use your software to prepare an executive summary as outlined below for the five required features.

## 1. [FoodItem]
### Description  
- **Type**: Class
- **Usage**: Represents a single food item with all its nutritional information
- **Key Attributes**: `name`, `calories`, `protein`, `carbohydrates`, `fats`, `vitamins`, `minerals`
- **Key Methods**: `get_nutrient_value(nutrient)`

**Interactions**:
- Serves as the fundamental unit of food information in the **NutritionalDatabase**
- Used in search, filter, and comparison functions
- Forms the basis of meal components in the **MealPlan** structure
  
### Steps
1. Define the Class: Create a class named FoodItem with the key attributes and methods.
2. Instantiate Food Items: Create instances of the FoodItem class for different foods.
3. Access Nutritional Information: Use the get_nutrient_value method to retrieve specific nutrient values.
4. Integrate with Nutritional Database: Use the FoodItem instances in your nutritional database for search, filter, and comparison functions.
5. Use in Meal Plan Structure: Incorporate FoodItem instances into meal plans.
6. Additional Steps:
- Expand Attributes: Add more attributes like serving size, fiber, sugar, etc.
- Enhance Methods: Include methods for updating nutrient values, calculating daily values, etc.
- User Interface: Develop a user interface to interact with the nutritional database and meal plans.
  
### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![1](https://github.com/IWibawa/NutriPro/blob/main/Diagrams/visual_design%20-%20main_screen.png?raw=true)


---

## 2. [NutritionalDatabase]
### Description  
- **Type**: Class
- **Usage**: Manages the entire database of food items
- **Key Attributes**: `food_items` (a list of **FoodItem** objects)
- **Key Methods**: `load_data(file_path)`, `search_food(query)`, `apply_filters(filters)`

**Interactions**:
- Acts as the central repository for all **FoodItem** instances
- Interfaces with the CSV file data source to populate its food items list
- Provides data access for search, filter, and meal planning functions
- 
### Steps
1. Define the Class: Create a class named NutritionalDatabase with the key attributes and methods.
2. Load Data from a CSV File: Use the load_data method to populate the food_items list from a CSV file.
3. Search for Food Items: Use the search_food method to find food items by name.
4. Apply Filters to Food Items: Use the apply_filters method to filter food items based on nutritional values.
5. Integrate with Other Features: Use the NutritionalDatabase class in conjunction with other features like meal planning.
6. Additional Steps:
- Expand Data Handling: Enhance the load_data method to handle different file formats (e.g., JSON, Excel).
- Improve Search and Filter: Add more sophisticated search and filter capabilities, such as regex matching or range filters.
- User Interface: Develop a user interface to allow users to interact with the database easily.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![1](https://github.com/IWibawa/NutriPro/blob/main/Diagrams/visual_design%20-%20search_and_comparison_screen.png?raw=true)

---

## 3.[Chart]
### Description  
- **Type**: Class
- **Usage**: Represents a visualization of nutritional data
- **Key Attributes**: `chart_type`, `data`
- **Key Methods**: `render()`
  
**Interactions**:
- Created by the `generate_nutrition_chart` function using **FoodItem** data
- Used in the user interface to display visual representations of nutritional information
- May be incorporated in **ComparisonResult** to visualize food comparisons
  
### Steps
1. Define the Class: Create a class named NutritionChart with the key attributes and methods.
2. Generate Data for Visualization: Use the FoodItem data to create a dictionary of nutritional values.
3. Create an Instance of the Visualization Class: Instantiate the NutritionChart class with the desired chart type and data.
4. Render the Chart: Call the render method to display the chart.
5. Integrate with the User Interface: Use the NutritionChart class in your application’s user interface to display nutritional data visually.
6. Use in Comparison Results: Incorporate the NutritionChart class in the ComparisonResult to visualize comparisons between different food items.
7. Additional Steps:
- Expand Chart Types: Add support for more chart types like line charts, scatter plots, etc.
- Enhance Data Handling: Improve data handling to include more detailed nutritional information.
- User Interface Improvements: Develop a more interactive user interface for better user experience.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    

![1](https://github.com/IWibawa/NutriPro/blob/main/Diagrams/visual_design%20-%20supplementary_search__screen.png?raw=true)


---

## 4. [ComparisonResult]
### Description  
- **Type**: Class
- **Usage**: Represents the result of a food comparison
- **Key Attributes**: `food_items` (list of compared **FoodItems**), `comparison_data` (nutritional data for comparison)

**Interactions**:
- Produced by the `compare_foods` function using multiple **FoodItem** instances
- Used in the user interface for side-by-side food comparisons
- May interact with the **Chart** class for visual comparison generation

### Steps
1. Define the Class: Create a class named ComparisonResult with the key attributes and methods. 
2. Generate Comparison Data: Use the compare_foods function to create instances of ComparisonResult.
3. Access Comparison Data: Use the get_comparison_data method to retrieve nutritional data for comparison.
4. Integrate with User Interface: Display the comparison data in the user interface for side-by-side comparisons.
5. Visualize Comparison Data: Use the NutritionChart class to create visual representations of the comparison data.
6. Additional Steps:
 - Expand Attributes: Include more detailed attributes like serving size, fiber, sugar, etc.
 - Enhance Methods: Add methods for more complex comparisons, such as percentage differences.
 - User Interface Improvements: Develop a more interactive and user-friendly interface for better user experience.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![1](./visual_design.png)

![2](./visual_design.png)


---

## 5. [MealPlan]
### Description  
- **Type**: Class
- **Usage**: Represents a weekly meal plan with daily breakdowns
- **Key Attributes**: `weekly_plan` (structured meal data), `daily_summaries` (nutritional summaries)
- **Key Methods**: `add_food_to_meal`, `calculate_daily_summary`, `get_weekly_overview`

**Interactions**:
- Created and populated by the `generate_meal_plan` function using **FoodItems** from the **NutritionalDatabase**
- Interacts with **FoodItem** instances to calculate nutritional summaries
- Used by `save_meal_plan` and `load_meal_plan` functions for data persistence
  
### Steps
1. Define the Class: Create a class named MealPlan with the key attributes and methods.
2. Generate a Meal Plan: Use the generate_meal_plan function to create and populate a MealPlan instance.
3. Add Food to a Meal: Use the add_food_to_meal method to add food items to specific meals on specific days.
4. Calculate Daily Summary: The calculate_daily_summary method is automatically called when food is added to a meal, updating the nutritional summary for that day.
5. Get Weekly Overview: Use the get_weekly_overview method to get a summary of the nutritional data for the entire week.
6. Get Weekly Overview: Use the get_weekly_overview method to get a summary of the nutritional data for the entire week.
7. Additional Steps:
 - Expand Attributes: Include more detailed attributes like meal times, portion sizes, etc.
 - Enhance Methods: Add methods for editing and removing food items from meals.
 - User Interface Improvements: Develop a user-friendly interface for creating and managing meal plans.


### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![1](https://github.com/IWibawa/NutriPro/blob/main/Diagrams/visual_design%20-%20meal_plan_screen.png?raw=true)


---
