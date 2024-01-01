from datetime import datetime
from blog_app import db, login_manager, app
# automatically brings in user model attribute requirements
from flask_login import UserMixin
# used to make sure that only email access can reset account password
from itsdangerous.serializer import Serializer

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# database model setup
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True,nullable=False)
	email = db.Column(db.String(120), unique=True,nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
	password =  db.Column(db.String(60), nullable=False)
	# interrelates users and posts: one to many
	posts = db.relationship("Post", backref="author", lazy=True)

# def get_reset_token(self, expires_sec=1800):
# 		s = Serializer(app.config["SECRET_KEY"], expires_sec)
# 		return s.dumps(["user_id": self.id])

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(app.config["SECRET_KEY"])
		# several exceptions possible with token
		try:
			user_id = s.loads(token)["user_id"]
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', 'self.image_file')"
	
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"
