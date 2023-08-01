#!/usr/bin/env python3
"""
Flask App - Basic

This module sets up a basic Flask app with a single route.
The route renders an index.html template with the title and header.

Usage:
    Run this script to start the Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object and store it in a module-level variable 'babel'
babel = Babel(app)


# Create a Config class with available languages
class Config:
    LANGUAGES = ["en", "fr"]


# Configure the Flask app to use the Config class for configuration
app.config.from_object(Config)


@app.route('/')
def index():
    """ Home route """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=3000)
