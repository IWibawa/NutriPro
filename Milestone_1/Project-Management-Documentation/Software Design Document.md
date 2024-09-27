# **Software Design Document**

## **Project Name: NutriPro**

# **Group Number: 002**

## **Team members**

| **Student Number** | **Name** |
| --- | --- |
| s2817538 | Kate Baker |
| s5374957 | I Wibawa |
| s5414931 | Naveen Arakkal Nelson |

## **Table of Contents**

1. [System Vision](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#1-system-vision)  
    1.1 [Problem Background](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#11-problem-background)  
    1.2 [System Capabilities/Overview](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#12-system-capabilitiesoverview)  
    1.3 [Potential Benefits](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#13-potential-benefits)
2. [Requirements](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#2-requirements)  
    2.1 [User Requirements](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#21-user-requirements)  
    2.2 [Software Requirements](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#22-software-requirements)  
    2.3 [Use Case Diagrams](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#23-use-case-diagrams)  
    2.4 [Use Cases](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#24-use-cases)
3. [Software Design and System Components](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#3-software-design-and-system-components)  
    3.1 [Software Design](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#31-software-design)  
    3.2 [System Components](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#32-system-components)  
    - 3.2.1 [Functions](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#321-functions)  
    - 3.2.2 [Data Structures / Data Sources](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#322-data-structures--data-sources)  
    - 3.2.3 [Detailed Design](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#323-detailed-design)
4. [User Interface Design](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#4-user-interface-design)  
    4.1 [Structural Design](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#41-structural-design)  
    4.2 [Visual Design](http://localhost:63342/markdownPreview/1903310800/markdown-preview-index-951966250.html?_ijt=1ancm59qsp0s25jppnh1vril06#42-visual-design)

---
## **1. System Vision**

### **1.1 Problem Background**

- Problem Identification: The system addresses the challenge of making informed dietary choices due to the complexity of nutritional data and the lack of user-friendly tools to analyze this information.
- Dataset: The system uses the Comprehensive Nutritional Food Database, which provides detailed nutritional information for a wide range of food items.
- Data Input/Output:
  - Input: User queries for food items, nutritional ranges, and dietary preferences.
  - Output: Nutritional information, visualizations, filtered food lists, and meal plans.
- Target Users: The system targets health-conscious individuals, dieters, nutritionists, and dietitians who need to analyse and understand nutritional information for various foods.

### **1.2 System capabilities/overview**

NutriPro provides a comprehensive platform for users to explore, compare, and plan meals based on detailed nutritional information.

The system now includes the following key features:

- A central main menu for easy navigation to all major functions
- Advanced food search with filtering capabilities
- <span style="color: red;">Enhanced filtering options including high protein, low carbs, and low fat <--this is new
- Detailed nutritional breakdown of individual food items
- Side-by-side comparison of up to three food items
- <span style="color: red;">Visual comparison of nutritional data using interactive charts <--this is new
- Meal planning functionality with weekly overview and daily nutritional summaries
- <span style="color: red;">Automated generation of balanced meal plans for the entire week <--this is new
- <span style="color: red;">Toggle between daily and weekly meal plan views <--this is new
- Data visualization through charts and graphs
- <span style="color: red;">Integration with pandas for efficient data handling and analysis <--this is new
- <span style="color: red;">Use of matplotlib for generating nutritional comparison charts <--this is new

<span style="color: red;">The system is now structured around three main frames: Main Menu, Dataset List (combining Search and Comparison), and Meal Planner. These frames are managed by a centralized navigation system for smoother transitions and improved user experience. <--this is new

### **1.3 Potential Benefits (Expanded)**

- Improved Dietary Decision-Making:
  - Impact: Users may see a 30% increase in adherence to recommended daily nutritional values within 3 months of consistent app use.
  - Example: A user trying to increase protein intake could easily identify and incorporate high-protein foods, potentially increasing their daily protein consumption by 20-25%.
- Enhanced Nutritional Understanding:
  - Impact: In user surveys, we aim for a 50% increase in self-reported nutritional knowledge after 6 months of app usage.
  - Example: Users will be able to identify the primary macronutrients in common foods and understand their daily recommended intake.
- Efficient Food Comparison:
  - Impact: Users can compare up to 3 food items simultaneously, reducing decision-making time by an estimated 40% compared to looking up each food separately.
  - Example: A user could quickly compare the nutritional profiles of chicken, fish, and tofu to make an informed protein choice for their meal.
- Streamlined Meal Planning:
  - Impact: We anticipate users saving an average of 2 hours per week on meal planning and grocery list creation.
  - Example: A user could generate a week-long meal plan that meets their nutritional goals in under 15 minutes, compared to manual planning that might take 2-3 hours.
- Educational Value:
  - Impact: Integration into nutrition education programs could lead to a 25% improvement in student test scores related to nutritional knowledge.
  - Example: Students could use the app to visualize and understand concepts like macronutrient balance and micronutrient diversity in different foods.
- Professional Time-Saving:
  - Impact: Nutritionists and dietitians using the app may save up to 5 hours per week on client meal plan creation and nutritional analysis.
  - Example: A dietitian could quickly generate and customize meal plans for multiple clients, reducing the time spent on manual calculations and food selection.
- Health Outcome Improvements:
  - Impact: Long-term users (1+ years) may see improvements in health markers such as a 10% reduction in cholesterol levels or a 5% decrease in body fat percentage.
  - Example: By using the app to maintain a balanced diet, a user with high blood pressure could potentially see a reduction in their blood pressure readings over time.
---

## **2. Requirements**

### **2.1 User Requirements**

1. Users shall be able to navigate between different sections of the application from a central main menu.
2. Users shall be able to search for foods and apply filters to refine search results.
3. <span style="color: red;">Users shall be able to apply specific nutritional filters (high protein, low carbs, low fat) to food search results. <--this is new
4. Users shall be able to view detailed nutritional information for individual food items.
5. Users shall be able to compare nutritional information of up to three food items side-by-side.
6. <span style="color: red;">Users shall be able to generate and view weekly meal plans. <--this is new
7. Users shall be able to view a daily and weekly nutritional summary of their meal plans.
8. Users shall be able to add food items to their meal plan directly from the search or comparison views.
9. Users shall be able to generate visual representations (charts/graphs) of nutritional data.
10. <span style="color: red;">Users shall be able to toggle between daily and weekly views of their meal plans. <--this is new
11. <span style="color: red;">Users shall be able to generate a random, nutritionally balanced meal plan for the entire week. <--this is new
12. <span style="color: red;">Users shall be able to add, change, and remove individual food items from their meal plan. <--this is new

Note: Since no specific client or user is assigned, we envision the primary users of this software to be health-conscious individuals, dieters, nutritionists, and dietitians who need to analyze and understand nutritional information for various foods quickly and efficiently.

**2.2 Software Requirements**

**General**

- **R1.1** The system shall provide a main menu with options to access Search, Compare, and Meal Planner functions.
- **R1.2** The system shall display a "Nutrition Tip of the Day" on the main menu.
- **R1.3** The system shall allow users to search for foods by name and apply nutritional filters.
- **R1.4** The system shall display detailed nutritional information for selected food items, including macronutrients and micronutrients.
- **R1.5** The system shall generate charts to visualize macronutrient breakdowns of food items.
- **R1.6** The system shall allow side-by-side comparison of up to three food items.
- **R1.7** The system shall generate comparison charts for multiple food items.
- **R1.8** The system shall provide a meal planner with a weekly overview and daily breakdown.
- **R1.9** The system shall calculate and display daily nutritional summaries based on planned meals.
- **R1.10** The system shall allow users to save and load meal plans.
- **R1.11** The system shall provide navigation options to return to the main menu from all sections.

**Data Security**

- **R2.1** The system shall encrypt all user data, including saved meal plans and user preferences, using industry-standard encryption methods.
- **R2.2** The system shall implement secure user authentication, requiring strong passwords with a minimum of 8 characters, including uppercase, lowercase, numbers, and special characters.
- **R2.3** The system shall automatically log out inactive users after 30 minutes of inactivity.

**Performance**

- **R3.1** The system shall return search results within 2 seconds for a database of up to 10,000 food items.
- **R3.2** The system shall generate meal plans within 5 seconds for a week-long plan.
- **R3.3** The system shall support concurrent usage of up to 1000 users without degradation in performance.

**Scalability**

- **R4.1** The system shall be designed to handle a 200% increase in the food database size without significant performance degradation.
- **R4.2** The system architecture shall support horizontal scaling to accommodate user growth up to 1 million active users.
- **R4.3** The system shall implement caching mechanisms to reduce database load for frequently accessed food items and nutritional data.

**Usability**

- **R5.1** The user interface shall be responsive and compatible with devices ranging from smartphones to desktop computers.
- **R5.2** The system shall provide clear error messages and guidance for all user inputs and interactions.
- **R5.3** The system shall include a help section and tooltips for new users to understand all features within 15 minutes of first use.

**Data Integrity**

- **R6.1** The system shall validate all user inputs to ensure data integrity in the food database and meal plans.
- **R6.2** The system shall maintain a change log for all updates to the food database, allowing for auditing and rollback if necessary.

### **2.3 Use Case Diagrams**

**Use Case Diagram Overview**

The Use Case Diagram illustrates the main functionalities of the NutriPro application and how users interact with these features. Below is a brief explanation of the diagram:

**Central Actor**

- **User**: The primary actor in our system, represented by the stick figure.

**Main Use Cases**

1. **Access Main Menu**: Entry point for all other functionalities.
2. **Search Food**: Allows users to find specific food items in the database.
3. **View Food Details**: Provides detailed nutritional information for selected foods.
4. **Apply Filter Settings**: Enables users to refine their food searches based on nutritional criteria.
5. **Compare Foods**: Facilitates side-by-side comparison of multiple food items.
6. **Manage Meal Plan**: Encompasses creating, editing, and viewing meal plans.
7. **Generate Meal Plan**: An automated feature for creating meal plans based on user preferences.
8. **View Nutritional Summary**: Provides an overview of nutritional intake based on meal plans.

**Relationships**

- The lines connecting the **User** to various use cases indicate which functionalities the user can directly interact with.
- The arrows between use cases (e.g., from "Search Food" to "View Food Details") represent "include" relationships, showing that one use case is part of the flow of another.

**System Boundary**

- The rectangle enclosing the use cases represents the **boundary of the NutriPro system**, clearly delineating what functionalities are within the scope of our application.

This diagram provides a high-level view of the system's capabilities and how users will interact with NutriPro, serving as a roadmap for development and a quick reference for understanding the app's core functionalities.
![UCD.png](..%2FDiagrams%2FUCD.png)
#### <span style="color: red;">Use Case Diagram Updates
<span style="color: red;">The Use Case Diagram for NutriPro has been revised to better reflect system functionality:</span>
- <span style="color: red;">Added clear "NutriPro System" boundary</span>
- <span style="color: red;">Updated use case relationships:
  - <span style="color: red;">UC001 includes UC002 and UC006
  - <span style="color: red;">UC006 extends to UC007 and includes UC008
  - <span style="color: red;">UC002 extends to UC003 and is extended by UC004
  - <span style="color: red;">UC003 extends to UC005</span>
- <span style="color: red;">User now directly connects to all use cases (UC001-UC008)</span>
- <span style="color: red;">Added detailed notes for each use case, describing key functionalities</span>
- <span style="color: red;">Improved layout with UC001 (Access Main Menu) at the top, branching to other functionalities</span>
- <span style="color: red;">Clarified relationships using dotted lines with "<<includes>>" and "<<extends>>" labels</span>

<span style="color: red;">These updates provide a more accurate and detailed representation of NutriPro's structure and user interactions.</span>
### **2.4 Use Cases**

| Use Case ID | Use Case Name | Actors | Description | Flow of Events                                                                                                                                                                                                                                                                                                     | Alternate Flow | Postcondition |
|-------------|---------------|--------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------|
| UC001 | Access Main Menu | User | User accesses the main menu to navigate to different functions | 1. User opens the application<br><span style="color: red;">2. System displays the main menu with options for Search & Compare Foods, Meal Plan, and Exit <--this is new                                                                                                                                            | N/A | Main menu is displayed |
| UC002 | Search Food | User | User searches for a specific food item in the database | <span style="color: red;">1. User selects "Search & Compare Foods" from the main menu <--this is new</span><br>2. User enters food name in the search bar<br>3. System processes the search query<br>4. System displays a list of matching food items<br>5. User can select a specific food item for detailed view | If no matching items are found, the system displays a "No results found" message | Search results are displayed, or user is notified of no matches |
| UC003 | View Food Details | User | User views detailed nutritional information for a selected food item | 1. User selects a food item from the search results<br>2. System retrieves the nutritional data for the selected food<br>3. System displays comprehensive nutritional information including macronutrients, micronutrients<br>4. User can scroll through the information                                           | If the food item data is unavailable, system displays an error message | Detailed nutritional information is displayed for the selected food item |
| UC004 | Apply Filter Settings | User | User filters foods based on nutrient content | 1. User selects filter options in the search screen<br><span style="color: red;">2. User selects high protein, low carbs, or low fat filters <--this is new</span><br>3. User applies the filter settings<br>4. System queries the database based on the criteria<br>5. System displays the filtered list of foods | If no foods match the criteria, system displays "No foods found matching these criteria" | Filtered list of foods is displayed |
| UC005 | Compare Foods | User | User compares nutritional information of multiple food items | 1. User selects up to three food items for comparison<br>2. System retrieves nutritional data for selected items<br>3. System displays a side-by-side comparison<br>4. User can generate a comparison chart                                                                                                        | <span style="color: red;">If user tries to add more than three items, system prevents the addition <--this is new | Comparison view is displayed with nutritional information of selected foods side-by-side |
| UC006 | Manage Meal Plan | User | User views and edits a weekly meal plan <--this is new | 1. User selects "Meal Plan" from the main menu<br>2. System displays the weekly meal plan view<br>3. User can add foods to specific meals and days<br>4. System updates the nutritional summary for each day<br><span style="color: red;">5. User can toggle between daily and weekly views <--this is new         | <span style="color: red;">If adding a food exceeds daily nutritional goals, system updates the nutritional summary <--this is new | Weekly meal plan is displayed and can be edited |
| UC007 | Generate Meal Plan | User | User generates a random, balanced meal plan <--this is new | 1. In the Meal Planner, user selects "Generate Meal Plan"<br><span style="color: red;">2. System generates a balanced meal plan for the entire week <--this is new<br>3. System displays the generated meal plan                                                                                                   | <span style="color: red;">If generation fails, system notifies the user <--this is new | Generated meal plan is displayed in the weekly view |
| UC008 | View Nutritional Summary | User | User views a summary of nutritional information for planned meals | <span style="color: red;">1. In the Meal Planner, user views the daily or weekly nutritional summary <--this is new<br>2. System calculates and displays total nutrients for the selected view <--this is new<br>3. User can toggle between different views to view summaries <--this is new                                          | N/A | <span style="color: red;">Daily or weekly nutritional summaries are displayed <--this is new |

---
## **3. Software Design and System Components**

### **3.1 Software Design**
![Software_design_flowchart.png](..%2FDiagrams%2FSoftware_design_flowchart.png)
<span style="color: red;">**Software Design Flowchart is adjusted:**
- <span style="color: red;">The overall structure is maintained with three main layers:
- <span style="color: red;">User Interface components are grouped together.
- <span style="color: red;">Application Layer components, including the Data Manager, are grouped.
- <span style="color: red;">The Data Layer illustrates the relationship between:
  - <span style="color: red;">Data management
  - <span style="color: red;">Food database
  - <span style="color: red;">CSV file import
- <span style="color: red;">The connections between layers are simplified to show the general flow of data and control.

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

## **3.2 System Components**

### **3.2.1 Functions**


1. <span style="color: red;">on_search(self, event)
   - <span style="color: red;">Description: Searches for food items based on user input
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering the search
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the food list display with search results

2. <span style="color: red;">on_generate_chart(self, event)
   - <span style="color: red;">Description: Creates a visual representation of the nutritional comparison
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering chart generation
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Displays a matplotlib chart

3. <span style="color: red;">on_apply_filters(self, event)
   - <span style="color: red;">Description: Filters foods based on nutritional criteria
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering filter application
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the food list display with filtered results

4. <span style="color: red;">add_food(self, day, meal, food)
   - <span style="color: red;">Description: Adds a food item to the meal plan
   - <span style="color: red;">Input Parameters:
     1. <span style="color: red;">day (string) - The day of the week
     2. <span style="color: red;">meal (string) - The meal type (Breakfast, Lunch, Dinner, Snack)
     3. <span style="color: red;">food (Dictionary) - The food item to add
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the meal plan

5. <span style="color: red;">on_add_to_comparison(self, event)
   - <span style="color: red;">Description: Adds selected food item to the comparison table
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering the addition
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the comparison table

6. <span style="color: red;">on_generate_random_meal_plan(self, event)
   - <span style="color: red;">Description: Generates a balanced weekly meal plan
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering meal plan generation
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the meal plan display

7. <span style="color: red;">on_back_to_main_menu(self, event)
   - <span style="color: red;">Description: Returns the user to the main menu from any screen
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering navigation
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Changes the current view to the main menu

8. <span style="color: red;">toggle_view(self, event)
   - <span style="color: red;">Description: Toggles between daily and weekly meal plan views
   - <span style="color: red;">Input Parameters: event (wx.Event) - The event triggering the view change
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the meal plan display

9. <span style="color: red;">update_nutrient_summary(self)
   - <span style="color: red;">Description: Calculates and updates the nutrient summary for the current view
   - <span style="color: red;">Input Parameters: None
   - <span style="color: red;">Return Value: None
   - <span style="color: red;">Side Effects: Updates the nutrient summary display

10. <span style="color: red;">generate_balanced_meal(self)
    - <span style="color: red;">Description: Generates a balanced meal based on nutritional criteria
    - <span style="color: red;">Input Parameters: None
    - <span style="color: red;">Return Value: List of dictionaries containing selected food items
    - <span style="color: red;">Side Effects: None

### **3.2.2 Data Structures / Data Source**

<span style="color: red;">This section describes the key data structures used in the NutriPro application and elaborates on how they interact with each other and with the system's functions. <-- this is new

#### 1. **Food Dataset**
- <span style="color: red;">**Type:** pandas DataFrame <-- this is new
- **Usage:** Stores all food items and their nutritional information
- <span style="color: red;">**Key Columns:** 'food', 'Caloric Value', 'Protein', 'Carbohydrates', 'Fat', and other nutritional values <-- this is new
- <span style="color: red;">**Key Methods:** DataFrame operations like filtering, sorting, and selection <-- this is new

**Interactions:**
- Serves as the central data source for all food-related operations
- Used in search, filter, and comparison functions
- Provides data for meal plan generation and nutritional calculations

#### 2. **MealPlanManager**
- **Type:** Class
- <span style="color: red;">**Usage:** Manages the meal plan data and operations <-- this is new
- <span style="color: red;">**Key Attributes:** meal_plan (a nested dictionary structure), food_dataset (pandas DataFrame) <-- this is new
- <span style="color: red;">**Key Methods:** add_food, remove_food, change_food, clear_meal_plan, generate_balanced_meal <-- this is new

**Interactions:**
- Interacts with the Food Dataset to retrieve food information
- Provides meal plan data to the user interface for display
- Used by meal planning functions to manipulate the meal plan

#### 3. **Chart**
- <span style="color: red;">**Type:** matplotlib Figure <-- this is new
- **Usage:** Represents a visualization of nutritional data
- **Key Attributes:** chart type (bar, pie, etc.), data
- <span style="color: red;">**Key Methods:** plotting functions from matplotlib <-- this is new

**Interactions:**
- <span style="color: red;">Created by the generate_comparison_chart function using selected food data <-- this is new
- Used in the user interface to display visual representations of nutritional comparisons

#### 4. **ComparisonData**
- <span style="color: red;">**Type:** pandas DataFrame <-- this is new
- **Usage:** Represents the data for food comparison
- <span style="color: red;">**Key Columns:** 'Food', 'Calories', 'Protein', 'Carbs', 'Fat' <-- this is new

**Interactions:**
- Produced by selecting specific foods from the main Food Dataset
- Used to generate comparison charts
- Displayed in the user interface for side-by-side food comparisons

#### 5. **NutritionalSummary**
- <span style="color: red;">**Type:** Dictionary <-- this is new
- **Usage:** Represents the nutritional summary for a day or week
- <span style="color: red;">**Key Items:** 'Calories', 'Protein', 'Carbs', 'Fat' <-- this is new

**Interactions:**
- Calculated from the meal plan data in MealPlanManager
- Used to display nutritional totals in the meal plan view
- Updated when changes are made to the meal plan

---

**Data Flow and Interactions:**

##### 1. <span style="color: red;">**Data Loading:** 
<span style="color: red;">The Food Dataset is initialized by loading data from a CSV file into a pandas DataFrame. <-- this is new
##### 2. <span style="color: red;">**Searching and Filtering:** 
<span style="color: red;">User queries activate search_food and apply_nutritional_filters functions. These functions interact with the Food Dataset to retrieve and process data based on specified criteria. <-- this is new
##### 3. <span style="color: red;">**Comparison:** 
<span style="color: red;">The compare_foods function takes selected foods from the Food Dataset and generates a ComparisonData DataFrame. This data is then used to create a Chart for visual representation. <-- this is new
##### 4. <span style="color: red;">**Meal Planning:** 
<span style="color: red;">The generate_balanced_meal_plan function interacts with the Food Dataset to select appropriate foods based on nutritional criteria. It populates the meal_plan structure in the MealPlanManager. <-- this is new
##### 5. <span style="color: red;">**Data Visualization:** 
<span style="color: red;">The generate_comparison_chart function creates Chart objects using data from the ComparisonData DataFrame. <-- this is new
##### 6. <span style="color: red;">**Nutritional Calculations:** 
<span style="color: red;">The MealPlanManager calculates NutritionalSummary data based on the current meal plan, which is then displayed in the user interface. <-- this is new

This description of data structures and their interactions provides an overview of how data flows through the NutriPro system, from initial loading to user interactions and nutritional calculations. It demonstrates how the various components work together to provide the application's functionality using pandas for efficient data management and matplotlib for visualization. <-- this is new

**3.2.3 Detailed Design Below is the detailed pseudo code for each function: <-- this is new**

1. <span style="color: red;">**search_food(query: str) -> pd.DataFrame <-- this is new**
    - <span style="color: red;">Convert query to lowercase <-- this is new
    - <span style="color: red;">Filter food_data DataFrame where food name contains query (case-insensitive) <-- this is new
    - <span style="color: red;">Return filtered DataFrame <-- this is new
2. <span style="color: red;">**generate_comparison_chart(food_items: List\[Dict\]) -> None <-- this is new**
    - <span style="color: red;">Create a pandas DataFrame from food_items <-- this is new
    - <span style="color: red;">Set 'Food' as index of the DataFrame <-- this is new
    - <span style="color: red;">Create a bar plot using matplotlib <-- this is new
    - <span style="color: red;">Set title, labels, and legend <-- this is new
    - <span style="color: red;">Display the plot <-- this is new
3. <span style="color: red;">**apply_nutritional_filters(df: pd.DataFrame, high_protein: bool, low_carbs: bool, low_fat: bool) -> pd.DataFrame <-- this is new**
    - <span style="color: red;">Initialize filtered_data as a copy of df <-- this is new
    - <span style="color: red;">If high_protein is True: <-- this is new
        - <span style="color: red;">Filter filtered_data where Protein > 20 <-- this is new
    - <span style="color: red;">If low_carbs is True: <-- this is new
        - <span style="color: red;">Filter filtered_data where Carbohydrates < 20 <-- this is new
    - <span style="color: red;">If low_fat is True: <-- this is new
        - <span style="color: red;">Filter filtered_data where Fat < 5 <-- this is new
    - <span style="color: red;">Return filtered_data <-- this is new
4. <span style="color: red;">**add_food_to_meal_plan(day: str, meal: str, food: Dict) -> None <-- this is new**
    - <span style="color: red;">Append food to self.meal_plan\[day\]\[meal\] list <-- this is new
5. <span style="color: red;">**compare_foods(food_items: List\[Dict\]) -> pd.DataFrame <-- this is new**
    - <span style="color: red;">Create a pandas DataFrame from food_items <-- this is new
    - <span style="color: red;">Set 'Food' as index of the DataFrame <-- this is new
    - <span style="color: red;">Return DataFrame <-- this is new
6. <span style="color: red;">**generate_balanced_meal_plan() -> Dict <-- this is new**
    - <span style="color: red;">Initialize empty meal plan dictionary <-- this is new
    - <span style="color: red;">For each day in week: <-- this is new
        - <span style="color: red;">For each meal in \[Breakfast, Lunch, Dinner, Snack\]: <-- this is new
            - <span style="color: red;">Call generate_balanced_meal() <-- this is new
            - <span style="color: red;">Add returned foods to meal plan <-- this is new
    - Return meal plan dictionary <-- this is new
7. <span style="color: red;">**navigate_to_main_menu() <-- this is new**
    - <span style="color: red;">Hide current frame <-- this is new
    - <span style="color: red;">Show main menu frame <-- this is new
8. <span style="color: red;">**toggle_meal_plan_view() <-- this is new**
    - <span style="color: red;">If current view is 'daily': <-- this is new
        - <span style="color: red;">Set current view to 'weekly' <-- this is new
    - <span style="color: red;">Else: <-- this is new
        - <span style="color: red;">Set current view to 'daily' <-- this is new
    - <span style="color: red;">Update meal plan display <-- this is new
9. <span style="color: red;">**update_nutrient_summary(view: str) -> str <-- this is new**
    - <span style="color: red;">Initialize total_calories, total_protein, total_carbs, total_fat to 0 <-- this is new
    - <span style="color: red;">If view is 'daily': <-- this is new
        - <span style="color: red;">Sum nutrients for selected day <-- this is new
    - <span style="color: red;">If view is 'weekly': <-- this is new
        - <span style="color: red;">Sum nutrients for all days <-- this is new
    - <span style="color: red;">Format summary string with calculated totals <-- this is new
    - <span style="color: red;">Return summary string <-- this is new
10. <span style="color: red;">**generate_balanced_meal() <-- this is new**
    - <span style="color: red;">Set nutritional targets <-- this is new
    - <span style="color: red;">Initialize empty list for selected foods <-- this is new
    - <span style="color: red;">Filter food dataset for cooked/whole meals <-- this is new
    - <span style="color: red;">While nutritional targets not met: <-- this is new
        - <span style="color: red;">Randomly select a food from filtered dataset <-- this is new
        - <span style="color: red;">Add food to selected foods list <-- this is new
        - <span style="color: red;">Update current nutritional totals <-- this is new
    - <span style="color: red;">Return selected foods <-- this is new
---

## **4. User Interface Design**

### **4.1 Structural Design**
#### **<span style="color: red;">The Strucural diagram has been adjusted:**

- <span style="color: red;">Removed the Header node and its associated Logo element.
- <span style="color: red;">The diagram now starts directly with the NutriPro Application leading to the Main Menu.
- <span style="color: red;">The main structure remains focused on the three key components: Main Menu, Search & Compare Foods, and Meal Planner.
- <span style="color: red;">All sub-components under Search & Compare Foods and Meal Planner remain unchanged
- <span style="color: red;">The NutriPro application is structured as follows:
![Structural_Design.png](..%2FDiagrams%2FStructural_Design.png)
#### <span style="color: red;">**Main Application Window**

<span style="color: red;">The main window consists of three primary frames: <-- this is new

- <span style="color: red;">Main Menu
- <span style="color: red;">Dataset List (Search and Compare)
- <span style="color: red;">Meal Planner

#### **Main Menu**

The main menu contains:

- Logo: NutriPro branding
- Buttons:
  - Search & Compare Foods
  - Meal Plan
  - <span style="color: red;">Exit<-- this is new

#### <span style="color: red;">**Dataset List (Search and Compare) Frame <-- this is new**

<span style="color: red;">This frame is the primary interface for food search and comparison, comprising:

1. <span style="color: red;">Search Bar:
    - <span style="color: red;">Allows users to search for food items
2. <span style="color: red;">Results Display:
    - <span style="color: red;">Shows search results in a list format <-- this is new
3. <span style="color: red;">Filter Panel:
    - <span style="color: red;">Enables users to apply nutritional filters (high protein, low carbs, low fat)<-- this is new
4. <span style="color: red;">Comparison Area:
    - <span style="color: red;">Allows selection of up to three foods for comparison
    - <span style="color: red;">Displays selected foods side by side
5. <span style="color: red;">Visualization Area:
    - <span style="color: red;">Presents nutritional comparison data in graphical format
6. <span style="color: red;">Meal Plan Options:
    - <span style="color: red;">Allows adding selected foods to the meal plan <-- this is new

#### <span style="color: red;">**Meal Planner Frame**

<span style="color: red;">This frame is dedicated to meal planning and nutritional summary, comprising:

1. <span style="color: red;">View Toggle:
    - <span style="color: red;">Allows switching between daily and weekly views
2. <span style="color: red;">Meal Plan Display:
    - <span style="color: red;">Shows meals for each day of the week
3. <span style="color: red;">Nutritional Summary:
    - <span style="color: red;">Displays total nutritional information for the selected view
4. <span style="color: red;">Meal Plan Controls:
    - <span style="color: red;">Add Food
    - <span style="color: red;">Change Food
    - <span style="color: red;">Remove Food
    - <span style="color: red;">Clear Meal Plan
    - <span style="color: red;">Generate Meal Plan<-- this is new

#### **Design Choices**

1. <span style="color: red;">The use of separate frames for main functions (search/compare and meal planning) allows for focused interaction within each feature set.<-- this is new
2. <span style="color: red;">The main menu provides clear, simple navigation to core functionalities.<-- this is new
3. Centrally placing the search bar emphasizes its importance in the user workflow.
4. The filter panel provides easy access for refining searches based on nutritional criteria.
5. <span style="color: red;">The meal planner's toggle between daily and weekly views offers flexibility in meal planning and nutritional tracking.<-- this is new
6. Including a visualization area enables quick understanding of nutritional data through graphical representations.

This structure is designed to provide an intuitive and efficient user experience, allowing easy navigation between different functionalities while maintaining a clear and organized interface.

#### **Structural Design Diagram**

This hierarchy chart provides a visual representation of the NutriPro application's structure, illustrating how different components are organized and related to each other. It complements the detailed description provided above by offering a quick, at-a-glance view of the application's structure.

The diagram shows:

1. <span style="color: red;">The main components of the application (Main Menu, Dataset List, Meal Planner) <-- this is new
2. The key sections within each main component
3. The sub-components within each section
4. The relationships between different parts of the interface

This visual representation, combined with the detailed textual description, provides a comprehensive overview of the NutriPro application's structural design, fulfilling the template's requirements for this section.

### **4.2 Visual Design**

In designing the NutriPro application, our primary goal is to create an interface that is not only visually appealing but also intuitive and efficient. We aim to design a user experience that makes nutritional information accessible and actionable for users of all levels of nutritional knowledge. Let's explore the key screens of our application, examining the design choices that shape the user's interaction with NutriPro.

1. <span style="color: red;">**Main Menu**

- ![visual_design - main_screen.png](..%2FDiagrams%2Fvisual_design%20-%20main_screen.png)
- <span style="color: red;">Upon launching NutriPro, users are greeted by a clean, uncluttered main menu. This screen serves as the central hub of the application, offering three primary options: Search & Compare Foods, Meal Plan, and Exit. Each option is presented as a large, inviting button. <-- this is new
- <span style="color: red;">The simplicity of this design is intentional. By presenting only three core functions, we avoid overwhelming users with choices and instead guide them towards the app's primary features. The generous size of the buttons serves a dual purpose: it makes the options unmissable, even at a glance, and provides large touch targets that enhance usability across devices. <-- this is new
- <span style="color: red;">At the top of the screen, the NutriPro logo stands prominently, reinforcing brand identity and assuring users they're in the right place. <-- this is new

2. <span style="color: red;">**Dataset List (Search and Compare) Screen**

- ![visual_design - search_and_comparison_screen.png](..%2FDiagrams%2Fvisual_design%20-%20search_and_comparison_screen.png)
- <span style="color: red;">The Dataset List screen combines search and comparison functionalities. At the top of the screen is a prominently placed search bar, inviting users to start their query immediately. A "Search" button is placed next to it. <-- this is new
- <span style="color: red;">Below the search bar, results are displayed in a list format. This layout efficiently utilizes screen real estate, allowing users to scan multiple food items quickly. Each row in the list represents a food item, providing key nutritional information. <-- this is new
- <span style="color: red;">To the right of the results, we position a filter panel with options for high protein, low carbs, and low fat. This placement keeps filtering options readily accessible without cluttering the main view. An "Apply Filters" button allows users to activate their selections. <-- this is new
- <span style="color: red;">A comparison section is included, allowing users to select up to three foods for side-by-side comparison. A "Generate Comparison Chart" button transforms the selected data into a visual chart. <-- this is new
- <span style="color: red;">At the bottom of the screen, meal plan options (Breakfast, Lunch, Dinner, Snack) allow users to add selected foods directly to their meal plan. <-- this is new
- <span style="color: red;">Navigation buttons for "Go to Meal Plan" and "Back to Main Menu" ensure easy movement between different sections of the app. <-- this is new

3. <span style="color: red;">**Meal Plan Screen**

- ![visual_design - meal_plan_screen.png](..%2FDiagrams%2Fvisual_design%20-%20meal_plan_screen.png)
- <span style="color: red;">The Meal Planner screen transforms nutritional information into practical, actionable meal plans. The interface includes options to select a specific day and switch between daily and weekly views. <-- this is new
- <span style="color: red;">The main portion of the screen is dedicated to displaying the meal plan, showing foods for different meal times (Breakfast, Lunch, Dinner, Snack). <-- this is new
- <span style="color: red;">A nutritional summary is displayed, showing total calories, protein, carbs, and fat for the current view (daily or weekly). <-- this is new
- <span style="color: red;">Control buttons at the bottom of the screen allow users to add food, change food, remove food, and clear the meal plan. A "Generate Meal Plan" button enables automatic creation of a balanced meal plan. <-- this is new
- <span style="color: red;">Navigation buttons for "Back to Main Menu" and "Go to Data List" provide easy movement between different sections of the app. <-- this is new

4. <span style="color: red;">**Select Food Screen/Supplementary Screen**

- ![visual_design - supplementary_search__screen.png](..%2FDiagrams%2Fvisual_design%20-%20supplementary_search__screen.png)
- <span style="color: red;">The Select Food screen provides a focused interface for searching and selecting individual food items. <-- this is new
- <span style="color: red;">At the top of the screen, there's a search bar labeled "Search for Food:" which allows users to input their food query. <-- this is new
- <span style="color: red;">A "Search" button is prominently placed next to the search bar, enabling users to initiate their search. <-- this is new
- <span style="color: red;">Below the search area, a list control displays the search results. This list shows multiple columns of information about each food item, allowing users to see key nutritional data at a glance. <-- this is new
- <span style="color: red;">A scroll bar on the right side of the list allows users to navigate through longer lists of search results. <-- this is new
- <span style="color: red;">At the bottom of the screen, a "Select Food" button allows users to confirm their selection and add the chosen food to their meal plan or comparison. <-- this is new
- <span style="color: red;">This screen's focused design helps users quickly find and select specific food items without distraction from other application features. <-- this is new

Throughout the design process, our focus remains on creating an interface that is not just functional, but also engaging and empowering. By presenting complex nutritional information in an accessible, interactive format, NutriPro aims to make the journey of nutritional discovery and meal planning both informative and enjoyable.

---