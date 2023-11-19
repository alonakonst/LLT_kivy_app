from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.list import ThreeLineListItem
from Model import DictionaryEntry
class Dictionary(Screen):
    table = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        word = ''
        for i in DictionaryEntry().select():
            word = i.text
            self.ids.container.add_widget(
                ThreeLineListItem(
                    text=f"{word}",
                    secondary_text = "Translation:",
                    tertiary_text = "Notes:"
                )
            )

