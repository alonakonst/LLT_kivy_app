from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty
class Dictionary(Screen):
    table = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_table()


    def add_table(self):
        if not self.table:
             self.table = MDDataTable(
                 column_data=[
                     ("Word/Phrase", dp(30)),
                     ("Translation", dp(30)),
                     ("Notes", dp(30))
                 ]
             )
        self.add_widget(self.table)


#Builder.load_file(os.path.join(os.path.dirname(__file__), "dictionary.kv"))