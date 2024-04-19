#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

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
    number = int(n)
    if isinstance(number, int):
        return f"{n} is a number"


if __name__ == "__main__":
    ##app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
