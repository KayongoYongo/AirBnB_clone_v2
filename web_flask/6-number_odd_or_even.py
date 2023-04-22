#!/usr/bin/python3
"""a script that starts a Flask web application:"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """The function returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """a function to return HBNB"""
    return "HBNB"


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c_is_fun(text):
    """a function to return C is fun"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def display_number(n):
    """displays only when a number is passed on the url"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_html_variables(n):
    """renders html page with variables"""
    if n % 2 == 0:
        is_odd_or_even = "even"
    else:
        is_odd_or_even = "odd"

    return render_template("6-number_odd_or_even.html", p=n, m=is_odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
