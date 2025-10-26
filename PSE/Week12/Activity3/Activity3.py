from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get form data from query parameters
    temp = request.args.get('temp')
    from_ = request.args.get('from_unit')
    to_ = request.args.get('to_unit')
    result = None

    if temp and from_ and to_:
        temp = float(temp)
        if from_ == 'Celsius' and to_ == 'Fahrenheit':
            result = (temp * 9/5) + 32
        elif from_ == 'Fahrenheit' and to_ == 'Celsius':
            result = (temp - 32) * 5/9
        elif from_ == 'Celsius' and to_ == 'Kelvin':
            result = temp + 273.15
        elif from_ == 'Kelvin' and to_ == 'Celsius':
            result = temp - 273.15
        elif from_ == 'Fahrenheit' and to_ == 'Kelvin':
            result = (temp - 32) * 5/9 + 273.15
        elif from_ == 'Kelvin' and to_ == 'Fahrenheit':
            result = (temp - 273.15) * 9/5 + 32

    return render_template('index.html', result=result)
    

if __name__ == '__main__':
    app.run(debug=True)
