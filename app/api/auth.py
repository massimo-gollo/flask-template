from app.api import api_bp as bp
from flask import request, url_for, current_app as app
from app.models.user import User
from app.tools import jsonify
from app.api.errors import bad_request
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_jwt_extended import create_access_token, create_refresh_token


@bp.route('/auth/verify', methods=['POST', 'GET'])
def verify():
    tkn = request.get_json().get('idToken')
    print(tkn)
    if tkn is None:
        return bad_request('missing token')

    user_info = token_is_valid(tkn)
    if user_info is not None:
        user = User.objects(email=user_info['email']).first()
        if user is None:
            user = User(email=user_info['email'],
                        first_name=user_info['given_name'],
                        last_name=user_info['family_name'],
                        profile_pic=user_info['picture'])
            user.save().reload()

        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        print("access " + access_token)
        print("refresh " + refresh_token)

        return jsonify({'access': access_token, 'refresh': refresh_token})
    else:
        return bad_request('error validate user')


def token_is_valid(tkn):
    try:
        idinfo = id_token.verify_oauth2_token(tkn, requests.Request(), app.config['GOOGLE_CLIENT_ID'])
        return idinfo
    except ValueError:
        print('invalid Token')
        return None


