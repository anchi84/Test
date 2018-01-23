"""Flask app."""

# Priprema radnog okruzenja
"""
virtualenv venv
venv\Scripts\activate.bat
pip install -r pips.txt
"""
# Pokretanje aplikacije
"""
venv\Scripts\activate.bat
set FLASK_APP=app.py
flask run
"""

from flask import Flask, render_template
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
    """/comments route handler."""
    return render_template('result.html', array = COMMENTS)

# if __name__ == '__main__':
#    app.run(debug = True)