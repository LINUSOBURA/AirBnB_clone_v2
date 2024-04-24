#!/usr/bin/python3
"""This module serves a Flask application to display a list of states.

The application retrieves states data from storage, sorts them by name,
and renders them using a template.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Retrieve states data, sort them by name, and render them on a template.

    Returns:
        str: Rendered HTML template with the list of states.
    """
    states_data = sorted(list(storage.all(State).values()),
                         key=lambda x: x.name)
    return render_template('7-states_list.html', states=states_data)


@app.teardown_appcontext
def teardown_storage(exception):
    """Close the storage connection when the application context ends."""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
