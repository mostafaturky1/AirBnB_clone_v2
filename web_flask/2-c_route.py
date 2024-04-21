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
    return ("c" + " " + text)


if __name__ == "__main__":
    HBNB.run()
