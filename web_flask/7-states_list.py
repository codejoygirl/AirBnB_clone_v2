#!/usr/bin/python3
"""Script to start a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
import sys
import os

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the AirBnB_clone_v2 directory to the Python path
AirBnB_clone_v2_directory = os.path.join(current_directory, "..")
sys.path.append(AirBnB_clone_v2_directory)

app = Flask(__name__)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
