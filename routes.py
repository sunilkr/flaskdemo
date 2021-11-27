from flask import current_app as app

@app.route("/")
def home():
    return "<h3>This is home</h3>"