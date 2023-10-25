from .base import Base

from peewee import TextField


class DictionaryEntry(Base):
    text = TextField(null=False)
    translation = TextField(null=True)
    notes = TextField(null=True)
