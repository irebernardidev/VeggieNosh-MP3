# Import required libraries, modules, and forms

from flask import Flask, render_template, url_for, flash, redirect
from veggienosh import app
from veggienosh import mongo
from veggienosh.forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# Define MongoDB collections
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# Define routes
@app.route('/')
@app.route("/home")
def home():
    """Landing page route."""
    return render_template('home.html', title='Home', recipes=recipes_coll.find())

@app.route('/all_recipes')
def all_recipes():
    """Display all recipes route."""
    return render_template("all_recipes.html", recipes=recipes_coll.find(), title='Recipes')

@app.route("/login", methods=['GET', 'POST'])
def login():
    """Login route."""
    form = LoginForm()
    if form.validate_on_submit():
        # Check credentials (This is just a placeholder; real apps should validate against the database)
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been successfully logged in!')
            return redirect(url_for('home'))
        else:
            flash('Username or password is incorrect. Please try again')
    return render_template('login.html', form=form, title='Login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Registration route."""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Placeholder for creating a new user (This should save the user to the database in real apps)
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

