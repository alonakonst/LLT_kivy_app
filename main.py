import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sqlite3

class WelcomeWindow(Screen):
   user_name = ObjectProperty(None)

   def btn(self):
       print("Name:", self.user_name.text)
       self.user_name.text = ""


class SecondWindow(Screen):
    pass

class InsertIntoDictionary(Screen):
    def submit_new_word(self):
        con = sqlite3.connect('dictionary.db')
        cur = con.cursor()
        cur.execute("INSERT INTO words VALUES(:first)",
{
                'first': self.new_word.text,
            })
        con.commit()
        con.close()

    def show_dictionary(self):
        con = sqlite3.connect('dictionary.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM words")
        records = cur.fetchall()
        word = ''
        for i in records:
            word = f'{word}\n{i[0]}'
            self.manager.get_screen("dictionary").ids.word_label.text = f'{word}'
        con.commit()
        con.close()

class DisplayDictionary(Screen):
    pass
class WindowManager(ScreenManager):
    pass

con = sqlite3.connect('dictionary.db')
cur = con.cursor()
cur.execute("""CREATE TABLE if not exists words(
        word text
        translation text
        notes text)
    """)
con.commit()
con.close()

kv = Builder.load_file("style.kv")

class LLTApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    LLTApp().run()