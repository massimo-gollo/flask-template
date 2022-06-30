from flask import url_for
from app.database.db import mongo as me
from flask_user import UserMixin


class User(me.Document, UserMixin):
    username = me.StringField(default='')
    email = me.StringField(default='')
    password_hash = me.StringField(default='')
    active = me.BooleanField(default=True)

    def get_resources(self):
        from app.models.resource import Resource
        return Resource.objects.get_or_404(author=self)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            # 'resource_count': self.get_ruppus.count(),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'resources': url_for('api.get_resources', id=self.id),
                #  'avatar': self.avatar(128)
            }
        }

        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    # TODO add hash psw
    def set_password(self, password):
        self.password_hash = password


def __repr__(self):
    return '<User {}>'.format(self.username)
