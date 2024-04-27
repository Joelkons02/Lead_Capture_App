import os

class Config:
    SECRET_KEY = 'your_secret_key'  # Replace with a random secret key

    # MySQL database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://app_user:your_password@localhost/lead_capture_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
