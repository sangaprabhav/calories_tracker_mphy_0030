import datetime 
import re
import csv

# Function to get today's date
def get_date():
    return datetime.date.today()

# Function to convert date object to string
def date_to_str(date):
    return date.strftime('%d-%m-%Y')

# Function to calculate BMR using Mifflin-St Jeor equation
def bmr_mifflin_st_jeor(weight_kg, height_cm, age, gender):
    if gender == 'male':
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    elif gender == 'female':
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    else:
        raise ValueError("Gender should be either 'male' or 'female'")
    
# Function to validate the date format (dd-mm-yyyy)
def is_valid_date_format(date_str):
    # Regular expression for the date format dd-mm-yyyy
    date_pattern = r"^\d{2}-\d{2}-\d{4}$"
    return re.match(date_pattern, date_str)

# Function to load calorie data from CSV
def load_calorie_data(file_path):
    calorie_data = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                date, calories = row
                if date in calorie_data:
                    calorie_data[date] += float(calories)
                else:
                    calorie_data[date] = float(calories)
    except FileNotFoundError:
        pass
    return calorie_data

# Function to get total calories for a specific date
def get_total_calories_for_date(calorie_data, date):
    return calorie_data.get(date, 0)