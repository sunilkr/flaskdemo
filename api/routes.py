from flask import json
from flask.json import jsonify
from flask import Blueprint, request
from ..models import Book, User
from ..db import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/hello")
def hello():
    return jsonify({"hello":"world"})

@api_bp.route("/user/<id>")
def get_user(id):
    user = User.query.filter(User.id == int(id)).first()
    if(user is not None):
        return jsonify(user.serialize())
    return jsonify({"error": "Not found"}), 404


@api_bp.route("/user/new", methods=["POST"])
def new_user():
    input = json.loads(request.data)
    user = User(**input)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201


@api_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.serialize() for u in users])



@api_bp.route("/book/<id>")
def get_book(id):
    book = Book.query.filter(Book.id == int(id)).first()
    if (book is not None):
        return jsonify(book.serialize())
    return jsonify({"error": "Not found"}), 404


@api_bp.route("/book/new", methods=["POST"])
def new_book():
    req_data = json.loads(request.data)
    book = Book()
    book.isbn = req_data['isbn']
    book.name = req_data['name']
    db.session.add(book)
    db.session.commit()
    return jsonify(book.serialize()), 201


@api_bp.route("/books", methods=["GET"])
def get_books():
    #books = Book.query.all()
    books = Book.query.all()
    #return jsonify(list(map(lambda b: b.serialize(), books)))
    return jsonify([book.serialize() for book in books])
