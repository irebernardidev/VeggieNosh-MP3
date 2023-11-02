from flask import render_template, url_for, flash, redirect, request, session
from veggienosh import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from veggienosh.forms import (
    RegisterForm, LoginForm, ChangeUsernameForm,
    ChangePasswordForm, Add_RecipeForm
)
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import math

# MongoDB Collections Initialization
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
categories_coll = mongo.db.categories
diets_coll = mongo.db.diets
dishes_coll = mongo.db.dishes

# --- Routes ---

# Home Route
@app.route('/')
@app.route("/home")
def home():
    # Get a sample of 4 random recipes to feature
    featured_recipes = list(recipes_coll.aggregate([
        {"$sample": {"size": 4}}
    ]))
    
    # Render the home page with featured recipes
    return render_template(
        'home.html', 
        featured_recipes=featured_recipes,
        title='Veggienosh Home'
    )

# All Recipes Route
@app.route('/all_recipes')
def all_recipes():
    limit_per_page = 8  # Define the number of recipes per page
    current_page = int(request.args.get('current_page', 1))
    
    # Calculate the total number of recipes
    number_of_all_rec = recipes_coll.count_documents({})
    
    # Calculate the number of pages needed
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    
    # Query the recipes for the current page
    recipes = recipes_coll.find()\
        .sort('_id', pymongo.ASCENDING)\
        .skip((current_page - 1) * limit_per_page)\
        .limit(limit_per_page)
    
    # Render the all recipes page with pagination
    return render_template(
        "all_recipes.html",
        recipes=recipes,
        title='All Veggie Delights',
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec
    )


# Single Recipe Info Route
@app.route('/recipe_info/<recipe_id>')
def single_recipe_info(recipe_id):
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    author = users_coll.find_one({"_id": ObjectId(selected_recipe.get("author"))})["username"]
    return render_template("single_recipe_info.html", selected_recipe=selected_recipe,
                           author=author, title='Recipes')

# My Recipes Route
@app.route('/my_recipes/<username>')
def my_recipes(username):
    # Retrieve user ID based on session username
    my_id = users_coll.find_one({'username': session['username']})['_id']
    
    # Retrieve the same username from the session for consistency
    my_username = users_coll.find_one({'username': session['username']})['username']
    
    # Finds all user's recipes by author id
    my_recipes_query = {'author': my_id}
    
    # Get the total number of recipes created by the user
    number_of_my_rec = recipes_coll.count_documents(my_recipes_query)
    
    # Pagination settings
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    
    # Calculate the total number of pages
    pages = range(1, int(math.ceil(number_of_my_rec / limit_per_page)) + 1)
    
    # Retrieve recipes for the current page
    recipes = (
        recipes_coll.find(my_recipes_query)
        .sort('_id', pymongo.ASCENDING)
        .skip((current_page - 1) * limit_per_page)
        .limit(limit_per_page)
    )
    
    # Render the 'my_recipes' page with the user's recipes and pagination info
    return render_template(
        "my_recipes.html", 
        my_recipes=recipes,  
        username=my_username, 
        recipes=recipes,
        number_of_my_rec=number_of_my_rec,
        current_page=current_page, 
        pages=pages,
        title='My Recipes'
    )


# Add Recipe Route
@app.route('/add_recipe')
def add_recipe():
    # Check if user is logged in
    if 'username' not in session:
        flash('You must be logged in to add a new recipe!')
        return redirect(url_for('home'))

    # Initialize the form
    form = Add_RecipeForm()

    # Retrieve diet, dish, and category types from their respective collections
    diet_types = diets_coll.find()
    dish_types = dishes_coll.find()
    category_types = categories_coll.find()

    # Render the 'add_recipe.html' template with the necessary data
    return render_template("add_recipe.html", diet_types=diet_types,
                           category_types=category_types, dish_types=dish_types,
                           form=form, title='New Recipe')


# Insert Recipe Route
@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("recipe_directions").splitlines()
    author = users_coll.find_one({"username": session["username"]})["_id"]
    if request.method == 'POST':
        new_recipe = {
            "recipe_name": request.form.get("recipe_name").strip(),
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
        flash('Your recipe  was succsessfully added!')
        return redirect(url_for("single_recipe_info", recipe_id=insert_recipe_intoDB.inserted_id))

# Edit Recipe Route
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    # Check if the user is in session
    if 'username' not in session:
        flash('You must be logged in to edit a recipe!')
        return redirect(url_for('home'))
    
    # Get the user in session and the selected recipe
    user_in_session = users_coll.find_one({'username': session['username']})
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})

    # Check if the user in session is the author of the recipe
    if selected_recipe['author'] == user_in_session['_id']:
        # Get the diet, dish, and category types
        diet_types = diets_coll.find()
        dish_types = dishes_coll.find()
        category_types = categories_coll.find()

        # Render the edit recipe template
        return render_template('edit_recipe.html', selected_recipe=selected_recipe,
                               category_types=category_types, diet_types=diet_types,
                               dish_types=dish_types, title='Edit Recipe')
    # Add else block to handle case where user is not the author
    else:
        flash('You do not have permission to edit this recipe!')
        return redirect(url_for('home'))


# Update Recipe Route
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    # Ensure the request method is POST
    if request.method == "POST":
        # Split ingredients and directions into lists
        ingredients = request.form.get("ingredients").splitlines()
        directions = request.form.get("directions").splitlines()

        # Update the document
        recipes_coll.update_one(
            {"_id": ObjectId(recipe_id)},  # Query for the specific document
            {  # $set operator to specify fields to update
                "$set": {
                    "recipe_name": request.form.get("recipe_name"),
                    "description": request.form.get("recipe_description"),
                    "category_type": request.form.get("category_type"),
                    "dish_type": request.form.get("dish_type"),
                    "cooking_time": request.form.get("cooking_time"),
                    "diet_type": request.form.get("diet_type"),
                    "servings": request.form.get("servings"),
                    "ingredients": ingredients,
                    "directions": directions,
                    "image": request.form.get("recipe_image")
                }
            }
        )

        # Redirect to the recipe info page of the updated recipe
        return redirect(url_for("single_recipe_info", recipe_id=recipe_id))


