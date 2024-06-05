# backend/__init__.py
from flask import Flask
from .models import db
from .routes import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev-user13:16153371G.4.L@localhost/todo_list_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main_bp)

    return app