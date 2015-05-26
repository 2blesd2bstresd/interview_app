# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'd400u70sqnkvso'
USERNAME = 'snvsvsufglzpal'
PASSWORD = '-ReHAiJScBOaEUBlmqqJ8dBnQx'
DATABASE_PATH = os.path.join(basedir, DATABASE)
# database URI
SQLALCHEMY_DATABASE_URI = 'postgres://snvsvsufglzpal:-ReHAiJScBOaEUBlmqqJ8dBnQx@ec2-54-197-224-173.compute-1.amazonaws.com:5432/d400u70sqnkvso'