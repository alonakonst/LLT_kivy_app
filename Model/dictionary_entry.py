from .base import Base

from peewee import TextField


class DictionaryEntry(Base):
    text = TextField(null=False)
    translation = TextField(null=True)
    notes = TextField(null=True)

    def __str__(self) -> str:
        return f"{{id={self.id} text={self.text!r} translation={self.translation!r} notes={self.notes!r}}}"
