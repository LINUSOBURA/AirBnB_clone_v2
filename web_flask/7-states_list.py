#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from os import getenv

from flask import Flask, abort, jsonify, render_template
from flask_mysqldb import MySQL
from models import storage
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['MYSQL_HOST'] = getenv('HBNB_MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('HBNB_MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('HBNB_MYSQL_PWD')
app.config['MYSQL_DB'] = getenv('HBNB_MYSQL_DB')

db = MySQL(app)


def get_states():
    return storage.all("state").values()


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    cur = db.connection.cursor()
    cur.execute('SELECT states.id, states.name FROM states')
    data = cur.fetchall()
    states_list = [{'id': row[0], 'name': row[1]} for row in data]
    cur.close()
    return render_template('7-states_list.html', states_list=states_list)


@app.route('/test')
def test():
    states_data = get_states()
    return render_template('7-states_list.html', states=states_data)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
