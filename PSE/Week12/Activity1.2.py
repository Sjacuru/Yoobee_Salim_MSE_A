from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Activity 1. Hello, Flask!</p>"

@app.route("/lili")
def hello_lili():
    return "<p>Hello, Lili!</p>"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

if __name__ == '__main__':
    app.run(debug = True)


