#!/usr/bin/python3
"""a script that starts a Flask web application:"""


from flask import Flask

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
def index_c(text):
    """a function to return C is fun"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
