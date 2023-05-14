# Python classes converted to html forms when in a template
from flask_wtf import FlaskForm
# Fields and validations available for form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators

class RegistrationForm(FlaskForm):
	# Validates existence and particular length
	username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
	# Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", validators=[validators.DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
	submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    # Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", validators=[validators.DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")

