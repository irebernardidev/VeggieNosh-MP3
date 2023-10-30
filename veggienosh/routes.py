from flask import render_template, url_for, flash, redirect, request, session
from veggienosh import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from veggienosh.forms import (
    RegisterForm, LoginForm, ChangeUsernameForm,
    ChangePasswordForm, Add_RecipeForm
)
from flask_pymongo import pymongo
from bson.objectid import ObjectId

# MongoDB Collections Initialization
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# Routes

@app.route('/')
@app.route("/home")
def home():
    recipes = recipes_coll.find()
    return render_template('home.html', recipes=recipes, title='Veggienosh Home')


@app.route('/all_recipes')
def all_recipes():
    recipes = recipes_coll.find()
    return render_template("all_recipes.html", recipes=recipes, title='All Veggie Delights')


@app.route('/recipe_info/<recipe_id>')
def single_recipe_info(recipe_id):
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    author = users_coll.find_one({"_id": ObjectId(selected_recipe.get("author"))})["username"]
    return render_template("single_recipe_info.html", selected_recipe=selected_recipe,
                           author=author, title='Recipes')


@app.route('/my_recipes/<username>')
def my_recipes(username):
    my_id = users_coll.find_one({'username': session['username']})['_id']
    my_username = users_coll.find_one({'username': session['username']})['username']
    my_recipes = recipes_coll.find({'author': my_id})
    return render_template("my_recipes.html", my_recipes=my_recipes, username=my_username,
                           title='My Recipes')


@app.route('/add_recipe')
def add_recipe():
    form = Add_RecipeForm()
    diet_types = diets_coll.find()
    dish_types = dishes_coll.find()
    category_types = categories_coll.find()
    return render_template("add_recipe.html", diet_types=diet_types,
                           category_types=category_types, dish_types=dish_types,
                           form=form, title='New Recipe')


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


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    diet_types = diets_coll.find()
    dish_types = dishes_coll.find()
    category_types = categories_coll.find()
    return render_template('edit_recipe.html', selected_recipe=selected_recipe,
                           category_types=category_types, diet_types=diet_types,
                           dish_types=dish_types, title='Edit Recipe')


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = recipes_coll
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    author = selected_recipe.get("author")
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("directions").splitlines()
    if request.method == "POST":
        recipes.update({"_id": ObjectId(recipe_id)}, {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),
            "category_type": request.form.get("category_type"),
            "dish_type": request.form.get("dish_type"),
            "cooking_time": request.form.get("cooking_time"),
            "diet_type": request.form.get("diet_type"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "directions": directions,
            'author': author,
            "image": request.form.get("recipe_image")
        })
        return redirect(url_for("single_recipe_info",
                                recipe_id=recipe_id))

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipes_coll.remove({"_id": ObjectId(recipe_id)})
    author = recipes_coll.find_one({"_id": ObjectId(recipe_id)})["author"]
    users_coll.update_one({"_id": ObjectId(author)},
                          {"$pull": {"user_recipes": ObjectId(recipe_id)}})
    return redirect(url_for("all_recipes"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash('You are already in the Veggienosh kitchen, Chef!')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user and check_password_hash(registered_user['password'], request.form['password']):
            session['username'] = request.form['username']
            flash('Welcome back, Veggie Chef!')
            return redirect(url_for('home'))
        else:
            flash("Oops, something's not right in the recipe. Please recheck your credentials.")
            return redirect(url_for('login'))

    return render_template('login.html', form=form, title='Enter the Veggie World')

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
                "password": hashed_password
            }
            users_coll.insert_one(new_user)
            session['username'] = request.form['username']
            flash('You are now officially a Veggienosh Chef!')
            return redirect(url_for('home'))

    return render_template('register.html', form=form, title='Join the Veggie World')


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
    users = users_coll
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        registered_user = users.find_one({'username': request.form['new_username']})
        if registered_user:
            flash('Chef name already taken. Choose a different one.')
            return redirect(url_for('change_username', username=session["username"]))
        else:
            users.update_one(
                {"username": username},
                {"$set": {"username": request.form["new_username"]}})
            flash(
                "Chef's name plate updated! "
                "Next time, use your new name to enter the Veggienosh kitchen.")
            session.pop("username", None)
            return redirect(url_for("login"))

    return render_template(
        'change_username.html', username=session["username"], form=form, title='Change Username')


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
                users.update_one(
                    {'username': username},
                    {'$set': {'password': generate_password_hash(request.form['new_password'])}})
                flash(
                    "Recipe secret updated! Log in with the new ingredient next time.")
                session.pop('username', None)
                return redirect(url_for('login'))
            else:
                flash("Oops! The new ingredients don't match. Try again.")
                return redirect(url_for('change_password', username=session["username"]))
        else:
            flash("Oops! Old ingredient is not correct. Recheck and try again.")
            return redirect(url_for('change_password', username=session["username"]))

    return render_template(
        'change_password.html', username=username, form=form, title='Change Secret Ingredient')


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    user = users_coll.find_one({"username": username})
    if check_password_hash(user["password"], request.form["confirm_password_to_delete"]):
        flash("We are sad to see you leave the Veggienosh family. Take care, Veggie Chef!")
        session.pop("username", None)
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("home"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("account_settings", username=username))
