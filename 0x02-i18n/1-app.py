#!/usr/bin/env python3
"""
Flask App - Basic

This module sets up a basic Flask app with a single route.
The route renders an index.html template with the title and header.

Usage:
    Run this script to start the Flask app.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def home():
    """ Home route """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
