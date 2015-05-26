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

import config

url = urlparse.urlparse('//yymrdbzqoowsqh:1bmpBpFOiKPLzweXcuX04FASwB@ec2-23-21-183-70.compute-1.amazonaws.com:5432/d7p0rp7lvl3e7b')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# SQLAlchemy models
class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)

	def __init__(self, name, id):

		name = self.name
		id = self.id

class Post(db.Model):

	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String)
	data = db.Column(db.String)

	def __init__(self, user_id, name):

		user_id = self.user_id
		name = self.name


@app.route('/', methods=['GET'])
def index():
	return 'welcome!'

@app.route('/add', methods=['POST'])
def add():

	print 'REQUEST: ', request

	form = request.form

	print 'FORM: ', form

	data = form.get('data', None)
	user_id = form.get('user_id', None)

	print 'DATA: ', data
	print 'USER ID: ', user_id
	
	post = Post(user_id, data)

	print 'FAILED TO INIT'

	db.session.add(post)
	db.session.commit()

	print 'SUCCESS!'

	return jsonify({'status': 200})

@app.route('/retrieve', methods=['GET'])
def retrieve():

	form = request.form

	data = form.get('data', None)
	user_id = form.get('user_id', None)

	posts = db.session.query(Post).filter(data=data).filter(user_id=user_id).all()

	return jsonify({'posts': posts})


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port = port)

