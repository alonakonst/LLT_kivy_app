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


def initialise_database():
    with database:
        database.create_tables(TABLES, safe=True)
