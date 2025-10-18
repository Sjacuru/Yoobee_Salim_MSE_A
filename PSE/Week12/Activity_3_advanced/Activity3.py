from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def converter():
    result = None
    from_unit = to_unit = value = None

    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_temperature(value, from_unit, to_unit)
        except ValueError:
            result = "Invalid input. Please enter a numeric value."

    return render_template('index.html', result=result, value=value, from_unit=from_unit, to_unit=to_unit)


def convert_temperature(value, from_unit, to_unit):
    # Normalize input (make sure we only convert if different units)
    if from_unit == to_unit:
        return value

    # Convert input to Celsius first
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        celsius = value - 273.15
    else:
        return "Invalid unit"

    # Convert Celsius to target unit
    if to_unit == 'Celsius':
        return round(celsius, 2)
    elif to_unit == 'Fahrenheit':
        return round((celsius * 9/5) + 32, 2)
    elif to_unit == 'Kelvin':
        return round(celsius + 273.15, 2)
    else:
        return "Invalid unit"


if __name__ == '__main__':
    app.run(debug=True)
