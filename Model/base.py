from .database import database

from peewee import Model


class Base(Model):
    class Meta:
        database = database
