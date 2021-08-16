from time import get_time_string
from flask import Flask

app = Flask(__name__)


@app.route("/")
def show_time():
    '''
    Fetch Moscow time string and display it in a paragraph
    '''
    time = get_time_string('Europe/Moscow')
    return f"<p>{time}</p>"
