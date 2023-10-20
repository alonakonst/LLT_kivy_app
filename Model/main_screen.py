import sqlite3
from View.main_screen import InsertIntoDictionary
class MainScreenModel:

    con = sqlite3.connect('dictionary.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE if not exists words(
            word text
            translation text
            notes text)
        """)
    con.commit()
    con.close()
    print("connection to database")
