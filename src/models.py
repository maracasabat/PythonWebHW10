from datetime import datetime

from mongoengine import *

connect(host="mongodb://localhost:27017/address_book")


class User(Document):
    name = StringField(max_length=120, min_length=2, required=True)
    phone = StringField(max_length=20, unique=True, default=None)
    email = EmailField(required=True, unique=True, default=None)
    address = StringField(max_length=120, default=None)
    added_on = DateTimeField(default=datetime.utcnow)
