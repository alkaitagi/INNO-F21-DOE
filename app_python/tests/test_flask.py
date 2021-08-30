import re
from main import app
from world_time import get_time_string


def test_time():
    time = get_time_string()
    assert re.match(
        r"\d\d/\d\d/\d\d \d\d:\d\d:\d\d",
        time,
    )


def test_index():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert re.match(
            r"<p>Time in Moscow</p><p>\d\d/\d\d/\d\d \d\d:\d\d:\d\d</p>",
            response.data.decode("utf-8"),
        )
