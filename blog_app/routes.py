from flask import render_template, url_for, flash, redirect, abort, request
from blog_app import app, db, bcrypt
# from other Python files, same directory layer
from blog_app.forms import RegistrationForm, LoginForm, PostForm
from blog_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# routes throughout app:
# home page with all posts
@app.route("/")
@app.route("/home")
def home():
	posts = Post.query.all()
	return render_template("home.html", title="Home", posts=posts)

# about page
@app.route("/about")
def about():
	return render_template("about.html", title="About")

# log into a registered account
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
			flash(f"Logged in!", "info")
			return redirect(url_for("home"))
		else:
			flash(f"Login unsuccessful, please check email and password.", "danger")
	return render_template("login.html", title="Login", form=form)

# log out of current account
@app.route("/logout")
def logout():
	logout_user()
	flash(f"Logged out.", "info")
	return redirect(url_for("home"))

# register for an account
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

@app.route("/account")
@login_required
def account():
	image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
	return render_template("account.html", title="Account", image_file=image_file)

# create a new post
@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		# flash messages send one time alerts
		flash("Your post has been created!", "success")
		return redirect(url_for("home"))
	return render_template("create_post.html", title="New Post", form=form, legend="New Post")

# view individual posts
@app.route("/post/<int:post_id>")
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template("post.html", title=post.title, post=post)

# update a given post
@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)

	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash("Post updated successfully!", "success")
		return redirect(url_for("post", post_id=post.id))
	elif request.method == "GET":
		form.title.data = post.title
		form.content.data = post.content
	return render_template("create_post.html", title="Update Post", form=form, legend="Update Post")
	
# delete a given post
@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash("Post deleted successfully!", "success")
	return redirect(url_for("home"))
