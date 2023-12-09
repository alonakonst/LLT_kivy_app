"""
Create all the tables in the database using initialise_database
Usage:
    All Models that are stored in the database should be imported and included in the TABLES array (as classes)
"""

from Model import database

from Model import DictionaryEntry

TABLES = [
    DictionaryEntry,
]


def is_database_empty():
    for table in TABLES:
        if table.select():
            return False

    return True


def create_dummy_database():
    DictionaryEntry(text='lykke', translation='happiness', notes='1234567890').save()
    DictionaryEntry(text='skov', translation='forest', notes='1234567890').save()
    DictionaryEntry(text='drøm', translation='dream', notes='1234567890').save()
    DictionaryEntry(text='frokost', translation='lunch', notes='1234567890').save()
    DictionaryEntry(text='stjerne', translation='star', notes='1234567890').save()
    DictionaryEntry(text='hav', translation='sea', notes='1234567890').save()
    DictionaryEntry(text='bog 1', translation='This is a annoyingly long phrase, probably hard to render',
                    notes='1234567890').save()
    DictionaryEntry(text='smil', translation='smile', notes='1234567890').save()
    DictionaryEntry(text='Vinter', translation='winter',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='solnedgang', translation='sunset', notes='1234567890').save()
    DictionaryEntry(text='This is a annoyingly long phrase, probably hard to render',
                    translation='This is a annoyingly long phrase, probably hard to render',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='1 1',
                    translation='This is a annoyingly long phrase, probably hard to render',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='2 1',
                    translation='3',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='4 1',
                    translation='This is a annoyingly long phrase, probably hard to render',
                    notes='5').save()


def initialise_database(*, dummy=False):
    with database:
        database.create_tables(TABLES, safe=True)

    if dummy and is_database_empty():
        create_dummy_database()
