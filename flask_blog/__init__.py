from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)

    from flask_blog.main.routes import main
    app.register_blueprint(main)

    return app
