# BMR Calculator and Calorie Tracker

This Python project helps you calculate your Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation and keep track of your daily calorie intake by logging it in a CSV file. The application allows users to store daily calorie consumption and retrieve historical data based on the date.

## Features

- Calculate BMR using the Mifflin-St Jeor equation.
- Log daily calories consumed along with the date.
- Append data to an existing CSV file (`calories_data.csv`).
- Search for calorie entries by date.
- Calculate the total calories consumed for any specific date.
<img width="1138" alt="Screenshot 2024-10-04 at 19 11 33" src="https://github.com/user-attachments/assets/194ae864-6495-4baf-ad70-ccf630a06a18">

## Requirements

- Python 3.x
- Libraries: `Flask`, `csv`, `datetime`, `os`, `re`

## Application Implementation

This project is implemented as a Flask web application. The user interface allows users to enter their weight, height, age, gender, and daily calorie consumption through web forms. 

### Application Structure

- **index.html**: Main form for entering weight, height, age, gender, and calories.
- **search.html**: Form for searching calorie entries by date.
- **search_results.html**: Displays search results and allows users to navigate back to the home page or search for another date.
- **results.html**: Displays BMR calculation and allows users to enter new data or search for another date
- **global.css**: Contains all the styling for the HTML pages.

### How to Run the Flask App

1. **Set Up Your Environment**: 
   - Ensure that you have Python 3.x installed on your system.
   - Install the required libraries using pip:

     ```bash
     pip install Flask
     ```

2. **Clone or Download the Repository**: 
   - Clone this repository or download the source code to your local machine.

3. **Navigate to Your Project Directory**: 
   - Open your command line interface and change to the directory where your Flask application file (e.g., `app.py`) is located:

     ```bash
     cd path/to/your/project
     ```

4. **Set Environment Variables**:
   - Set the `FLASK_APP` environment variable to your application file. For example:

     - **On Windows (Command Prompt)**:

       ```bash
       set FLASK_APP=app.py
       ```

     - **On macOS/Linux**:

       ```bash
       export FLASK_APP=app.py
       ```

5. **Run the Flask Application**:
   - Execute the following command:

     ```bash
     flask run
     ```

6. **Access Your Application**:
   - Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

### BMR Calculation

The program uses the Mifflin-St Jeor equation to calculate the BMR:
- For males:  
  `BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) + 5`
- For females:  
  `BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) - 161`

### CSV File Format

The CSV file (`calories_data.csv`) stores data in the following format:

| Date       | Calories |
|------------|----------|
| 01-10-2024 | 1800     |
| 02-10-2024 | 2000     |

## Functions

### `get_date()`
Returns today's date in a `datetime` object.

### `date_to_str(date)`
Converts a date object to a string in the format `dd-mm-yyyy`.

### `is_valid_date_format(date_str)`
Verifies that the inputted date is in the correct format 

### `bmr_mifflin_st_jeor(weight_kg, height_cm, age, gender)`
Calculates BMR based on the Mifflin-St Jeor formula.

### `search_in_csv(file_path, search_string)`
Searches for a string (typically a date) in the CSV file and prints the matching rows.

### `load_calorie_data(file_path)`
Loads calorie data from the CSV file into a dictionary where the key is the date, and the value is the sum of calories.

### `get_total_calories_for_date(calorie_data, date)`
Retrieves the total calorie count for a given date.

## Error Handling

- If the CSV file doesn't exist, the program will create it.
- If the user enters an invalid gender, the program raises a `ValueError`.
