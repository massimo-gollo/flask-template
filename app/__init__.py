from flask import Flask
from config import Config
from app.database.db import mongo

from app.plugins.jwt_manager import jwt


def create_app(config=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    mongo.init_app(app)
    jwt.init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        from . import routes

    return app
