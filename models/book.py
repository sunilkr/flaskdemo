#from flask_sqlalchemy.model import Model
#from ..db import ModelBase
from ..db import db
from sqlalchemy import Column, Integer, String

class Book(db.Model):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    isbn = Column(String(13), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)

    def __init__(self, isbn='0'*13, name='TBD'):
        #super().__init__()        
        self.isbn = isbn
        self.name = name


    def serialize(self):
        return {'id': self.id, 'name': self.name, 'isbn': self.isbn}

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    def __repr__(self) -> str:
        return f"<Book {{ISBN: {self.isbn}}}>"
