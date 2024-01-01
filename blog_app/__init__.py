# This file tells Python that the project is package structure
from flask import Flask
# creates SQL database per app instance
from flask_sqlalchemy import SQLAlchemy
# hashes passwords to prevent theft
from flask_bcrypt import Bcrypt
# login session manager
from flask_login import LoginManager
# import python environment variables
import os

# app initialization
app = Flask(__name__)
# secret key prevents cross-site request forgery (CSRF) / cookie changes, environment variable in .bash_profile
app.config["SECRET_KEY"] = os.environ.get("KEY")
# SQLite database file location, relative path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_message_category = "info"

# must be after app initialization to avoid circular import
from blog_app import routes

