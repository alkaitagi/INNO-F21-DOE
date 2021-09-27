# DevOps Engineering labs

![Python](https://github.com/alkaitagi/INNO-F21-DOE/actions/workflows/python.yml/badge.svg)
![Docker](https://github.com/alkaitagi/INNO-F21-DOE/actions/workflows/docker.yml/badge.svg)

This is a simple python web application for displaying current Moscow time on page load. Written in Flask and contained in Docker.

## Installation

Mount the virtual environment and install the packages.

```bash
python -m venv venv
pip install -r requirements.txt
```

## Usage

There are several ways to run the app:

```bash
# direct python launch
python main.py

# or running the flask
flask run

# or building the docker image
docker build -t inno-f21-doe:latest .
docker run -d -p 5000:5000 inno-f21-doe:latest
```

## Endpoints

- `/`: Displays the current time in Moscow.
- `/visits`: Displays the number of visits to the app.

## Testing

Unit tests are present:

```bash
python -m pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
