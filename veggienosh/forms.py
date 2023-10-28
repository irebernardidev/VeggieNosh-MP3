from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# --- Register Form ---
class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')


# --- Login Form ---
class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Login')


# --- Change Username Form ---
class ChangeUsernameForm(FlaskForm):
    new_username = StringField(
        'New Username',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    submit = SubmitField('Change Username')


# --- Change Password Form ---
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        'Current Password',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    new_password = PasswordField(
        'New Password',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    confirm_new_password = PasswordField(
        'Confirm New Password',
        validators=[DataRequired(), Length(min=3, max=15)]
    )
    submit = SubmitField('Change Password')
