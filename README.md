# Labs 1 & 2

This is a simple python web application for displaying current Moscow time on page load. Written in Flask and contained in Docker.

## Installation

Mount the virtual environment and install the packages.

```bash
python -m venv venv
pip install -r requirements.txt
```

## Usage

There are several ways to run the app

```bash
# direct python launch
python main.py

# or running the flask
flask run

# or building the docker image
docker build -t lab2 .
docker run -d -p 5000:5000 lab2
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
