from flask import Flask
from word_time import get_time_string

app = Flask(__name__)


@app.route("/")
def show_time():
    '''
    Fetch Moscow time string and display it in a paragraph
    '''
    time = get_time_string('Europe/Moscow')
    return f"<p>Time in Moscow: {time}</p>"
