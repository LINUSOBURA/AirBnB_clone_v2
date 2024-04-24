#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    mod_text = text.replace('_', ' ')
    return "C " + mod_text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': None}, strict_slashes=False)
def py_text(text):
    if text is not None:
        mod_text = text.replace('_', ' ')
        return "Python " + mod_text
    else:
        return "Python is cool"


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    try:
        number = int(n)
        return "{} is a number".format(number)
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    try:
        number = int(n)
        return render_template('5-number.html', number=number)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_even(n):
    try:
        number = int(n)
        if number % 2 == 0:
            number_t = "even"
        else:
            number_t = "odd"
        return render_template('6-number_odd_or_even.html',
                               number=number,
                               number_t=number_t)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
