from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder
class Dictionary(Screen):
    pass

Builder.load_file(os.path.join(os.path.dirname(__file__), "dictionary.kv"))