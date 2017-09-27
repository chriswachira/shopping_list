from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo, DataRequired, Email

class RegistrationForm(FlaskForm):
    """Creates registration form for web app"""
    firstname = StringField("Name", validators=[Required(),
        Length(min=2,max=20)])
    lastname = StringField("Username", validators=[Required(),
        Length(min=2, max=20)])
    email = StringField("Email", validators=[Email(), Required(),
        Length(min=6, max=30)])
    password = PasswordField('New Password', validators=[DataRequired(),
        Length(min=6, max=15),
        EqualTo('password_confirm', message='Passwords should match')])
    password_confirm = PasswordField("Enter password again", validators=[
        DataRequired()])

class LoginForm(FlaskForm):
    """Create login form for web app"""
    username = StringField("Username",
            validators=[Required(), Length(min=6, max=30)])
    password = PasswordField('New Password', validators=[DataRequired()])


