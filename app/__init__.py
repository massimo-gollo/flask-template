from flask import Flask
from config import Config


def create_app(config=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    mongo.init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        from . import routes

    return app
