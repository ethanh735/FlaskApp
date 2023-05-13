from flask import Flask, render_template, url_for, flash, redirect
# from forms.py, same directory layer
from forms import RegistrationForm, LoginForm
# escape user data to prevent script injection
from markupsafe import escape

app = Flask(__name__)

# secret key prevents cross-site request / cookie changes
app.config["SECRET_KEY"] = "b368e6ea06db12e08f25c58465daf913"

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
	# uses login form for credentials
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "a@gmail.com" and form.password.data == "123":
			# flash messages send one time alerts
			flash(f"You have been logged in!", "success")
			return redirect(url_for("home"))
		else:
			flash(f"Login unsuccessful, please check username and password.", "danger")
	return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
	# uses registration form for credentials
	form = RegistrationForm()
	if form.validate_on_submit():
		# flash messages send one time alerts
		flash(f"Account created for {form.username.data}!", "success")
		return redirect(url_for("home"))
	return render_template("register.html", title="Register", form=form)

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"
