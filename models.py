# models.py
from database import db

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)

	def __init__(self, name, id):

		name = self.name
		id = self.id

class Post(db.Model):

	__tablename__ = 'posts'

	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String)
	data = db.Column(db.String)

	def __init__(self, user_id, name):

		user_id = self.user_id
		name = self.name
