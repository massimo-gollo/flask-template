from app.api import api_bp as bp
from flask import request, url_for
from app.models.user import User
from app.tools import jsonify
from app.api.errors import bad_request


@bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    return jsonify(User.objects.get_or_404(id=id).to_dict())


@bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass


@bp.route('/users', methods=['GET'])
def get_users():
    pass


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    print(data)
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.objects(username=data['username']):
        return bad_request('please use a different username')
    if User.objects(email=data['email']):
        return bad_request('please use a different email')
    user = User()
    user.from_dict(data, new_user=True)
    user.save()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<id>/resource/<int:resource_id>')
def get_resource(id, resource_id):
    pass


@bp.route('/users/<id>/resources')
def get_resources():
    pass
