# backend/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from backend.config import Config
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()  # Initialize CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize database
    db.init_app(app)

    # Initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Set the login view

    # Initialize CSRF protection
    csrf.init_app(app)

    # Import and register blueprints
    from backend.routes.auth import auth_bp
    from backend.routes.profile import profile_bp
    from backend.routes.tasks import tasks_bp
    from backend.routes.index import index_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(index_bp)

    return app

# Import your User model here
from backend.models import User  

# Define user loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
