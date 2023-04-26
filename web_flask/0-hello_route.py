#!/usr/bin/python3
"""A script that runs flask"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """returns the index page of the application"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
