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

http://127.0.0.1:5000/
http://127.0.0.1:5000/comments
http://127.0.0.1:5000/api/v1.0/comments
"""

from flask import Flask, render_template, jsonify
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

@app.route('/api/v1.0/comments', methods=['GET'])
def api_comments():
    """Handle HTTP GET Request for the comments API endpoint."""
    result = []
    for comment in COMMENTS:
        comment_dict = {
            "TEXT": comment.text,
            "DATE": comment.date
        }
        result.append(comment_dict)
    return jsonify({'comments': result}) # ovo zahteva da je uradjeno `from flask import jsonify`