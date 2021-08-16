from flask import Flask
import requests
from datetime import datetime

API_URL = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
app = Flask(__name__)


@app.route("/")
def show_time():
    data = requests.get(API_URL).json()
    date = datetime.fromisoformat(data["datetime"])
    text = date.strftime('%Y-%m-%d %H:%M:%S')
    return f"<p>{text}</p>"
