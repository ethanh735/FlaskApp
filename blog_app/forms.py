# Python classes converted to html forms when in a template
from flask_wtf import FlaskForm
# file type management and restriciton for account image
from flask_wtf.file import FileField, FileAllowed
# Fields and validations available for form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, validators, ValidationError
from blog_app.models import User
# For account update checks: okay to have info matching current user
from flask_login import current_user

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
		# if user exists
		if user:
			raise ValidationError("Username is taken. Please choose another username.")
		
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		# if user exists
		if user:
			raise ValidationError("Email is taken. Please choose another email.")

#TODO: implement "remember me" functionality
class LoginForm(FlaskForm):
    # Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", validators=[validators.DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")

class PostForm(FlaskForm):
	title = StringField("Title", validators=[validators.DataRequired()])
	content = TextAreaField("Content", validators=[validators.DataRequired()])
	submit = SubmitField("Post")

class UpdateAccountForm(FlaskForm):
	# Validates existence and particular length
	username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
	# Validates existence and correct type
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	# Validates correct file type
	picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
	submit = SubmitField("Update")

	# custom validations for already registered user
	def validate_username(self, username):
		# only checked if username is changed
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			# if user exists
			if user:
				raise ValidationError("Username is taken. Please choose another username.")
		
	def validate_email(self, email):
		# only checked if email is changed
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			# if user exists
			if user:
				raise ValidationError("Email is taken. Please choose another email.")

class RequestResetForm(FlaskForm):
	email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
	submit = SubmitField("Request Password Reset")

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		# if user doesn't exist
		if user is None:
			raise ValidationError("There is no account with this email. You must register an account first.")

class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password", validators=[validators.DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
	submit = SubmitField("Reset Password")
