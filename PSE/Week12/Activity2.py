from flask import Flask, url_for
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

@app.route('/link')
def link():
    image_url = url_for('static', filename='images/jpg_blue.jpg')
    return f'''
        <h1>This is a link to the Yoobee website</h1>
        <a href="https://www.yoobee.ac.nz/" target="_blank">
            <img src="{image_url}" alt="Blue JPG image" width="300" loading="lazy">
        </a>
    '''

if __name__ == '__main__':
    app.run(debug = True)


