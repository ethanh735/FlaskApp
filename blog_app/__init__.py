from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# hashes passwords to prevent theft
from flask_bcrypt import Bcrypt
# login session manager
from flask_login import LoginManager

# app initialization
app = Flask(__name__)
# secret key prevents cross-site request / cookie changes
app.config["SECRET_KEY"] = "b368e6ea06db12e08f25c58465daf913"
# SQLite database file location, relative path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_message_category = "info"

# must be after app initialization to avoid circular import
from blog_app import routes

