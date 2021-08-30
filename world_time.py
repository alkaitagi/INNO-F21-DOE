import requests
from datetime import datetime


def get_time_string(place: str = "Europe/Moscow"):
    """
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
    """

    url = "http://worldtimeapi.org/api/timezone/" + place
    data = requests.get(url).json()
    date = datetime.fromisoformat(data["datetime"])
    string = date.strftime("%Y-%m-%d %H:%M:%S")
    return string
