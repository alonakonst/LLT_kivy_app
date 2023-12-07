from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from Model import DictionaryEntry
from kivymd.uix.card import MDCardSwipe
from Controller import DictionaryController

class Dictionary(Screen):

    def __init__(self, **kwargs):
        self.controller = DictionaryController(self)
        super().__init__(**kwargs)

    #TODO MOVE DictionaryEntry().select() to controller
    #TODO: if there are no notes, then write: no notes
    def on_enter(self):
        for i in DictionaryEntry().select():
            self.ids.container.add_widget(
                ListItem(
                    id=i.id,
                    text=f"{i.text}",
                    secondary_text=f"in English: {i.translation}",
                    tertiary_text=f"notes: {i.notes}",
                )
            )


    def remove_item(self, dictionary_entry):

        #removes list item from the screen
        list_item = self.ids.content.parent.parent
        list_item.parent.remove_widget(list_item)

        #removes the record from the database
        Dictionary().controller.remove_dictionary_entry(dictionary_entry)

    def show_search_results(self):
        print('it works')

    def show_popup(self, instance):
        popup = PopupContent(instance)
        popup.open()


class ListItem(MDCardSwipe):
    id = NumericProperty()
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()

class PopupContent(Popup):
    def __init__(self, instance, **kwargs):
        super().__init__(**kwargs)
        self.ids.full_word.text = instance.text
        self.ids.full_translation.text = instance.secondary_text
        self.ids.full_notes.text = instance.tertiary_text