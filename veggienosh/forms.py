from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Optional, Regexp, ValidationError

# Define the registration form for new users
class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=15),
            Regexp('^[\S]+$', message='No whitespace allowed')  # Username must not contain whitespace
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=3, max=15),
            Regexp('^[\S]+$', message='No whitespace allowed')  # Password must not contain whitespace
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')  # Ensure confirmation matches the password
        ]
    )

    submit = SubmitField('Register')

    
    # Custom validator for the password field
    def validate_password(self, field):
        if self.username.data and field.data.lower().startswith(self.username.data.lower()):
            raise ValidationError("Password cannot start with username")

# Form for user login
class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=15)
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Login')

# Form to change the current username
class ChangeUsernameForm(FlaskForm):
    current_username = StringField('Current Username')

    new_username = StringField(
        'New Username',
        validators=[
            DataRequired(),
            Length(min=3, max=15),
            Regexp('^[\S]+$', message='No whitespace allowed')  # New username must not contain whitespace
        ]
    )

    submit = SubmitField('Change Username')

    # Custom validator for the new username field
    def validate_new_username(self, field):
        if self.current_username.data and self.current_username.data.lower() == field.data.lower():
            raise ValidationError('New username cannot match current username')

# Form to change the current password
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        'Current Password',
        validators=[
            DataRequired(),
            Length(min=3, max=15)
        ]
    )

    new_password = PasswordField(
        'New Password',
        validators=[
            DataRequired(),
            Length(min=3, max=15)
        ]
    )

    confirm_new_password = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(),
            Length(min=3, max=15)
        ]
    )

    submit = SubmitField('Change Password')

# Form for adding a new recipe
class Add_RecipeForm(FlaskForm):
    recipe_name = StringField(
        'Recipe Name',
        validators=[
            DataRequired()
        ]
    )

    recipe_description = TextAreaField(
        'Recipe Description',
        validators=[
            DataRequired()
        ]
    )

    cooking_time = IntegerField(
        'Cooking Time (minutes)',
        validators=[
            DataRequired()
        ]
    )

    servings = IntegerField(
        'Number of Servings',
        validators=[
            DataRequired()
        ]
    )

    image = StringField(
        'Recipe Image',
        validators=[
            Optional()  # Image field is optional
        ]
    )

    ingredients = TextAreaField(
        'Ingredients',
        validators=[
            DataRequired()
        ]
    )

    recipe_directions = TextAreaField(
        'Directions',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Add Recipe')

