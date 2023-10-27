# Import required libraries, modules, and forms
from flask import render_template, url_for, flash, redirect, request, session
from veggienosh import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from veggienosh.forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# MongoDB Collections Initialization
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# Landing Page Route
@app.route('/')
@app.route("/home")
def home():
    """Landing page route."""
    return render_template('home.html', title='Home', recipes=recipes_coll.find())

# Route to Display All Recipes
@app.route('/all_recipes')
def all_recipes():
    """Display all recipes route."""
    return render_template("all_recipes.html", recipes=recipes_coll.find(), title='All Vegan Recipes')

# User Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    """User login route."""
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':  # This is a placeholder; real apps should validate against the database
            flash('Welcome back, vegan chef! You have successfully logged in.')
            return redirect(url_for('home'))
        else:
            flash('Oops! Your credentials seem to be stir-fried. Please try again.')
    return render_template('login.html', form=form, title='Login')

# User Registration Route
@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user:
            flash("Oh snap! That username is already taken. Maybe try something more flavorful?")
            return redirect(url_for('register'))
        else:
            hashed_password = generate_password_hash(request.form['password'])
            new_user = {
                "username": request.form['username'],
                "password": hashed_password,
                "user_recipes": [],
            }
            users_coll.insert_one(new_user)
            session["username"] = request.form['username']
            flash(f'Welcome to the VeggieNosh family! Your account is ready to simmer.')
            return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Join VeggieNosh')


@app.route("/logout")
def logout():
    session.pop("username",  None)
    return redirect(url_for("home"))
