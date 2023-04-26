#!/usr/bin/python3
"""A script that runs flask"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>/')
def number(n):
    """a route to display an integer"""
    return "{} is a number".format(n)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text="is cool"):
    """a route with default parameter"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number_template/<int:n>/')
def number_template(n):
    """route returns number in template"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
