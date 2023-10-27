# Import necessary libraries and modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# Registration Form
# -----------------
class RegistrationForm(FlaskForm):
    # Define username field with validators
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    
    # Define password field with validators
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    
    # Define confirm password field with validators
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    
    # Define submit button
    submit = SubmitField('Register')


# Login Form
# ----------
class LoginForm(FlaskForm):
    # Define username field with validators
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    
    # Define password field with validators
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    
    # Define submit button
    submit = SubmitField('Login')
