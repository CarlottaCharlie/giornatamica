import re
from datetime import datetime
from app import app, db
from sqlalchemy.orm.exc import NoResultFound, StaleDataError, MultipleResultsFound
import os, glob
from werkzeug.security import generate_password_hash, check_password_hash
# from search import add_to_index, remove_from_index, query_index
from flask_login import UserMixin
from app import login
from flask_login import current_user

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
