# Import required libraries, modules, and forms
from flask import render_template, url_for, flash, redirect, request, session
from veggienosh import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from veggienosh.forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# --- MongoDB Collections Initialization ---
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# --- Routes ---

# Landing Page Route
@app.route('/')
@app.route("/home")
def home():
    """Serve the landing page."""
    return render_template('home.html', title='Home', recipes=recipes_coll.find())

# Display All Recipes
@app.route('/all_recipes')
def all_recipes():
    """Serve the page showing all vegan recipes."""
    return render_template("all_recipes.html", recipes=recipes_coll.find(), title='All Vegan Recipes')

# My Recipes Page
@app.route('/my_recipes')
def my_recipes():
    """Serve the user's personal recipe page."""
    return render_template("my_recipes.html", title='My Recipes')

# Add New Recipe
@app.route('/add_recipe')
def add_recipe():
    """Serve the add new recipe page."""
    return render_template("add_recipe.html", title='Add New Vegan Recipe')

# User Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    """User login functionality."""
    # Check if user is already logged in
    if 'username' in session:
        flash('You are already logged in, dear Vegan!')
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        # Fetch the user from database
        registered_user = users_coll.find_one({'username': request.form['username']})

        if registered_user and check_password_hash(registered_user['password'], request.form['password']):
            session['username'] = request.form['username']
            flash('Welcome back to VeggieNosh!')
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials. Please munch on a carrot and try again.')
            return redirect(url_for('login'))

    return render_template('login.html', form=form, title='Login')

# User Registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    """User registration functionality."""
    if 'username' in session:
        flash('You are already registered and logged in!')
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username is already taken
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user:
            flash('This username is already being used by another vegan chef. Please choose another!')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(request.form['password'])
        new_user = {
            "username": request.form['username'],
            "password": hashed_password,
            "user_recipes": []
        }
        users_coll.insert_one(new_user)
        session["username"] = request.form['username']
        flash('Welcome to VeggieNosh! Your account has been created.')
        return redirect(url_for('home'))

    return render_template('register.html', form=form, title='Register')

# User Logout
@app.route("/logout")
def logout():
    """Log the user out and redirect to the homepage."""
    session.pop("username", None)
    flash('You have been logged out. See you soon, Vegan!')
    return redirect(url_for("home"))

# Account Settings
@app.route("/account_settings/<username>")
def account_settings(username):
    """Serve the account settings page."""
    username = users_coll.find_one({'username': session['username']})['username']
    return render_template('account_settings.html', username=username, title='Account Settings')
