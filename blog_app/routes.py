from flask import render_template, url_for, flash, redirect
from blog_app import app, db, bcrypt
# from forms.py, same directory layer
from blog_app.forms import RegistrationForm, LoginForm
from blog_app.models import User, Post
from flask_login import login_user, current_user, logout_user


# post dummy data
posts = [
{
	"author": "first author",
	"title": "this is a title",
	"content": "content of my first post!",
	"date_posted": "May 11, 2023"
},
{
	"author": "another author",
    "title": "this title is different",
    "content": "A different post?",
    "date_posted": "May 09, 2023"
}
]

# routes throughout app
@app.route("/")
def index():
	return render_template("index.html", title="Index")

@app.route("/home")
def home():                                                                                     
	return render_template("home.html", title="Home", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
	# uses login form for credentials
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		# if email is in database and passwords match
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for("home"))
		else:
			flash(f"Login unsuccessful, please check email and password.", "danger")
	return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
	# uses registration form for credentials
	form = RegistrationForm()
	if form.validate_on_submit():
		# password handling for database
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		# initialize user for database
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		# flash messages send one time alerts
		flash(f"Account created for {form.username.data}! You are now able to log in.", "success")
		return redirect(url_for("login"))
	return render_template("register.html", title="Register", form=form)

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"
