#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

HBNB = Flask(__name__)


@HBNB.route("/", strict_slashes=False)
def hello_HBNB():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@HBNB.route("/hbnb", strict_slashes=False)
def hbnb_HBNB():
    """Displays 'HBNB'"""
    return "HBNB"


@HBNB.route("/c/<text>", strict_slashes=False)
def c_HBNB(text):
    """Displays 'HBNB'"""
    text = text.replace("_", " ")
    return ("C" + " " + text)


@HBNB.route("/python", strict_slashes=False)
@HBNB.route("/python/<text>", strict_slashes=False)
def Python_HBNB(text="is cool"):
    """Displays 'python <text>'"""
    text = text.replace("_", " ")
    return ("Python" + " " + text)


@HBNB.route('/number/<int:n>', strict_slashes=False)
def Number_HBNB(n):
    """Displays 'python <text>'"""
    return f"{n} is a number"


if __name__ == "__main__":
    HBNB.run()
