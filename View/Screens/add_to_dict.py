from kivy.uix.screenmanager import Screen
from Model import DictionaryEntry
import os
from kivy.lang import Builder
class AddToDict(Screen):

        # Todo Move to controller
    def insert(self):
        text = self.ids.word.text
        dictionary_entry = DictionaryEntry(text=text)
        dictionary_entry.save()

        # Todo Move to controller
   # def show(self):
      #  word = ''
       # for i in DictionaryEntry().select():
       #     word = f'{word}\n{i.text}'
        #    self.manager.get_screen("dictionary").ids.word_label.text = f'{word}'
         #   print(word)

#Builder.load_file(os.path.join(os.path.dirname(__file__), "add_to_dict.kv"))