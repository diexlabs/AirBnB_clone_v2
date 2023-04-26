#!/usr/bin/python3
"""A script that runs flask"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """returns the index page of the application"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """a route of the server"""
    return "HBNB"


@app.route('/c/<text>/')
def ctext(text):
    """a route with parameter"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
