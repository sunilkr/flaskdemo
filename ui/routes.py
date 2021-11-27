from flask import Blueprint

ui_bp = Blueprint("ui", __name__, template_folder="templates", static_folder="static")

@ui_bp.route("/")
def index():
    return "<h3> This comes from UI</h3>"
    