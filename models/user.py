from ..db import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def serialize(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}

    def __repr__(self):
        return '<User %r>' % self.username
