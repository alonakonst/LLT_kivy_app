from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder
class Practise(Screen):
    pass

Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))