from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)


def get_time_string(place: str = 'Europe/Moscow'):
    '''
    Get time data from worldtimeapi.org and return simple string

    Parameters
    ----------
    place : str
        Location, i.e. 'Europe/Moscow'.

    Returns
    -------
    string
        Time in format '%Y-%m-%d %H:%M:%S'

    Examples
    --------
    >>> get_time_string()
    2021-08-16 16:03:34
    '''

    url = "http://worldtimeapi.org/api/timezone/"+place
    data = requests.get(url).json()
    date = datetime.fromisoformat(data["datetime"])
    string = date.strftime('%Y-%m-%d %H:%M:%S')
    return string


@app.route("/")
def show_time():
    '''
    Fetch Moscow time string and display it in a paragraph
    '''
    time = get_time_string('Europe/Moscow')
    return f"<p>{time}</p>"
