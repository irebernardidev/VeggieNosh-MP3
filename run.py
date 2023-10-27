# Import necessary libraries and modules
import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm

# Check for environment file and import
if os.path.exists("env.py"):
    import env

# Create Flask application instance
app = Flask(__name__)

# Configuration settings from environmental variables
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Create MongoDB instance
mongo = PyMongo(app)

# Define MongoDB Collections
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# Define route for landing page
@app.route('/')
@app.route("/home")
def home():
    """Landing page route."""
    return render_template('home.html', title='Home')

# Define route to display all recipes
@app.route('/all_recipes')
def all_recipes():
    """Display all recipes route."""
    return render_template("all_recipes.html", recipes=recipes_coll.find(), title='Recipes')

# Define login route
@app.route("/login")
def login():
    """Login route."""
    return render_template('login.html', title='Login')

# Define registration route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

# Main driver function
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
