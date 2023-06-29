from app import app, db
from flask import render_template

@app.route('/')
def home():
    return render_template('base.html')