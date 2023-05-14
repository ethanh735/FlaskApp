# Python classes converted to html forms when in a template
from flask_wtf import FlaskForm
# Fields and validations available for form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, ValidationError
from blog_app.models import User

class RegistrationForm(FlaskForm):
	# Validates existence and particular length
	username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
	# Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", validators=[validators.DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
	submit = SubmitField("Sign Up")

	# custom validations for already registered user
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		# if user is anything other than none
		if user:
			raise ValidationError("Username is taken. Please choose another username.")
		
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		# if user is anything other than none
		if user:
			raise ValidationError("Email is taken. Please choose another email.")

class LoginForm(FlaskForm):
    # Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", validators=[validators.DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")

