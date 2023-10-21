import sqlite3
from sqlite3 import connect

class MainScreenModel:
    db = None
    @staticmethod
    def connectDatabase():
        MainScreenModel.db = connect('Model/dictionary.db')
        cur = MainScreenModel.db.cursor()
        cur.execute("""CREATE TABLE if not exists words(
                word text
                translation text
                notes text)
            """)
        MainScreenModel.db.commit()
        print("connection to database")

    @staticmethod
    def insert_words(word):
        cur = MainScreenModel.db.cursor()
        cur.execute("INSERT INTO words VALUES(:val)",
{
                'val': f'{word}',
            })
        MainScreenModel.db.commit()

    @staticmethod
    def show_words():
        cur = MainScreenModel.db.cursor()
        cur.execute("SELECT * FROM words")
        records = cur.fetchall()
        return records
        MainScreenModel.db.commit()