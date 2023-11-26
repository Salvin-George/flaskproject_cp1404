from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/determine_temperature')
@app.route('/determine_temperature/<temperature>')
def determine_temperature(temperature=None):
    if temperature is not None:
        fahrenheit = float(temperature) * 9.0 / 5 + 32
        return f"Fahrenheit: {str(fahrenheit)}"
    else:
        return "Temperature not provided."

if __name__ == '__main__':
    app.run()
