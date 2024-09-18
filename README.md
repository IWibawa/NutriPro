# Group-Repo

## Nutritional Food Database Analysis and Visualization Tool

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
ANY UPDATES PLACE HERE. 
Check the Section in Software Document (Detailed Design - Section3) for you psudo code section to complete and create. 

Ogi - 2, 3, 5 
Kate - 1, 4, 9
Naveen - 6, 7, 8



### Project Overview

The Nutritional Food Database Analysis and Visualization Tool is a desktop application designed to empower users with comprehensive nutritional information and analysis capabilities. This software aims to address the challenge of making informed dietary choices by providing an intuitive interface for exploring and understanding nutritional data.

Key features include:
1. Food search functionality with detailed nutritional information display
2. Interactive visualization of nutrition breakdowns using pie charts and bar graphs
3. Advanced filtering options based on nutritional content ranges and levels
4. Side-by-side comparison of multiple food items
5. Personalized meal planning based on user-defined nutritional goals and preferences

The application utilizes the Comprehensive Nutritional Food Database, offering detailed nutritional information for a wide range of food items. It's designed to cater to health-conscious individuals, dieters, nutritionists, and dietitians, providing a powerful tool for dietary analysis and decision-making.

Our team is developing this tool as part of a group project, focusing on creating a user-friendly, efficient, and informative application that can significantly impact users' understanding of their dietary choices.
### Team Members
- MadH3r3K8 [Kate]
- IWibawa [Ogi]
- narakkal-nelson [Naveen]

### Project Structure
- `Project Plan.md`: Detailed plan for the project development
- `Software Design Document.md`: Comprehensive design specifications
- `README.md`: This file
- `Diagrams/`: Folder containing all project diagrams and charts

### Recent Updates
- Reorganized project structure: Moved all diagrams to a dedicated "Diagrams" folder
- Updated Project Plan to align with the latest Software Design Document
- Revised Software Design Document 
- Implemented Work Breakdown Structure (WBS)
- Continuous updates to Project Plan and Software Design Document

### Development Process
Our team is following an iterative development process, with regular updates to project documentation and design artifacts. We're using Git for version control, with all team members contributing to various aspects of the project.

---

# 1. Introduction

The group project consists of two milestones:

- **Milestone 1**: Project Management
- **Milestone 2**: Data Analysis and Visualisation

The primary goal of Milestone 2 in the group project is to use **wxPython** and **wxFormBuilder** to develop a desktop application, specifically a simple data analysis and visualisation tool for the provided database. Your team designed this software in Milestone 1, and now, in Milestone 2, you will begin implementing it. Ensure that the software is not only functional but also user-friendly and thoroughly tested to enhance its overall quality and reliability.

All work must be hosted on the same GitHub repository created in Milestone 1 with access restricted to your group members. Download **Milestone_2.zip**, unzip it, and upload the contents to your group GitHub repository. Your team has to use the same guide **Group_Project_Collaboration_Workflow.pdf**.

Download **Group_Project_Collaboration_Workflow.pdf** provided in Milestone 1 to collaborate on the group project and synchronize the code.

This repository will have a track record of regular commits, showcasing the incremental and collaborative efforts on the project. All project resources (python code, documents, images, and others) should be stored in the GitHub repository.

---

# 2. Files Required for Submission

Please note that late submissions will be marked according to Griffith University’s assessment policy. **5% of the marks will be deducted for each day late**. After 7 days, no submissions will be accepted.

> **You have to use the provided templates, otherwise your team will lose 10 marks.**

> **Only one submission per group is required.**

### Files Required for Submission:

Please upload each required file individually; compressed files in .zip format are not accepted.

- **GUI.fbp**
  - The project file created by wxFormbuilder.
- **GUI.pdf**
  - Include screenshots of GUI.fbp showing only the Object Tree and the Designer.
  - Ensure they are visually articulated, as demonstrated in the provided GUI.pdf.
- **Executive_Summary.md** and **Executive_Summary.pdf** *(Refer to Milestone_2.zip)*.
- **Unit_Testing_Report.md** and **Unit_Testing_Report.pdf** *(Refer to Milestone_2.zip)*.
- **Coverage_Testing_Report.md** and **Coverage_Testing_Report.pdf** *(Refer to Milestone_2.zip)*.
- **Project_Plan.md** and **Project_Plan.pdf**
  - An updated project plan document.
  - Please ensure that any updates to the text are highlighted in **red font**.
  - Please provide a description in **red font** for any updates made to the images.
- **Software_Design_Document.md** and **Software_Design_Document.pdf**
  - An updated software design document.
  - Please ensure that any updates to the text are highlighted in **red font**.
  - Please provide a description in **red font** for any updates made to the images.
- **Gantt_chart.xlsx**
  - An updated separate Gantt chart.
  - You should embed the screenshot (as an image) of this in your **Project_Plan.md**.
- **git_log.txt**
  - 10 marks will be deducted for not providing the git_log.txt file.
  - You have to use this command to produce the git_log.txt:
    ```
    git log --oneline --graph --decorate --pretty=format:"%h %ad by [%an] | %s%d" --date=short > git_log.txt
    ```
- All **.py** files and their corresponding **.txt** files.
  - Create a .txt for each .py file by copying and pasting the code for plagiarism review.
- Other resources
  - Such as images/screenshots in png/bmp/jpg formats.

# Submission Instructions:

