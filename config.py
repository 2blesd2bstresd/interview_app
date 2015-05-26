# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'd400u70sqnkvso'
USERNAME = 'snvsvsufglzpal'
PASSWORD = '-ReHAiJScBOaEUBlmqqJ8dBnQx'
SECRET_KEY = 'my_precious'
CSRF_ENABLED = True 
DATABASE_PATH = os.path.join(basedir, DATABASE)

URL = '//snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'

# database URI
SQLALCHEMY_DATABASE_URI = 'postgres://snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'