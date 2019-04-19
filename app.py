from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# import click

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
