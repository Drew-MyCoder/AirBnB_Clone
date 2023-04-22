#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)
"""flask web app name hasn't been set"""


@app.route('/', strict_slashes=False)
def index():
    """message to be printed!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """message to be printed"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
"""value of c text"""
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
"""value of python text"""
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
"""number dispay"""
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
