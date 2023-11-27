"""
First if the database exists prompt to delete.
Fill the database with words
"""

from Model import DictionaryEntry

from pathlib import Path


def create_dummy_database():
    database_path = Path('database.db')
    if database_path.exists():
        yes = input("Recreated database? [y/N]: ")

        if yes == "y":
            database_path.unlink()
            from Utility import initialise_database

            initialise_database()
        else:
            print(f'{yes!r} not {"y"!r}')

    DictionaryEntry(text='lykke', translation='happiness', notes='1234567890').save()
    DictionaryEntry(text='skov', translation='forest', notes='1234567890').save()
    DictionaryEntry(text='drøm', translation='dream', notes='1234567890').save()
    DictionaryEntry(text='frokost', translation='lunch', notes='1234567890').save()
    DictionaryEntry(text='stjerne', translation='star', notes='1234567890').save()
    DictionaryEntry(text='hav', translation='sea', notes='1234567890').save()
    DictionaryEntry(text='bog', translation='This is a annoyingly long phrase, probably hard to render', notes='1234567890').save()
    DictionaryEntry(text='smil', translation='smile', notes='1234567890').save()
    DictionaryEntry(text='Vinter', translation='winter', notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='solnedgang', translation='sunset', notes='1234567890').save()
    DictionaryEntry(text='This is a annoyingly long phrase, probably hard to render', translation='This is a annoyingly long phrase, probably hard to render', notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='1',
                    translation='This is a annoyingly long phrase, probably hard to render',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='2',
                    translation='3',
                    notes='This is a annoyingly long phrase, probably hard to render').save()
    DictionaryEntry(text='4',
                    translation='This is a annoyingly long phrase, probably hard to render',
                    notes='5').save()

    print("Success!")

if __name__ == '__main__':
    create_dummy_database()
