from . import create_app
from config import basedir
from db import db
from .ui.routes import ui_bp
from .api.routes import api_bp


app = create_app()
app.register_blueprint(ui_bp, url_prefix="/ui")
app.register_blueprint(api_bp, url_prefix="/api")
db.init_app(app)

with app.app_context():
    import routes
    from .models.book import Book
    
    #db.init_app(app=app)
    db.create_all()
    db.session.commit()
    #db.session.add(Book())
    #db.session.commit()
    #books = Book.query.all()
    #print(books)

print (app.config['DEBUG'])
print (basedir)
