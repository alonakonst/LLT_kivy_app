from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.list import ThreeLineListItem
from Model import DictionaryEntry
from kivymd.uix.card import MDCardSwipe
from Controller import DictionaryController

class ListItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class Dictionary(Screen):

    def __init__(self, **kwargs):
        self.controller=DictionaryController(self)
        super().__init__(**kwargs)


    def on_enter(self):
        for i in DictionaryEntry().select():
            self.ids.container.add_widget(
                ListItem(
                    text=f"{i.text}",
                    secondary_text = f"In English: {i.translation}",
                    tertiary_text = f"Notes: {i.notes}",
                )
            )


    def remove_item(self):
        list_item = self.ids.content.parent.parent
        list_item.parent.remove_widget(list_item)
