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
        title='VeggieNosh Home'
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

# Define the route for viewing a user's recipes
@app.route('/my_recipes/<username>')
def my_recipes(username):
    # Retrieve user's ID from the database using the session username
    my_id = users_coll.find_one({'username': session['username']})['_id']
    # Retrieve the actual username for display purposes
    my_username = users_coll.find_one({'username': session['username']})['username']
    
    # Execute a query to find all recipes authored by the user
    my_recipes_cursor = recipes_coll.find({'author': my_id})
    # Count the total number of recipes found
    number_of_my_rec = recipes_coll.count_documents({'author': my_id})
    
    # Pagination setup: number of recipes displayed per page set to 8
    limit_per_page = 8
    # Determine the current page number from the query parameter 'current_page'
    current_page = int(request.args.get('current_page', 1))
    # Calculate the total number of pages needed to display all recipes
    total_pages = math.ceil(number_of_my_rec / limit_per_page)
    # Generate a range of page numbers for pagination links
    pages = range(1, int(total_pages) + 1)
    
    # Sort recipes by ID in ascending order for the current page and limit the results per page
    recipes_displayed = my_recipes_cursor.sort('_id', pymongo.ASCENDING) \
                                         .skip((current_page - 1) * limit_per_page) \
                                         .limit(limit_per_page)

    # Render the 'my_recipes' template with the data for the user's recipes
    return render_template(
        "my_recipes.html",
        my_recipes=list(recipes_displayed),  # Convert cursor to a list for the template
        username=my_username,
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


# Route for inserting a new recipe into the database
@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    # Parse ingredients and directions from form, splitting by new lines
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("recipe_directions").splitlines()
    # Retrieve author's ID from the session
    author = users_coll.find_one({"username": session["username"]})["_id"]

    # Process the form submission
    if request.method == 'POST':
        # Construct the new recipe dictionary from form inputs
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
        
        # Insert the new recipe document into the database
        insert_recipe_intoDB = recipes_coll.insert_one(new_recipe)
        
        # Update the user's document with the new recipe's ID
        users_coll.update_one(
            {"_id": ObjectId(author)},
            {"$push": {"user_recipes": insert_recipe_intoDB.inserted_id}}
        )
        
        # Notify user of successful addition and redirect to the new recipe's page
        flash('Your recipe was successfully added!')
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


# Define the route to update a specific recipe by its ID
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    # Find the selected recipe by its ID in the database
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    
    # Retrieve the author's information from the selected recipe
    author = selected_recipe.get("author")
    
    # Only proceed if the method is POST
    if request.method == "POST":
        # Split the ingredients and directions from the form into lists
        ingredients = request.form.get("ingredients").splitlines()
        directions = request.form.get("directions").splitlines()

        # Update the recipe document in the database with new values
        recipes_coll.update_one(
            {"_id": ObjectId(recipe_id)},  # Query for the specific document
            {  # Use the $set operator to specify the fields to be updated
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

        # After updating, redirect the user to the recipe info page of the updated recipe
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
        flash('You are already in the VeggieNosh kitchen, Chef!')
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
        flash('Chef, you are already in the VeggieNosh kitchen!')
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
            flash('You are now officially a VeggieNosh Chef!')
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

@app.route("/change_username", methods=['GET', 'POST'])  # Removed <username> to prevent confusion
def change_username():
    # Redirect user if they're not logged in
    if 'username' not in session:
        flash("You need to be in the VeggieNosh kitchen to update your chef's name!")
        return redirect(url_for('login'))

    users = users_coll
    current_username = session['username']
    form = ChangeUsernameForm(current_username=current_username)

    if form.validate_on_submit():
        new_username = request.form['new_username']

        # Check if the new username already exists, case-insensitive search
        registered_user = users.find_one({'username': {"$regex": f"^{new_username}$", "$options": "i"}})
        
        if registered_user and registered_user['username'] != current_username:
            flash('Chef name already taken. Choose a different one.')
        else:
            # Update the database with the new username
            users.update_one(
                {"username": current_username},
                {"$set": {"username": new_username}})
            flash("Chef's name plate updated! Next time, use your new name to enter the Veggienosh kitchen.")
            session['username'] = new_username  # Update the session with the new username
            return redirect(url_for("login"))

    return render_template(
        'change_username.html', username=current_username, form=form, title='Change Username')

# Change Password Route
@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    if 'username' not in session:
        flash('Chef, please log in to the VeggieNosh kitchen to update your secret sauce!')
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
        flash('You must be in the VeggieNosh kitchen to toss out an account!')
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

            flash("We are sad to see you leave the VeggieNosh family. Take care, Veggie Chef!")
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


@app.route("/search")
def search():
    """
    Function to handle search queries for recipes.

    Retrieves user input, searches the database for matching recipes
    with regex for partial matching, handles pagination,
    and renders the results on 'search.html'.
    """
    
    # Pagination setup
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    query = request.args.get('query')

    # Perform the search with regex for partial matching
    regex_query = {"$regex": query, "$options": "i"}  # Case-insensitive partial match
    results = recipes_coll.find(
        {"recipe_name": regex_query}
    ).sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1) * limit_per_page
    ).limit(limit_per_page)

    # Calculate the total number of recipes found with regex search
    number_of_recipes_found = recipes_coll.count_documents(
        {"recipe_name": regex_query}
    )

    # Determine the total number of pages for pagination
    total_pages = int(math.ceil(number_of_recipes_found / limit_per_page))
    results_pages = range(1, total_pages + 1)

    # Render the search results page
    return render_template(
        "search.html",
        title='Search',
        limit_per_page=limit_per_page,
        number_of_recipes_found=number_of_recipes_found,
        current_page=current_page,
        query=query,
        results=results,
        results_pages=results_pages,
        total_pages=total_pages
    )