

# BMR Calculator and Calorie Tracker

This Python project helps you calculate your Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation and keep track of your daily calorie intake by logging it in a CSV file. The application allows users to store daily calorie consumption and retrieve historical data based on the date.

## Features

- Calculate BMR using the Mifflin-St Jeor equation.
- Log daily calories consumed along with the date.
- Append data to an existing CSV file (`calories_data.csv`).
- Search for calorie entries by date.
- Calculate the total calories consumed for any specific date.

## Requirements

- Python 3.x
- Libraries: `csv`, `datetime`, `os`

## How to Use

1. **Run the Program**: The script will prompt you to enter your weight, height, age, gender, and daily calorie consumption.
2. **Logging Calories**: After calculating your BMR, the program stores today's date and the calories consumed in a CSV file (`calories_data.csv`). If the file doesn't exist, it will create one.
3. **Search Calories by Date**: You can search for your calorie intake for any given date and get the total calories consumed for that day.

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

### Example Usage

1. Run the script and input the required details:
    ```python
    Enter your weight in kgs: 70
    Enter your height in cm: 175
    Enter your age in years: 25
    Enter your gender (male/female): male
    Enter the number of calories you consumed today: 2200
    ```

2. To search for a specific date:
    ```python
    Enter the date you want to search: 01-10-2024
    ```
    The program will display the total calories consumed on that date.

## Functions

### `get_date()`
Returns today's date in a `datetime` object.

### `date_to_str(date)`
Converts a date object to a string in the format `dd-mm-yyyy`.

### `str_to_date(str)`
Converts a string back to a `datetime.date` object.

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


