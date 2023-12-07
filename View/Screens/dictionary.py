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

    #TODO Shorten this finction
    def show_popup(self, instance):
        layout = MDBoxLayout(orientation='vertical', adaptive_height=True, padding='0dp')  # set orientation and use adaptive_height
        text = MDLabel(text=instance.text, halign="left", valign="top", adaptive_height=True)
        translations = MDLabel(text=instance.secondary_text, halign="left", valign="bottom", adaptive_height=True)
        notes = MDLabel(text=instance.tertiary_text, halign="left", valign="bottom", adaptive_height=True)
        layout.add_widget(text)
        layout.add_widget(translations)
        layout.add_widget(notes)
        dialog = MDDialog(
            type="custom",
            content_cls=ScrollView(),  # set content of dialog to a ScrollView
            buttons=[
                MDFlatButton(
                    text="edit",
                    on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
        dialog.content_cls.add_widget(layout)  # add the BoxLayout to the ScrollView
        dialog.update_height()  # update the dialog
        dialog.open()


class ListItem(MDCardSwipe):
    id = NumericProperty()
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()

