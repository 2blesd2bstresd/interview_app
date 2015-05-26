# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

database = 'd400u70sqnkvso'
user = 'snvsvsufglzpal'
pw = '-ReHAiJScBOaEUBlmqqJ8dBnQx'

CSRF_ENABLED = True 
# SECRET_KEY = 'my_precious'
# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database URI
SQLALCHEMY_DATABASE_URI = 'postgres://snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'