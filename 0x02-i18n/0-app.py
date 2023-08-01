#!/usr/bin/env python3
"""
Flask App - Basic

This module sets up a basic Flask app with a single route.
The route renders an index.html template with the title and header.

Usage:
    Run this script to start the Flask app.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Index route handler.

    Returns:
        str: The HTML content to display on the page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=3000)
