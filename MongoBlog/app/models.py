from django.db import models
from mongoengine import *
from MongoBlog.settings import DBNAME
connect(DBNAME)

class User(Document):
    email = StringField(required=True)
    user_name = StringField(max_length=20)
    full_name = StringField(max_length=60)


class Comment(EmbeddedDocument):
    content = StringField()
    user_name = StringField(max_length=120)


class Blog(Document):
    title = StringField(max_length=120, required=True)
    content = StringField()
    image_path = StringField()
    link_url = StringField()
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
