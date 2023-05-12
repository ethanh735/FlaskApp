from flask import Flask, render_template, url_for
# escape user data to prevent script injection
from markupsafe import escape

app = Flask(__name__)

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

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/home")
def home():
	return render_template("home.html", title="Home", posts=posts)

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"
