import os
import json

from flask import Flask, jsonify
from world_time import get_time_string

app = Flask(__name__)

FILE_NAME = "/home/app/visits.json"

@app.route("/")
def show_time():
    """
    Fetch Moscow time string and display it in a paragraph
    """
    
    visits = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            visits = json.load(f)
    with open(FILE_NAME, "w") as f:
        json.dump(visits + 1, f)

    time = get_time_string("Europe/Moscow")
    return f"<p>Time in Moscow</p><p>{time}</p>"

@app.route("/visits")
def visit():
    """Sends back the total number of visits to the root endpoint."""
    visits = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            visits = json.load(f)
    return jsonify(visits)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
