from flask import Flask, request, render_template

app = Flask(__name__)

# Route for displaying the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and calculation
@app.route('/calculate', methods=['POST'])
def calculate_efficiency():
    try:
        # Get form inputs
        area = float(request.form['area'])
        sunlight_hours = float(request.form['sunlight'])
        efficiency = float(request.form['efficiency']) / 100  # Convert percentage to decimal
        power_output = float(request.form['power'])

        # Validate inputs
        if area <= 0 or sunlight_hours <= 0 or efficiency < 0 or power_output <= 0:
            return "All inputs must be positive numbers."

        # Calculate energy output (kWh/day)
        energy_output = area * sunlight_hours * power_output * efficiency

        # Display the result
        return f"The estimated energy output is {energy_output:.2f} kWh per day."
    except ValueError:
        return "Please enter valid numbers for all inputs."

if __name__ == '__main__':
    app.run(debug=True)
