from flask import json
from flask.json import jsonify
from flask import Blueprint, request
from ..models.book import Book


api_bp = Blueprint("api", __name__)

@api_bp.route("/hello")
def hello():
    return jsonify({"hello":"world"})

@api_bp.route("/user/<id>")
def get_user(id):
    #user = User(id=1, username='test', email='test@email.com')
    return jsonify(None)

@api_bp.route("/book/<id>")
def get_book(id):
    book = Book()
    book.id = int(id)
    book.name = "Its a new book"
    book.isbn = "1"*13
    return jsonify(book.serialize())

@api_bp.route("/book/new", methods=["POST"])
def new_book():
    req_data = json.loads(request.data)
    book = Book()
    book.id = int(req_data['id'])
    book.isbn = req_data['isbn']
    book.name = req_data['name']
    book.save()
    return jsonify(req_data)

@api_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify(map(lambda b: b.serialize(), books))
