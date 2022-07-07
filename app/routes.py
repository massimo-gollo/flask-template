
from flask import current_app as app, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.tools import jsonify


@app.route('/ping')
def ping():
    return 'pong', 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()

    print(identity)
    # access_token = create_access_token(identity=identity)
    # return jsonify(access_token=access_token)
    return jsonify(identity=identity)
