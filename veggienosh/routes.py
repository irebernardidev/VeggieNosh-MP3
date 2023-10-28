from flask import render_template, url_for, flash, redirect, request, session
from veggienosh import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from veggienosh.forms import (
    RegisterForm, LoginForm, ChangeUsernameForm, ChangePasswordForm
)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# MongoDB Collections Initialization
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# --- ROUTES ---


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', title='Veggienosh Home')


@app.route('/all_recipes')
def all_recipes():
    return render_template(
        "all_recipes.html", recipes=recipes_coll.find(),
        title='All Veggie Delights'
    )


@app.route('/my_recipes')
def my_recipes():
    return render_template("my_recipes.html", title='My Veggie Creations')


@app.route('/add_recipe')
def add_recipe():
    return render_template(
        "add_recipe.html", title='Craft a New Veggie Recipe'
    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash('You are already cultivating vegan wonders!')
        return redirect(url_for('home'))

    form = LoginForm()
    users = users_coll  
    if form.validate_on_submit():
        registered_user = users.find_one({'username': request.form['username']})
        if registered_user and check_password_hash(
                registered_user['password'], request.form['password']):
            session['username'] = request.form['username']
            flash('Welcome back, Veggie Chef!')
            return redirect(url_for('home'))
        else:
            flash("Oops, that's not right. Please double-check your credentials.")
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Enter the Veggie World')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        flash('You are already a member of our vegan community!')
        return redirect(url_for('home'))

    form = RegisterForm()
    users = users_coll  
    if form.validate_on_submit():
        registered_user = users.find_one({'username': request.form['username']})
        if registered_user:
            flash("This chef name is already in use. Choose another!")
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
            flash('Welcome to the Veggienosh family!')
            return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Join the Veggienosh Family')


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash('See you soon, Veggie Chef!')
    return redirect(url_for("home"))


@app.route("/account_settings/<username>")
def account_settings(username):
    username = users_coll.find_one({'username': session['username']})['username']
    return render_template('account_settings.html', username=username, title='Veggie Chef Settings')


@app.route("/change_username/<username>", methods=['GET', 'POST'])
def change_username(username):
    form = ChangeUsernameForm()
    users = users_coll  
    if form.validate_on_submit():
        registered_user = users.find_one({
            'username': request.form['new_username']
        })
        if registered_user:
            flash('Chef name already taken. Choose a different one.')
            return redirect(url_for('change_username', username=session["username"]))
        users.update_one(
            {"username": username},
            {"$set": {"username": request.form["new_username"]}})
        flash(
            "Your username was updated successfully. "
            "Please, login with your new username"
        )
        session.pop("username",  None)
        return redirect(url_for("login"))
    return render_template('change_username.html', username=session["username"], form=form, title='Change Username')


@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    users = users_coll
    form = ChangePasswordForm()
    username = users.find_one({'username': session['username']})['username']
    if form.validate_on_submit():
        if check_password_hash(users.find_one({
                'username': username})['password'], request.form.get('old_password')):
            if request.form.get("new_password") == request.form.get("confirm_new_password"):
                users.update_one(
                    {'username': username},
                    {'$set': {'password': generate_password_hash(request.form['new_password'])}}
                )
                flash("Success! Your password was updated.")
                return redirect(url_for('account_settings', username=username))
            else:
                flash("New passwords do not match! Please try again")
                return redirect(url_for("change_password", username=session["username"]))
        else:
            flash('Incorrect original password! Please try again')
            return redirect(url_for('change_password', username=session["username"]))
    return render_template('change_password.html', username=username, form=form, title='Change Password')
