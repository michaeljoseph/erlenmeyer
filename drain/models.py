from peewee import *
import drain
print(dir(drain))
from drain.app import db


class User(Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

class Birthday(Model):
    birthday = DateField()
    is_relative = BooleanField()
    class Meta:
        database = db
