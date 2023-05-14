from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app initialization
app = Flask(__name__)
# secret key prevents cross-site request / cookie changes
app.config["SECRET_KEY"] = "b368e6ea06db12e08f25c58465daf913"
# SQLite database file location, relative path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

# must be after app initialization to avoid circular import
from blog_app import routes

