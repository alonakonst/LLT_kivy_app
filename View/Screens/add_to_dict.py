from kivy.uix.screenmanager import Screen
from Model import DictionaryEntry
from kivy.lang import Builder
class AddToDict(Screen):

        # Todo Move to controller
    def insert(self):
            text = self.ids.word.text
            dictionary_entry = DictionaryEntry(text=text)
            dictionary_entry.save()

