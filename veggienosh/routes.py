# --- Imports ---
from flask import (render_template, url_for, flash, redirect, 
                   request, session)
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

from veggienosh import app, mongo
from veggienosh.forms import RegisterForm, LoginForm

# --- MongoDB Collections Initialization ---
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# --- Routes ---

@app.route('/')
@app.route("/home")
def home():
    """Serve the landing page."""
    return render_template(
        'home.html', title='Home', recipes=recipes_coll.find())

@app.route('/all_recipes')
def all_recipes():
    """Serve page showing all vegan recipes."""
    return render_template(
        "all_recipes.html", recipes=recipes_coll.find(), title='All Vegan Recipes')

@app.route('/my_recipes')
def my_recipes():
    """Serve the user's personal recipe page."""
    return render_template("my_recipes.html", title='My Recipes')

@app.route('/add_recipe')
def add_recipe():
    """Serve the add new recipe page."""
    return render_template("add_recipe.html", title='Add New Vegan Recipe')

@app.route("/login", methods=['GET', 'POST'])
def login():
    """User login functionality."""
    if 'username' in session:
        flash('You are already logged in, dear Vegan!')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one(
            {'username': request.form['username']})
        
        if (registered_user and 
                check_password_hash(registered_user['password'], 
                                    request.form['password'])):
            session['username'] = request.form['username']
            flash('Welcome back to VeggieNosh!')
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html', form=form, title='Login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    """User registration functionality."""
    if 'username' in session:
        flash('You are already registered and logged in!')
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one(
            {'username': request.form['username']})
        if registered_user:
            flash('Username taken. Please choose another!')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(request.form['password'])
        new_user = {
            "username": request.form['username'],
            "password": hashed_password,
            "user_recipes": []
        }
        users_coll.insert_one(new_user)
        session["username"] = request.form['username']
        flash('Welcome to VeggieNosh! Account created.')
        return redirect(url_for('home'))

    return render_template('register.html', form=form, title='Register')

@app.route("/logout")
def logout():
    """Log the user out and redirect to homepage."""
    session.pop("username", None)
    flash('You have been logged out. See you soon, Vegan!')
    return redirect(url_for("home"))

@app.route("/account_settings/<username>")
def account_settings(username):
    username = users_coll.find_one(
        {'username': session['username']})['username']
    return render_template(
        'account_settings.html', username=username, title='Account Settings')
