"""Flask app."""

from flask import Flask
from models import *

app = Flask(__name__)


@app.route("/")
def index():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Comment</title>
    </head>

    <body>
        <h1>"Welcome!"</h1>
    </body>

    </html>
    """
    return page

@app.route("/comments")
def comments():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Comment</title>
    </head>

    <body>
        {}
    </body>

    </html>
    """
    table = table()
    return page.format(table)