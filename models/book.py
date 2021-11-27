
from ..db import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column (db.Integer, primary_key=True)
    isbn = db.Column (db.String(13), unique=True, nullable=False)
    name = db.Column (db.String(100), unique=True, nullable=False)

    def __init__(self, id=0, isbn='0'*13, name='TBD'):
        #super().__init__()
        self.id = id
        self.isbn = isbn
        self.name = name


    def serialize(self):
        return {'id': self.id, 'name': self.name, 'isbn': self.isbn}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f"<Book {{ISBN: {self.isbn}}}>"
