from flask import Flask, flash, render_template, request, redirect, url_for
from helpers import bmr_mifflin_st_jeor, date_to_str, get_date, is_valid_date_format, load_calorie_data, get_total_calories_for_date
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        calories = int(request.form['calories'])
        
        # Calculate BMR
        bmr = bmr_mifflin_st_jeor(weight, height, age, gender)
        
        # Append today's date and calorie data to CSV
        filename = 'calories_data.csv'
        date = date_to_str(get_date())

        if not os.path.isfile(filename):
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Calories"])

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, calories])  # Save the actual calories consumed, not the difference.

        return redirect(url_for('result', bmr=bmr, calories=calories))

    return render_template('index.html')

# Route to display results
@app.route('/result')
def result():
    bmr = float(request.args.get('bmr'))
    calories = int(request.args.get('calories'))
    return render_template('results.html', bmr=bmr, calories=calories)

# Route to search for a specific date
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_date = request.form['date_search']

        # Check if the date format is valid
        if not is_valid_date_format(search_date):
            flash(f"Invalid date format. Please use dd-mm-yyyy format.")
            return redirect(url_for('search'))

        # Load calorie data from the CSV
        calorie_data = load_calorie_data('calories_data.csv')

        # Get total calories for the specific date
        total_calories = get_total_calories_for_date(calorie_data, search_date)

        # Render the result page with search result or no result
        return render_template('search_results.html', total_calories=total_calories, search_date=search_date)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
