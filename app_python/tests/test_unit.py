import re
from main import app
from world_time import get_time_string

rtime = r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d"


def test_time():
    '''
    Check that the time is in the right format.
    '''
    time = get_time_string()
    assert re.match(rtime, time)


def test_index():
    '''
    Check that the index html is correct.
    '''
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert re.match(
            rf"<p>Time in Moscow</p><p>{rtime}</p>",
            response.data.decode("utf-8"),
        )
