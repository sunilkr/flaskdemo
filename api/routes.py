from flask.json import jsonify
from flask import Blueprint


api_bp = Blueprint("api", __name__)

@api_bp.route("/hello")
def hello():
    return jsonify({"hello":"world"})

@api_bp.route("/user/<id>")
def get_user(id):
    #user = User(id=1, username='test', email='test@email.com')
    return jsonify(None)
