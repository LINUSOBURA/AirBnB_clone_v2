#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """ Get states sorted by names and render on template """
    states_data = list(storage.all(State).values())

    if id is not None:
        id = 'state.' + id
    return render_template('9-states.html', states=states_data, state_id=id)


@app.teardown_appcontext
def teardown_storage(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
