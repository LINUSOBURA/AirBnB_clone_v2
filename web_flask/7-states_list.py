#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Get states sorted by names and render on template """
    states_data = sorted(list(storage.all(State).values()),
                         key=lambda x: x.name)
    return render_template('7-states_list.html', states=states_data)


@app.teardown_appcontext
def teardown_storage(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
