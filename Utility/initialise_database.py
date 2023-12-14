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
    DictionaryEntry(text='lykke', translation='happiness', notes='there is a book called Lykke').save()
    DictionaryEntry(text='skov', translation='forest', notes='Himmel Skov').save()
    DictionaryEntry(text='drøm', translation='dream', notes='at drømme').save()
    DictionaryEntry(text='frokost', translation='lunch', notes='julefrokost').save()
    DictionaryEntry(text='stjerne', translation='star', notes='').save()
    DictionaryEntry(text='hav', translation='sea', notes='middelhavet').save()
    DictionaryEntry(text='elefant', translation='elephant',
                    notes='en elefant').save()
    DictionaryEntry(text='smil', translation='smile', notes='').save()
    DictionaryEntry(text='Spiser du krabbe?', translation='Do you eat crab?',
                    notes='').save()
    DictionaryEntry(text='solnedgang', translation='sunset', notes='').save()
    DictionaryEntry(text='en ugl',
                    translation='an owl',
                    notes='').save()
    DictionaryEntry(text='Dyret er der',
                    translation='The animal is there',
                    notes='dyr is animal').save()
    DictionaryEntry(text='sulten',
                    translation='hungry',
                    notes='Jeg er sulten').save()
    DictionaryEntry(text='ko',
                    translation='cow',
                    notes='en ko, koen').save()
    DictionaryEntry(text='anderledes', translation='different', notes='').save()
    DictionaryEntry(text='jeg stoler på dig',
                    translation='I trust you',
                    notes='').save()
    DictionaryEntry(text='især',
                    translation='Especially',
                    notes='usually in the beginning of the sentence').save()
    DictionaryEntry(text='i det mindste',
                    translation='at least',
                    notes='').save()
    DictionaryEntry(text='bare',
                    translation='just',
                    notes='').save()
    DictionaryEntry(text='selv',
                    translation='even',
                    notes='').save()
    DictionaryEntry(text='væk',
                    translation='away',
                    notes='').save()
    DictionaryEntry(text='langt væk',
                    translation='far away',
                    notes='').save()
    DictionaryEntry(text='tydeligt',
                    translation='clearly',
                    notes='').save()
    DictionaryEntry(text='årtier',
                    translation='decades',
                    notes='').save()
    DictionaryEntry(text='klatre',
                    translation='climb',
                    notes='').save()
    DictionaryEntry(text='sejle',
                    translation='sail',
                    notes='').save()
    DictionaryEntry(text='alten',
                    translation='balcony',
                    notes='').save()
    DictionaryEntry(text='afdeling',
                    translation='department',
                    notes='').save()
    DictionaryEntry(text='udvalg',
                    translation='selection',
                    notes='').save()
    DictionaryEntry(text='udforsk',
                    translation='explore',
                    notes='').save()
    DictionaryEntry(text='nemt',
                    translation='easily',
                    notes='').save()
    DictionaryEntry(text='umuligt',
                    translation='impossible',
                    notes='').save()
    DictionaryEntry(text='hvid',
                    translation='white',
                    notes='').save()
    DictionaryEntry(text='lækker',
                    translation='delicious',
                    notes='En lækker brun kop kaffe').save()
    DictionaryEntry(text='and',
                    translation='duck',
                    notes='').save()
    DictionaryEntry(text='køkken',
                    translation='kitchen',
                    notes='').save()
    DictionaryEntry(text='Hvor er hunden',
                    translation='Where is the dog',
                    notes='').save()
    DictionaryEntry(text='Han kan lide kylling',
                    translation='he likes chicken',
                    notes='').save()
    DictionaryEntry(text='der er en fugl',
                    translation='there is a bird',
                    notes='').save()
    DictionaryEntry(text='lille',
                    translation='small',
                    notes='').save()
    DictionaryEntry(text='en fugl i et træ',
                    translation='a bird in a tree',
                    notes='').save()
    DictionaryEntry(text='Danmark er et lille land. Danmark består af halvøen Jylland, tre store øer og 403 små øer.',
                    translation='',
                    notes='learn how to pronounce till next class').save()
    DictionaryEntry(text='knuss',
                    translation='',
                    notes='use this in the end of en email to the friend or family').save()
    DictionaryEntry(text='øre',
                    translation='ear',
                    notes='').save()
    DictionaryEntry(text='Hun fået job som taxachauffør',
                    translation='He have got a job as a taxidriver',
                    notes='lønnen er god').save()


def initialise_database(*, dummy=False):
    with database:
        database.create_tables(TABLES, safe=True)

    if dummy and is_database_empty():
        create_dummy_database()