# Delete Recipe Route
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Check if user is logged in
    if 'username' not in session:
        flash('You must be logged in to delete a recipe!')
        return redirect(url_for('home'))

    # Find user in session
    user_in_session = users_coll.find_one({'username': session['username']})
    
    # Retrieve the selected recipe
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    
    # Check if the logged in user is the author of the recipe
    if selected_recipe and selected_recipe['author'] == user_in_session['_id']:
        # Delete the recipe from the collection
        recipes_coll.delete_one({"_id": ObjectId(recipe_id)})
        
        # Update the user's list of recipes by pulling the deleted recipe
        users_coll.update_one({"_id": ObjectId(user_in_session['_id'])},
                              {"$pull": {"user_recipes": ObjectId(recipe_id)}})
        flash('Your recipe has been deleted.')
        return redirect(url_for("home"))
    else:
        # User is not the author or recipe does not exist
        flash("You can only delete your own recipes!")
        return redirect(url_for('home'))

# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    if 'username' in session:
        flash('You are already in the Veggienosh kitchen, Chef!')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        # Retrieve the user collection
        users = users_coll
        # Find the user by username
        registered_user = users.find_one({'username': request.form['username']})
        
        if registered_user:
            # Check if the provided password matches the hashed password in the DB
            if check_password_hash(registered_user['password'], request.form['password']):
                # Set the user session with the current username
                session['username'] = request.form['username']
                flash('Welcome back, Veggie Chef!')
                return redirect(url_for('home'))
            else:
                # If password does not match
                flash("Oops, something's not right in the recipe. Please recheck your credentials.")
                return redirect(url_for('login'))
        else:
            # If the username does not exist in the database
            flash("Chop-chop, that username isn't in our kitchen! Give it another whisk!")
            return redirect(url_for('login'))

    # Render the login template if not logged in or validation fails
    return render_template('login.html', form=form, title='Enter the Veggie World')


# Register Route
@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        flash('Chef, you are already in the Veggienosh kitchen!')
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        users = users_coll
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user:
            flash("This chef name is already cooking. Choose another!")
            return redirect(url_for('register'))
        else:
            hashed_password = generate_password_hash(request.form['password'])
            new_user = {
                "username": request.form['username'],
                "password": hashed_password,
                "user_recipes": []
            }
            users_coll.insert_one(new_user)
            session['username'] = request.form['username']
            flash('You are now officially a Veggienosh Chef!')
            return redirect(url_for('home'))

    return render_template('register.html', form=form, title='Join the Veggie World')

# Logout Route
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash('See you soon, Veggie Chef!')
    return redirect(url_for("home"))

# Account Settings Route
@app.route("/account_settings/<username>")
def account_settings(username):
    if 'username' not in session:
        flash('Chef, please log in to enter the Veggienosh kitchen and view that page!')
    username = users_coll.find_one({'username':
                                    session['username']})['username']
    return render_template('account_settings.html',
                           username=username, title='veggie Chef Settings')

# Change Username Route
@app.route("/change_username/<username>", methods=['GET', 'POST'])
def change_username(username):
    if 'username' not in session:
        flash("You need to be in the Veggienosh kitchen to update your chef's name!")
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

# Change Password Route
@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    if 'username' not in session:
        flash('Chef, please log in to the Veggienosh kitchen to update your secret sauce!')
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
                return redirect(url_for('account_settings', username=username))
            else:
                flash("Oops! The new ingredients don't match. Try again.")
                return redirect(url_for("change_password",
                                        username=session["username"]))
        else:
            flash('Oops! Old ingredient is not correct. Recheck and try again.')
            return redirect(url_for('change_password',
                            username=session["username"]))
    return render_template('change_password.html', username=username,
                           form=form, title='Change Password')
    

# Delete Account Route
@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    if 'username' not in session:
        flash('You must be in the Veggienosh kitchen to toss out an account!')
        return redirect(url_for('login'))  # Redirect if not logged in

    user = users_coll.find_one({"username": username})
    if user is None:
        flash("User not found!")
        return redirect(url_for('home'))  # Redirect if user is not found

    if request.method == 'POST':
        if check_password_hash(user["password"], request.form.get("confirm_password_to_delete")):
            # Removes all user's recipes from the Database
            # Assuming user_recipes field stores a list of ObjectId instances
            all_user_recipes = user.get("user_recipes", [])
            for recipe_id in all_user_recipes:
                recipes_coll.delete_one({"_id": recipe_id})

            flash("We are sad to see you leave the Veggienosh family. Take care, Veggie Chef!")
            session.pop("username", None)
            users_coll.delete_one({"_id": user["_id"]})

            return redirect(url_for("home"))

        else:
            flash("Password is incorrect! Please try again.")
            return redirect(url_for("account_settings", username=username))
    # If the request method is not POST, you may want to show the form or page to confirm deletion
    return render_template('confirm_delete_account.html', username=username)

# Error handlers

# Handle 404 error (page not found)
@app.errorhandler(404)
def error_404(error):
    return render_template('error-pages/404.html', error=True,
                           title="Page not found"), 404

# Handle 500 error (internal server error)
@app.errorhandler(500)
def error_500(error):
    return render_template('error-pages/500.html', error=True,
                           title="Internal Server Error"), 500



    
