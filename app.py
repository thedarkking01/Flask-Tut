from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss

# My App
app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='static')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)