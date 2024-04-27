from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after initializing app
from app import routes
