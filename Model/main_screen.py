import sqlite3
import os
from sqlite3 import connect

class MainScreenModel:
    def __init__(self):
        self.conn = sqlite3.connect('Model/dictionary.db')
        self.cur = self.conn.cursor()


        try:
            MainScreenModel.__init__(self)
        except Exception as e:
            print(e)

    def __del__(self):
        self.conn.close()

    @staticmethod
    def create_table():
        pass

    @staticmethod
    def insert():
        pass

    @staticmethod
    def show():
        pass


class Words(MainScreenModel):

    def __init__(self):
        super().__init__()

    def create_table(self):
        self.cur.execute("""CREATE TABLE if not exists words(
                      word text
                      translation text
                      notes text)
                  """)
        self.conn.commit()

    def insert(self, word):
        self.cur.execute("INSERT INTO words VALUES(:val)",
                    {
                        'val': f'{word}',
                    })

        self.conn.commit()

    # @staticmethod
    def show(self):
        self.cur.execute("SELECT * FROM words")
        records = self.cur.fetchall()
        self.conn.commit()
        return records


