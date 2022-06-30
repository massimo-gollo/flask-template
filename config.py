from os import environ


class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')

    MONGODB_SETTINGS = {
        'host': environ.get("MONGO_HOST"),
        'db': environ.get("MONGO_NAME") or 'flask-template',
        'username': environ.get("MONGO_USER"),
        'password': environ.get("MONGO_PASS"),
        'authentication_source': environ.get("MONGO_AUTH_SOURCE") or 'admin'
    }
