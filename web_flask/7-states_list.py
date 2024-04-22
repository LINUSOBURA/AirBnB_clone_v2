#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from os import getenv

from flask import Flask, abort, jsonify, render_template
from models import storage

app = Flask(__name__)


def get_states():
    return storage.all()


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    states_data = get_states()
    return render_template('7-states_list.html', states=states_data)


@app.route("/states", strict_slashes=False)
def test():
    states_data = get_states()
    return list(states_data)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
