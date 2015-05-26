# database.py
from app import app
from models import User, Post

db = SQLAlchemy(app)