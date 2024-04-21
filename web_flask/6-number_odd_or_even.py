#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask, render_template

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


@HBNB.route('/number_template/<int:n>', strict_slashes=False)
def render_HBNB(n):
    """Displays 'python <text>'"""
    return render_template('5-number.html', number=n)


@HBNB.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOreven_HBNB(n):
    """Displays 'even ot odd'"""
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html',
                           number=n, result=result)


if __name__ == "__main__":
    HBNB.run()
