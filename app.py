import os
import psycopg2
# from functools import wraps
from psycopg2.extras import RealDictCursor
import urlparse
from flask import Flask, jsonify, abort, request, session, Response
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from datetime import datetime
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# SQLAlchemy models
class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)

	def __init__(self, name, id):

		self.name = name
		self.id = id

	def __repr__(self):
		return '<USER>'

class Post(db.Model):

	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	data = db.Column(db.String)

	def __init__(self, user_id, data):

		self.user_id = user_id
		self.data = data

	def __repr__(self):
		return '<POST>'


@app.route('/', methods=['GET'])
def index():
	return 'welcome!'

@app.route('/add', methods=['POST'])
def add():

	form = request.form

	data = form.get('data', None)
	user_id = form.get('user_id', None)
	
	p = Post(user_id=user_id, data=data)

	db.session.add(p)
	db.session.commit()

	return jsonify({'status': 200})

@app.route('/retrieve', methods=['GET'])
def retrieve():

	user_id = request.args.get('user_id')
	posts = Post.query.filter_by(user_id=user_id).all()

	data = []

	for p in posts:
		data.append(p.data)

	return jsonify({'posts': data})


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port = port)

