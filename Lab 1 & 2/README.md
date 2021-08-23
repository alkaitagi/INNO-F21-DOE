# Labs 1 & 2

This is a simple python web application for displaying current Moscow time on page load. Written in Flask and contained in Docker.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python -m venv venv
pip install -r requirements.txt
```

## Usage

Either run the app directly from the command line:

```bash
python app.py
```

or using the flask command:

```bash
flask run
```

or use the provided Dockerfile:

```bash
docker build -t python-app .
docker run -d -p 5000:5000 python-app
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
