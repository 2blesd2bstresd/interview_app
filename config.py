# config.py
import os
# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'd400u70sqnkvso' 
USERNAME = 'snvsvsufglzpal' 
PASSWORD = '-ReHAiJScBOaEUBlmqqJ8dBnQx' 
CSRF_ENABLED = True 
SECRET_KEY = 'my_precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# DB URL
URL = '//snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'

# database URI
SQLALCHEMY_DATABASE_URI = 'postgres://snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'