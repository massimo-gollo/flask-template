from app.models.user import User
from app.database.db import mongo as me


class ResourceItem(me.EmbeddedDocument):
    entry = me.StringField()
    marked = me.BooleanField(
        default=False
    )


class Resource(me.Document):
    author = me.ReferenceField(User, required=True)
    title = me.StringField()
    list = me.EmbeddedDocumentListField(ResourceItem)

    def __repr__(self):
        return '<User {}>'.format(self.username)
