from flask_jwt_extended import JWTManager
from mongoengine import DoesNotExist


class CustomJWTManager(JWTManager):

    def __init__(self, app=None):
        super().__init__()

        if app is not None:
            self.init_app(app)


jwt = CustomJWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    from app.models.user import User
    try:
        u = User.objects(email=identity).get()
    except DoesNotExist:
        return None
    return u


@jwt.user_lookup_error_loader
def user_lookup_error_loader(jwt_header, jwt_payload):
    return "Cannot validate token"
