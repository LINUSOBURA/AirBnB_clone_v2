#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from os import getenv

from flask import Flask, abort, jsonify, render_template
from flask_mysqldb import MySQL
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['MYSQL_HOST'] = getenv('HBNB_MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('HBNB_MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('HBNB_MYSQL_PWD')
app.config['MYSQL_DB'] = getenv('HBNB_MYSQL_DB')

db = MySQL(app)


@app.route("/states_list", strict_slashes=False)
def states():
    cur = db.connection.cursor()
    cur.execute('SELECT states.id, states.name FROM states')
    data = cur.fetchall()
    states_list = [{'id': row[0], 'name': row[1]} for row in data]
    cur.close()
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