1. Scroll to the bottom of the page. **Upload** will be pre-selected.
2. Follow the prompts to upload your file.
3. Tick **I agree** to indicate the submission is your own work.
4. Click **Submit Assignment**.

---

what change from the original software doc:
# 1. Overall Structure:
**Original Design Document:**
- 8 separate Python files: 4 frame files and 4 logic files.

**Current Implementation:**
- 4 frame files and 4 corresponding logic files, plus a central `main.py` file coordinating the application.

**Notable Changes:**
- Consolidation into fewer files, with `main.py` coordinating the logic and maintaining instances of the frames, which deviates from the original approach of using 8 separate files.
- This consolidation helps in better handling navigation and avoids recreating frame instances unnecessarily.

# 2. Main Navigation and Application Logic:
**Original Design Document:**
- No clear mention of how navigation between frames was to be handled.

**Current Implementation (`main.py`):**
- `MainApp` class manages the frames, allowing smooth transitions between them (e.g., from meal plan to dataset list).
- Functions like `show_dataset_list()` and `show_meal_plan()` manage navigation.

**Notable Changes:**
- The centralized navigation and frame management system using the `MainApp` class was a design improvement not explicitly outlined in the original document.
- The ability to avoid recreating frames on each navigation action is a new addition, improving efficiency.

# 3. Dataset Handling:
**Original Design Document:**
- Likely implied a simple food dataset without specifications on how it would be managed.

**Current Implementation:**
- Dataset loaded using `pandas` for efficient handling and filtering (seen in both `DatasetListLogic.py` and `FoodSearchDialogLogic.py`).
- Data is filtered and searched using `pandas`, with conditions for specific nutritional values (e.g., filtering by protein, carbs, fat).
- Dataset displayed in a `ListCtrl` for easier comparison and selection.

**Notable Changes:**
- The use of `pandas` to handle the food dataset and perform data type conversion for nutritional values is a significant change.
- The `initialize_list_controls()` method dynamically sets up the columns for food lists, which was not detailed in the original design.

# 4. Meal Plan Management:
**Original Design Document:**
- Likely a simple meal plan system without detailed mechanisms for adding, removing, and modifying food.

**Current Implementation (`MealPlanFrameLogic.py`):**
- The `MealPlanManager` class tracks meals by day and meal time (Breakfast, Lunch, Dinner, Snack).
- `generate_balanced_meal()` method added for generating a well-balanced meal plan for the week using the dataset.
- Added logic for filtering cooked/whole meals using keywords like "cooked," "baked," etc. This logic ensures that the meal plan generation avoids individual ingredients.

**Notable Changes:**
- Random meal generation for the entire week, based on caloric and macronutrient targets, was not part of the original design.
- The addition of filtering logic for cooked foods represents a significant refinement from the original design, ensuring the selection of appropriate meals.

# 5. Food Search and Selection:
**Original Design Document:**
- Expected a basic food search system.

**Current Implementation (`FoodSearchDialogLogic.py`):**
- Implements search functionality using `pandas` to filter foods by name and bind them to search results.
- The selected food is stored as a dictionary with nutritional information, ensuring accurate meal plan addition.

**Notable Changes:**
- The use of `pandas` to search the dataset by food names is a significant improvement over any simpler string matching system that might have been expected in the original design.

# 6. Visual Design and GUI Changes:
**Original Design Document:**
- Presumed basic navigation between frames with buttons but no clear specification on visual structure.

**Current GUI:**
- The GUI design includes various buttons for navigation and interaction:
  - **Main Menu**: Contains "Search & Compare Foods," "Meal Plan," and "Exit" buttons.
  - **Dataset List Frame**: Includes filters, a comparison chart generator, and an option to add food to the meal plan.
  - **Meal Plan Frame**: Allows switching between daily and weekly views and generating meal plans.

**Notable Changes:**
- Improved interaction with the user, allowing more robust filtering options (e.g., high protein, low carbs) and comparison charts.
- GUI components like `ListCtrl` for showing food items and comparison charts are more sophisticated than the presumed original design.
- The back navigation to the main menu, direct navigation to the meal plan from the dataset list, and daily/weekly views are useful additions not mentioned in the original document.

# 7. Error Handling and Warnings:
**Original Design Document:**
- No details on error handling.

**Current Implementation:**
- Warnings for wxPython deprecation are suppressed in `main.py`.
- Error handling during dataset loading, including displaying error messages if the dataset fails to load.

**Notable Changes:**
- The robust error handling and suppression of wxPython deprecation warnings were not originally planned, but they improve user experience and application reliability.

# 8. Data Management and Calculations:
**Original Design Document:**
- No mention of specific data management techniques.

**Current Implementation:**
- The system uses `pandas` to manage the food dataset, ensuring that all nutritional values are properly converted to floats for accurate calculations.
- Nutritional summaries are calculated dynamically and updated in the meal plan view.

**Notable Changes:**
- The transition to using `pandas` for managing the dataset and performing accurate nutritional calculations represents a major enhancement over the presumed simpler data management system.

# Conclusion:
Your current implementation significantly improves upon the original design in terms of efficiency, functionality, and user experience. The following key differences were noted:

- Centralized navigation system using `MainApp`.
- More robust dataset handling with `pandas`.
- Randomized meal plan generation based on nutritional targets.
- Filtering of cooked/whole foods to ensure appropriate meal selection.
- Enhanced visual design and GUI components, including filters, comparison charts, and direct navigation.

If you’d like to explore further adjustments or need help with any specific part of the application, feel free to ask!
