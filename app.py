from flask import Flask
from .db import db
from .config import Config
from .models import *
from .api.routes import api_bp
from .ui.routes import ui_bp

app = Flask(__name__)

print (Config.SQLALCHEMY_DATABASE_URI)
#app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config.from_object(Config)
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(ui_bp, url_prefix='/ui')
#db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()
