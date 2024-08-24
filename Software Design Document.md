
# Software Design Document

## Project Name: Nutritional Food Database Analysis and VisualiSation Tool
# Group Number: 02

## Team members

| Student Number | Name      |
|----------------|-----------|
| s2817538       | Kate Baker |
| s5374957       | I Wibawa |
| s5414931       | Naveen Arakkal Nelson |
## Table of Contents

1. [System Vision](#1-system-vision)  
    1.1 [Problem Background](#11-problem-background)  
    1.2 [System Capabilities/Overview](#12-system-capabilitiesoverview)  
    1.3 [Potential Benefits](#13-potential-benefits)  

2. [Requirements](#2-requirements)  
    2.1 [User Requirements](#21-user-requirements)  
    2.2 [Software Requirements](#22-software-requirements)  
    2.3 [Use Case Diagrams](#23-use-case-diagrams)  
    2.4 [Use Cases](#24-use-cases)  

3. [Software Design and System Components](#3-software-design-and-system-components)  
    3.1 [Software Design](#31-software-design)  
    3.2 [System Components](#32-system-components)  
        - 3.2.1 [Functions](#321-functions)  
        - 3.2.2 [Data Structures / Data Sources](#322-data-structures--data-sources)  
        - 3.2.3 [Detailed Design](#323-detailed-design)  

   
4. [User Interface Design](#4-user-interface-design)  
    4.1 [Structural Design](#41-structural-design)  
    4.2 [Visual Design](#42-visual-design)  


## 1. System Vision

### 1.1 Problem Background

- Problem Identification: The system addresses the challenge of making informed dietary choices due to the complexity of nutritional data and the lack of user-friendly tools to analyze this information.

- Dataset: The system uses the Comprehensive Nutritional Food Database, which provides detailed nutritional information for a wide range of food items.

- Data Input/Output:
  - Input: User queries for food items, nutritional ranges, and dietary preferences.
  - Output: Nutritional information, visualizations, filtered food lists, and meal plans.

- Target Users: The system targets health-conscious individuals, dieters, nutritionists, and dietitians who need to analyze and understand nutritional information for various foods.

### 1.2 System capabilities/overview

- System Functionality: The system will provide a user-friendly interface for analyzing and visualizing nutritional data from the Comprehensive Nutritional Food Database.

- Features and Functionalities:
  1. Search for foods by name and view comprehensive nutritional information
  2. Visualize nutrition breakdowns using pie charts and bar graphs
  3. Filter foods based on specific nutritional content ranges
  4. Categorize and filter foods by nutritional levels (low, mid, high)
  5. Compare multiple food items side-by-side
  6. Generate personalized daily meal plans based on user-defined nutritional goals and preferences

### 1.3 Benefit Analysis

- Improved dietary decision-making through easy access to comprehensive nutritional information
- Enhanced understanding of nutritional content in various foods through visual representations
- Easier comparison of different food items, supporting more informed food choices
- Support for meal planning and diet management
- Potential use in educational settings to teach about nutrition
- Empowerment of users to make data-driven decisions about their diet and health
- Timesaving for nutritionists and dietitians in analyzing and presenting food nutritional data

## 2. Requirements

### 2.1 User Requirements

1. Users shall be able to search for foods by entering names in a search bar.
2. Users shall view detailed nutritional information for selected foods, including macronutrients, vitamins, and minerals.
3. Users shall visualize nutritional breakdowns through interactive pie charts and bar graphs.
4. Users shall filter foods by setting specific nutritional ranges (e.g., protein content between 10g and 20g per 100g).
5. Users shall categorize and filter foods by nutritional content levels (low, mid, high) for fat, protein, carbohydrates, sugar, and nutritional density.
6. Users shall compare multiple food items side-by-side in a comparison view.
7. Users shall generate personalized daily meal plans by inputting their nutritional goals and preferences.

Note: Since no specific client or user is assigned, we envision the primary users of this software to be health-conscious individuals, dieters, nutritionists, and dietitians who need to analyze and understand nutritional information for various foods quickly and efficiently.

### 2.2 Software Requirements

- R1.1 The system shall provide a search functionality for foods in the database.
- R1.2 The system shall display comprehensive nutritional information for each food item.
- R1.3 The system shall generate pie charts and bar graphs for nutrient breakdowns.
- R1.4 The system shall allow users to set minimum and maximum values for nutritional content filtering.
- R1.5 The system shall categorize foods into low, mid, and high levels for fat, protein, carbohydrates, sugar, and nutritional density.
- R1.6 The system shall have a graphical user interface for all interactions.
- R1.7 The system shall load and process data from the provided CSV file.
- R1.8 The system shall provide a comparison view for multiple selected food items.
- R1.9 The system shall generate personalized meal plans based on user-defined nutritional goals and preferences.
- R1.10 The system shall ensure all calculations and data presentations are accurate to two decimal places.
- R1.11 The system shall respond to user interactions within 2 seconds under normal operating conditions.

### 2.3 Use Case Diagrams

![UCD.png](Diagrams%2FUCD.png)

### 2.4 Use Cases

| Use Case ID | Use Case Name | Actors | Description | Flow of Events                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Alternate Flow | Postcondition |
|-------------|---------------|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------|
| UC001       | Search Food | User | User searches for a specific food item in the database | 1. User enters food name in the search bar<br>2. System processes the search query<br>3. System queries the Food Database<br>4. System displays a list of matching food items<br>5. User selects a specific food item<br>6. System displays detailed nutritional information for the selected item                                                                                                                                                                                 | If no matching items are found, the system displays a "No results found" message | Search results are displayed, or user is notified of no matches |
| UC002       | View Nutritional Information | User | User views detailed nutritional information for a selected food item | 1. User selects a food item from the search results or a list<br>2. System retrieves the nutritional data for the selected food from the Food Database<br>3. System displays comprehensive nutritional information including calories, macronutrients, vitamins, and minerals<br>4. User can scroll or navigate through the information                                                                                                                                            | If the food item data is unavailable, system displays an error message | Detailed nutritional information is displayed for the selected food item |
| UC003       | Visualize Nutrient Breakdown | User | User views graphical representation of a food's nutritional content | 1. User selects "Visualize" option for a food item<br>2. System retrieves nutritional data from the Food Database<br>3. System generates a pie chart showing macronutrient breakdown (fat, protein, carbohydrates)<br>4. System generates a bar graph showing micronutrient content<br>5. System displays both visualizations to the user                                                                                                                                          | If visualization cannot be generated, system displays an error message | Nutrient breakdown visualizations are displayed to the user |
| UC004       | Apply Filter Settings | User | User filters and categorizes foods based on nutrient content | 1. User navigates to the Filter Settings screen<br>2. User selects nutrient(s) to filter by (e.g., protein, carbs, fat)<br>3. User can either:<br>   a) Input specific range values for the selected nutrients, or<br>   b) Choose categorization levels (low, medium, high) for the nutrients<br>4. User applies the filter settings<br>5. System queries the Food Database based on the selected criteria<br>6. System displays the list of foods that match the filter settings | If no foods match the criteria, system displays "No foods found matching these criteria" | Filtered list of foods is displayed based on the applied settings, or user is notified of no matches |
| UC005       | Compare Foods | User | User compares nutritional information of multiple selected food items side-by-side | 1. User selects multiple food items for comparison<br>2. User chooses "Compare" option<br>3. System retrieves nutritional data for all selected items from the Food Database<br>4. System displays a side-by-side comparison of nutritional information                                                                                                                                                                                                                            | If user selects more than the maximum allowed number of items for comparison, system prompts user to reduce selection | Comparison view is displayed with nutritional information of selected foods side-by-side |
| UC006       | Generate Meal Plan | User | User generates a personalized meal plan based on nutritional goals and preferences | 1. User inputs nutritional goals and dietary preferences<br>2. User specifies the number of meals per day<br>3. System processes the input and searches the Food Database<br>4. System generates a meal plan meeting the specified criteria<br>5. System displays the meal plan to the user                                                                                                                                                                                        | If no suitable meal plan can be generated, system suggests adjustments to the user's input | Personalized meal plan is displayed, or system provides suggestions for adjustment |

## 3. Software Design and System Components

### 3.1 Software Design

![Software_design_flowchart.png](Diagrams%2FSoftware_design_flowchart.png)

Component Breakdown:

1. User Interface:
   - Web Interface: The main user interaction point
   - Search Bar: For food item searches
   - Filter/Range Selector: For applying nutritional filters
   - Visualization Panel: For displaying charts and graphs
   - Comparison Panel: For side-by-side food comparisons
   - Meal Plan Generator: Interface for creating meal plans

2. Application Layer:
   - Search Component: Handles food search functionality
   - Filter Component: Manages filtering and categorization
   - Visualization Component: Generates charts and graphs
   - Comparison Component: Processes food comparisons
   - Meal Planning Component: Generates meal plans
   - Data Manager: Central component for data handling and communication with the data layer

3. Data Layer:
   - Food Database: Stores all food and nutritional information
   - CSV File: The source of the nutritional data

4. External Services:
   - Nutritional API: Optional external service for additional nutritional data (shown with a dotted line to indicate it's not a core component)

### 3.2 System Components

#### 3.2.1 Functions

1. search_food(query: str) -> List[FoodItem]
   - Description: Searches for food items based on user input
   - Input Parameters: query (string) - The search term entered by the user
   - Return Value: A list of FoodItem objects matching the search query

2. generate_nutrition_chart(food_item: FoodItem) -> Chart
   - Description: Creates a visual representation of the nutritional breakdown
   - Input Parameters: food_item (FoodItem) - The selected food item
   - Return Value: A Chart object containing the visualization

3. filter_foods_by_nutrient(nutrient: str, min_value: float, max_value: float) -> List[FoodItem]
   - Description: Filters foods based on a specific nutrient range
   - Input Parameters:
     1. nutrient (string) - The nutrient to filter by
     2. min_value (float) - The minimum value of the nutrient
     3. max_value (float) - The maximum value of the nutrient
   - Return Value: A list of FoodItem objects that fall within the specified range

4. categorize_foods_by_nutrient_level(nutrient: str, level: str) -> List[FoodItem]
   - Description: Categorizes foods based on low, mid, or high levels of a specific nutrient
   - Input Parameters:
     1. nutrient (string) - The nutrient to categorize by
     2. level (string) - The level to filter (low, mid, or high)
   - Return Value: A list of FoodItem objects in the specified category

5. compare_foods(food_items: List[FoodItem]) -> ComparisonResult
   - Description: Compares multiple food items
   - Input Parameters: food_items (List[FoodItem]) - A list of FoodItem objects to compare
   - Return Value: A ComparisonResult object containing the comparison data

#### 3.2.2 Data Structures / Data Sources

1. FoodItem
   - Type: Class
   - Usage: Represents a single food item with all its nutritional information
   - Attributes:
     - name: str
     - calories: float
     - protein: float
     - carbohydrates: float
     - fats: float
     - vitamins: Dict[str, float]
     - minerals: Dict[str, float]
   - Methods:
     - get_nutrient_value(nutrient: str) -> float

2. NutritionalDatabase
   - Type: Class
   - Usage: Manages the entire database of food items
   - Attributes:
     - food_items: List[FoodItem]
   - Methods:
     - load_data(file_path: str)
     - search_food(query: str) -> List[FoodItem]
     - apply_filters(filters: Dict[str, Any]) -> List[FoodItem]

3. Chart
   - Type: Class
   - Usage: Represents a visualization of nutritional data
   - Attributes:
     - chart_type: str
     - data: Dict[str, Any]
   - Methods:
     - render() -> Image

4. ComparisonResult
   - Type: Class
   - Usage: Represents the result of a food comparison
   - Attributes:
     - food_items: List[FoodItem]
     - comparison_data: Dict[str, List[float]]

#### 3.2.3 Detailed Design
1. search_food(query: str) -> List[FoodItem]
   - ![Function_detailed_design - search_food.png](Diagrams%2FFunction_detailed_design%20-%20search_food.png)
2. generate_nutrition_chart(food_item: FoodItem)
   - ![Function_detailed_design - generate_nutrition_chart.png](Diagrams%2FFunction_detailed_design%20-%20generate_nutrition_chart.png)
3. filter_foods_by_nutrient(nutrient: str, min_value: float, max_value: float) -> List[FoodItem]
   - ![Function_detailed_design - filter_foods_by_nutrient.png](Diagrams%2FFunction_detailed_design%20-%20filter_foods_by_nutrient.png)
4. categorize_foods_by_nutrient_level(nutrient: str, level: str) -> List[FoodItem]
   - ![Function_detailed_design - categorize_foods_by_nutrient_level.png](Diagrams%2FFunction_detailed_design%20-%20categorize_foods_by_nutrient_level.png)
5. compare_foods(food_items: List[FoodItem]) -> ComparisonResult
   - ![Function_detailed_design - compare_foods.png](Diagrams%2FFunction_detailed_design%20-%20compare_foods.png)
6. generate_meal_plan(user_preferences: Dict, nutritional_goals: Dict, num_days: int) -> MealPlan
   - ![Function_detailed_design - generate_meal_plan.png](Diagrams%2FFunction_detailed_design%20-%20generate_meal_plan.png)

## 4. User Interface Design

### 4.1 Structural Design

![Structural_Design.png](Diagrams%2FStructural_Design.png)

The Nutritional Food Database application is structured as follows:

#### Main Application Window
The main window consists of two primary sections:
- Header
- Content Area

#### Header
The header contains:
- Logo: Reinforces brand identity
- Navigation Menu: Provides quick access to main sections
  - Home
  - Compare
  - Meal Plan

#### Content Area
The content area is the primary interface for user interactions, comprising:

1. **Search Bar**: 
   - Prominently placed for easy access
   - Allows users to search for food items
2. **Results/Content Display**:
   - Dynamically shows different views based on user interaction:
     - Food List View: Displays search results
     - Detailed Food View: Shows comprehensive information about a selected food item
     - Comparison View: Allows side-by-side comparison of multiple food items
     - Meal Plan View: Displays generated meal plans
3. **Filter Panel**:
   - Enables users to refine search results or set preferences
   - Typically located on the right side for easy access
4. **Visualization Area**:
   - Presents nutritional data in graphical formats
   - Enhances understanding of nutritional information

#### Design Choices
1. The hierarchical structure ensures clear organization of features and information.
2. Centrally placing the search bar emphasizes its importance in the user workflow.
3. The consistent right-sided filter panel provides a familiar location for refining searches.
4. Separating different content views (list, details, comparison, meal plan) allows for focused presentation of information.
5. Including a visualization area enables quick understanding of nutritional data through graphical representations.

This structure is designed to provide an intuitive and efficient user experience, allowing easy navigation between different functionalities while maintaining a clear and organized interface.
### 4.2 Visual Design

1. Main search screen
   - This screen serves as the main entry point for users. It features:
     - A prominent search bar for food queries
     - A large area for displaying search results
     - A right-sided panel for applying filters
     - Clear navigation options in the header
     ![visual_design - main_search_screen.png](Diagrams%2Fvisual_design%20-%20main_search_screen.png)
2. Detailed food information view
    - This view provides comprehensive information about a selected food item:
      - Nutritional information is clearly separated into two panels: general nutrition and vitamin/mineral content
      - "Visualize" and "Add to Comparison" buttons offer quick access to additional features
      - A "Back to Search" option ensures easy navigation
      ![visual_design - food_details_screen.png](Diagrams%2Fvisual_design%20-%20food_details_screen.png)
3. Nutrition breakdown visualization
   - This screen offers a visual representation of a food item's nutritional content:
     - Macronutrients are displayed in a large chart or graph (left panel)
     - Micronutrients are listed with visual indicators of their relative quantities (right panel)
     - A "Back" button allows users to return to the previous screen
     ![visual_design - nutrition_breakdown_screen.png](Diagrams%2Fvisual_design%20-%20nutrition_breakdown_screen.png)
4. Filter settings screen
    - The filter screen allows users to refine their food searches:
      - Separate sections for "Nutrient Ranges" and "Nutrient Levels" provide comprehensive filtering options
      - "Apply Filters" and "Reset" buttons give users control over their selections
      - Consistent with other screens, a "Back to Search" option is available
      ![visual_design - filter_screen.png](Diagrams%2Fvisual_design%20-%20filter_screen.png)
5. Food Comparison
   - This screen enables users to compare multiple food items side-by-side:
     - Three columns allow for easy comparison of nutritional information
     - "Add Another Food" and "Generate Comparison Chart" buttons provide additional functionality
     - Consistent with other screens, a "Back to Search" option is available
     ![visual_design - comparison_screen.png](Diagrams%2Fvisual_design%20-%20comparison_screen.png)
6. Meal Plan Screen
   - The meal plan screen allows users to create and view personalized meal plans:
     - A calendar view displays meals for each day of the week
     - Each day shows breakfast, lunch, dinner, and snacks
     - Users can add or edit meals for each time slot
     - Nutritional information summaries are provided for each day
     - "Generate Meal Plan" and "Save Meal Plan" buttons offer key functionality
     ![visual_design - meal_plan_screen.png](Diagrams%2Fvisual_design%20-%20meal_plan_screen.png)