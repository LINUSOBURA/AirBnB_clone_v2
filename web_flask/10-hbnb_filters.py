#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def state_cities_list():
    """ Get states sorted by names and render on template """
    states_data = list(storage.all(State).values())
    amenity_data = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           states=states_data,
                           amenities=amenity_data)


@app.teardown_appcontext
def teardown_storage(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
