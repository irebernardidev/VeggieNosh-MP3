import os
from flask import Flask
from flask_pymongo import PyMongo

# Import environment variables if env.py exists
if os.path.exists("env.py"):
    import env

# Initialize Flask app
app = Flask(__name__)

# Config settings using environment variables from env.py
app.config["MONGODB_NAME"] = "veggienosh"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Setup MongoDB with Flask app
mongo = PyMongo(app)

from veggienosh import routes