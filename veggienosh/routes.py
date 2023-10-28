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


# Route for home page
@app.route('/')
@app.route("/home")
def home():
    recipes = recipes_coll.find()
    return render_template('home.html', recipes=recipes, title='Veggienosh Home')


# Route to display all recipes
@app.route('/all_recipes')
def all_recipes():
    return render_template(
        "all_recipes.html", recipes=recipes_coll.find(),
        title='All Veggie Delights'
    )


# Route to display user's recipes
@app.route('/my_recipes')
def my_recipes():
    return render_template("my_recipes.html", title='My Veggie Creations')


# Route to add new recipe
@app.route('/add_recipe')
def add_recipe():
    form = Add_Edit_RecipeForm(request.form)
    diet_types = diets_coll.find()
    dish_types = dishes_coll.find()
    category_types = categories_coll.find()
    return render_template(
        "add_recipe.html", diet_types=diet_types,
        category_types=category_types, dish_types=dish_types,
        form=form, title='New Recipe'
    )


# Route to insert a recipe into the database
@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("recipe_directions").splitlines()
    author = users_coll.find_one({"username": session["username"]})["_id"]

    if request.method == 'POST':
        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),
            "category_type": request.form.get("category_type"),
            "dish_type": request.form.get("dish_type"),
            "diet_type": request.form.get("diet_type"),
            "cooking_time": request.form.get("cooking_time"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "directions": directions,
            'author': author,
            "image": request.form.get("image")
        }
        insert_recipe_intoDB = recipes_coll.insert_one(new_recipe)
        users_coll.update_one(
            {"_id": ObjectId(author)},
            {"$push": {"user_recipes": insert_recipe_intoDB.inserted_id}}
        )
        return redirect(url_for("home", recipe_id=insert_recipe_intoDB.inserted_id))


# Route for user login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash('You are already in the Veggienosh kitchen, Chef!')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user and check_password_hash(
                registered_user['password'], request.form['password']):
            session['username'] = request.form['username']
            flash('Welcome back, Veggie Chef!')
            return redirect(url_for('home'))
        else:
            flash("Oops, something's not right in the recipe. Please recheck your credentials.")
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Enter the Veggie World')


# Route for user registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        flash('Chef, you are already in the Veggienosh kitchen!')
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user:
            flash("This chef name is already cooking. Choose another!")
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


# Route to logout the user
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash('See you soon, Veggie Chef!')
    return redirect(url_for("home"))


# Route for user account settings
@app.route("/account_settings/<username>")
def account_settings(username):
    username = users_coll.find_one({'username': session['username']})['username']
    return render_template('account_settings.html', username=username, title='Veggie Chef Settings')


# Route to change user's username
@app.route("/change_username/<username>", methods=['GET', 'POST'])
def change_username(username):
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one({'username': request.form['new_username']})
        if registered_user:
            flash('Chef name already taken. Choose a different one.')
            return redirect(url_for('change_username', username=session["username"]))
        users_coll.update_one(
            {"username": username},
            {"$set": {"username": request.form["new_username"]}}
        )
        flash(
            "Chef's name plate updated! "
            "Next time, use your new name to enter the Veggienosh kitchen."
        )
        session

        session.pop("username",  None)
        return redirect(url_for("login"))
    return render_template('change_username.html', username=session["username"], form=form, title='Change Username')


@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    users = users_coll
    form = ChangePasswordForm()
    username = users.find_one({'username': session['username']})['username']
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get("confirm_new_password")
    
    if form.validate_on_submit():
        if check_password_hash(users.find_one({
                'username': username})['password'], old_password):
            if new_password == confirm_password:
                users.update_one({'username': username}, {'$set': {'password': generate_password_hash(request.form['new_password'])}})
                flash("Recipe secret updated! You've successfully changed your password.")
                return redirect(url_for('account_settings', username=username))
            else:
                flash("New passwords do not match! Please try again")
                return redirect(url_for("change_password",
                                        username=session["username"]))
        else:
            flash('Incorrect original password! Please try again')
            return redirect(url_for('change_password', username=session["username"]))
    return render_template('change_password.html', username=username, form=form, title='Change Password')


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    user = users_coll.find_one({"username": username})
    if check_password_hash(user["password"],
                           request.form["confirm_password_to_delete"]):
        flash("We're sad to see you leave the Veggienosh kitchen. Farewell, Chef!")
        session.pop("username", None)
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("home"))
    else:
        flash("Something's amiss in the recipe. Please check your password.")
        return redirect(url_for("account_settings", username=username))