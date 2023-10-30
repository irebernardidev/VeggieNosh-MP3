# Import required libraries and modules
import os
from flask import Flask
from flask_pymongo import PyMongo

# Import environment variables if env.py exists
if os.path.exists("env.py"):
   import env

# Initialize Flask app
app = Flask(__name__)

# Config settings using environment variables from env.py
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Setup MongoDB with Flask app
mongo = PyMongo(app)

# Import routes for the app
from veggienosh import routes
