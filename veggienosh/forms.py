# Import necessary libraries and modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# --- Registration Form ---
class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=3, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    # Define submit button
    submit = SubmitField('Register')


# --- Login Form ---
class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# --- Change Username Form ---
class ChangeUsernameForm(FlaskForm):  # Corrected the class name here
    old_username = StringField('Current Username',
                               validators=[DataRequired(), Length(min=3, max=15)])
    new_username = StringField('New Username',
                               validators=[DataRequired(), Length(min=3, max=15)])
    submit = SubmitField('Change Username')


# --- Change Password Form ---
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current Password',
                                 validators=[DataRequired()])
    new_password = PasswordField('New Password', 
                                 validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password',
                                         validators=[DataRequired(), EqualTo('new_password')])  # It's better to compare it with 'new_password' 
    submit = SubmitField('Change Password')
