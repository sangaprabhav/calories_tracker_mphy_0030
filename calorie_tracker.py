import csv
import datetime
import os

# Function to get today's date
def get_date():
    return datetime.date.today()

# Function to convert date object to string
def date_to_str(date):
    return date.strftime('%d-%m-%Y')

# Function to convert string back to date object
def str_to_date(str):
    day, month, year = str.split('-')
    return datetime.date(int(year), int(month), int(day))

def bmr_mifflin_st_jeor(weight_kg, height_cm, age, gender):
    if gender == 'male':
        bmr_m = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
        return bmr_m
    elif gender == 'female':
        bmr_f = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
        return bmr_f
    else:
        raise ValueError("Gender should be either 'male' or 'female'")


weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cm: "))
age =    int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ").lower()

filename = 'calories_data.csv'

# Writing initial data to the CSV file if it doesn't exist
if not os.path.isfile(filename):
    data = [["Date", "Calories"]]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Append today's date and the calories entered by the user
date = date_to_str(get_date())
calories = input('Enter the number of calories you consumed today: ')

# Open the CSV file in append mode and add the new date and calories
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([date, bmr_mifflin_st_jeor(weight, height, age, gender)-int(calories)])

print("YOUR BMR IS: ",bmr_mifflin_st_jeor(weight, height, age,gender))

import csv

# Function to search for a string in the CSV and print matching rows
def search_in_csv(file_path, search_string):
    # Open the CSV file for reading
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        # Loop through each row in the CSV
        for row in reader:
            # Check if the search string is found in any element of the row
            if any(search_string in column for column in row):
                print(row)

# Function to load CSV data into a dictionary and sum calories for each date
def load_calorie_data(file_path):
    calorie_data = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header if there is one
            for row in reader:
                date, calories = row
                if date in calorie_data:
                    calorie_data[date] += float(calories)  # Sum calories for the same date
                else:
                    calorie_data[date] = float(calories)
    except FileNotFoundError:
        pass  # Handle missing file scenario
    return calorie_data

# Function to get total calories for a specific date
def get_total_calories_for_date(calorie_data, date):
    # Retrieve the total calories for the specified date, return 0 if not found
    return calorie_data.get(date, 0)

# Example usage:
file_path = 'calories_data.csv'
date_search = input("Enter the date you want to search: ")

# Search for the date in the CSV and print the matching rows
search_in_csv(file_path, date_search)

# Load calorie data from the CSV and print total calories for the specific date
calorie_data = load_calorie_data(file_path)
total_calories = get_total_calories_for_date(calorie_data, date_search)
print(f"Total calories for {date_search}: {total_calories}")



